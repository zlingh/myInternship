register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';
--register 'useday.py' using jython as dayudf;
register 'scoreidf.py' using jython as scoreudf;
register 'pigudfzp.jar';
define getday com.umeng.dm.pigudf.getUseDay2();
appzid = load '/tmp/20130502_zhangping/appkey_ucate.csv' as (appzkey:chararray, tag:chararray, platform:chararray);
--needid = load '/user/xiarong/usrinfo/usrgender' as (uid:chararray, gender:chararray, site:chararray);

dlilog = load '/dp/dailylaunch/201304*/compacted/*' using dli_loader;
usrlog =filter dlilog by umid is not null and SIZE(umid)>3 and app_key is not null and session_summary.launch_count >0
and session_summary.duration_total < 100000000 and session_summary.duration_total >0; 
usrlog = foreach usrlog generate umid, app_key, inst_at, session_summary.launch_count as launches, session_summary.duration_total as duration;
usrlog1= group usrlog by (umid,app_key,inst_at);
usrlogtmp = foreach usrlog1{ generate flatten(group), SUM(usrlog.launches) as launches, SUM(usrlog.duration) as duration; }

--usrlogtmp = load '/tmp/20130502_zhangping/game_duration20130403/*' as (umid:chararray, app_key:chararray, inst_at:chararray, launches:long, duration:long);
--usrlogtmp = filter usrlogtmp by SIZE(umid)>3;
--usrlogtmp = join usrlogtmp by umid, needid by uid using 'replicated'; 

usrlog = foreach usrlogtmp generate umid, app_key, getday(inst_at,'2013-04-30','30') as useday, launches, duration;
usrlog = foreach usrlog generate umid, app_key, (double)launches/useday as launches, (double)duration/useday as duration, (double)duration/launches as duraperl;

usrlog = join usrlog by app_key LEFT, appzid by appzkey using 'replicated';
usrlog = foreach usrlog generate umid, app_key, launches, duration, duraperl, platform, tag;

usrlog_g = group usrlog by (umid);
--usrlog_g = limit usrlog_g 1000;
usertagscore = foreach usrlog_g generate group as umid, flatten(scoreudf.calcScore(usrlog));

set default_parallel 20;
set job.name 'usr_ucate_zhangping';
store usertagscore into '/tmp/20130502_zhangping/ucate_score20130529' using PigStorage('\t');
