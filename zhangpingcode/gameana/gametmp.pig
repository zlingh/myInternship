--register 'useday.py' using jython as dayudf;
register 'score.py' using jython as scoreudf;
--dlilog = load '/dp/dailylaunch/20130401/compacted/part-r-0001*' using dli_loader;
register 'pigudfzp.jar';
define getday com.umeng.dm.pigudf.getUseDay2();
gameid = load '/tmp/20130502_zhangping/gameapp.csv' as (gamekey:chararray, platform:chararray, tag:chararray);

usrlogtmp = load '/tmp/20130502_zhangping/game_duration20130403/part-r-00001' as (umid:chararray, app_key:chararray, inst_at:chararray, launches:long, duration:long);
--inst = load '/user/xiarong/usr_data_pre/install_hisdata_0422/part*' as (key,appkey:chararray,install_at:chararray,os:chararray,umid:chararray,channel:chararray);
--usrloginst = join inst by (appkey, umid), usrlog by (app_key, umid);
--usrlog = foreach usrloginst generate key,appkey,install_at,os,umid,channel,launches, duration;
--store usrlog into '/tmp/20130502_zhangping/game_instst20130407' using PigStorage('\t');
usrlogtmp = filter usrlogtmp by SIZE(umid)>3;

apptotal1 = foreach usrlogtmp generate app_key, SUBSTRING(app_key, 0, 2) as flag;
apptotal2 = group apptotal1 by flag;
apptotal2 = foreach apptotal2 {appn =distinct apptotal1.app_key; generate group as flag, COUNT(appn) as allappNum;}
apptotal3 = group apptotal2 all;
apptotal = foreach apptotal3 generate group, SUM(apptotal2.allappNum) as allappNum;

usrtotal1 = foreach usrlogtmp generate umid, SUBSTRING(umid, 0, 2) as flag;
usrtotal2 = group usrtotal1 by flag;
usrtotal2 = foreach usrtotal2 { usrn = distinct usrtotal1.umid; generate group as flag, COUNT(usrn) as allusrNum;}
usrtotal3 = group usrtotal2 all;
usrtotal = foreach usrtotal3 generate group, SUM(usrtotal2.allusrNum) as allusrNum;

usrlog = foreach usrlogtmp generate umid, app_key, getday(inst_at,'2013-04-03','3') as useday, launches, duration;
usrlog = foreach usrlog generate umid, app_key, (double)launches/useday as launches, (double)duration/useday as duration, (double)duration/launches as duraperl;

usrlog = join usrlog by app_key LEFT, gameid by gamekey using 'replicated';
usrlog = foreach usrlog generate umid, app_key, launches, duration, duraperl, platform, tag;
--usrlog1 = group usrlog by app_key;
--usrlog = foreach usrlog1 generate flatten(usrlog), COUNT(usrlog) as appUserNum;

appuser = foreach usrlog generate umid, SUBSTRING(umid,0,2) as flag, app_key;
appuser1 = group appuser by (app_key, flag);
appuser1 = foreach appuser1 { generate flatten(group), COUNT(appuser) as appUserNum;}
appuser2 = group appuser1 by app_key;
appuser = foreach appuser2 {generate group as app_key2, SUM(appuser1.appUserNum) as appUserNum;}
usrlog = join usrlog by app_key, appuser by app_key2 using 'replicated';
usrlog = foreach usrlog generate umid, app_key, launches, duration, duraperl, platform, tag, appUserNum;

usrlog_g = group usrlog by (umid);
usertagscore = foreach usrlog_g generate group as umid, flatten(scoreudf.calcScore(usrlog, apptotal.allappNum, usrtotal.allusrNum));

set default_parallel 15;
set job.name 'game_duration_201304_zhangping';
--store usrlogtmp into '/tmp/20130502_zhangping/game_duration20130403' using PigStorage('\t');

store usertagscore into '/tmp/20130502_zhangping/game2_score20130403' using PigStorage('\t');
