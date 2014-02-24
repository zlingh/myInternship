register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';
register 'useday.py' using jython as dayudf;
register 'score.py' using jython as scoreudf;
dlilog = load '/dp/dailylaunch/2013040[1-3]/compacted/*' using dli_loader;
--dlilog = load '/dp/dailylaunch/20130401/compacted/part-r-0001*' using dli_loader;

gameid = load '/tmp/20130502_zhangping/gameapp.csv' as (gamekey:chararray, platform:chararray, tag:chararray);

usrlog =filter dlilog by umid is not null and app_key is not null and session_summary.launch_count >0
 and session_summary.duration_total < 100000000 and session_summary.duration_total >0;
usrlog = foreach usrlog generate umid, app_key, inst_at, session_summary.launch_count as launches, session_summary.duration_total as duration;
usrlog1= group usrlog by (umid,app_key,inst_at);
usrlogtmp = foreach usrlog1{ generate flatten(group), SUM(usrlog.launches) as launches, SUM(usrlog.duration) as duration; }

--inst = load '/user/xiarong/usr_data_pre/install_hisdata_0422/part*' as (key,appkey:chararray,install_at:chararray,os:chararray,umid:chararray,channel:chararray);
--usrloginst = join inst by (appkey, umid), usrlog by (app_key, umid);
--usrlog = foreach usrloginst generate key,appkey,install_at,os,umid,channel,launches, duration;
--store usrlog into '/tmp/20130502_zhangping/game_instst20130407' using PigStorage('\t');
apptotal1 = group usrlogtmp by app_key;
apptotal2 = group apptotal1 all;
apptotal = foreach apptotal2 generate group, COUNT(apptotal1) as allappNum;

usrtotal1 = group usrlogtmp by umid;
usrtotal2 = group usrtotal1 all;
usrtotal = foreach usrtotal2 generate group, COUNT(usrtotal1) as allusrNum;

usrlog = foreach usrlogtmp generate umid, app_key, dayudf.getuseday(inst_at,'2013-04-03',3) as useday, launches, duration;
usrlog = foreach usrlog generate umid, app_key, (double)launches/useday as launches, (double)duration/useday as duration, (double)duration/launches as duraperl;

usrlog = join usrlog by app_key, gameid by gamekey using 'replicated';
usrlog = foreach usrlog generate umid, app_key, launches, duration, duraperl, platform, tag;
usrlog1 = group usrlog by app_key;
usrlog = foreach usrlog1 generate flatten(usrlog), COUNT(usrlog) as appUserNum;

usrlog_g = group usrlog by (umid);
usertagscore = foreach usrlog_g generate group as umid, flatten(scoreudf.calcScore(usrlog, apptotal.allappNum, usrtotal.allusrNum));

set default_parallel 15;
set job.name 'game_duration_201304_zhangping';
store usrlogtmp into '/tmp/20130502_zhangping/game_duration20130403' using PigStorage('\t');

store usertagscore into '/tmp/20130502_zhangping/game_score20130403' using PigStorage('\t');
