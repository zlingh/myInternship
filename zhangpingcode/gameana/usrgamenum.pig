inst = load '/user/xiarong/usr_data_pre/install_hisdata_0422/part*' as (key,appkey:chararray,install_at:chararray,os:chararray,umid:chararray,channel:chararray);

gameid = load '/tmp/20130502_zhangping/gameapp.csv' as (gamekey:chararray, platform:chararray, tag:chararray);

usrinsttag = join inst by appkey LEFT, gameid by gamekey using 'replicated';

usrlog = foreach usrinsttag generate umid, appkey, os, tag;

usrlog_g = group usrlog by umid;

usrtag = foreach usrlog_g { gameapp = filter usrlog by tag=='game' ; generate group as umid, COUNT(usrlog) as totalNum, COUNT(gameapp) as gameNum;}

usrtag = foreach usrtag generate umid, (double)(gameNum)/totalNum;

set default_parallel 15;
set job.name 'game_num_201304_zhangping';

store usrtag into '/tmp/20130502_zhangping/usr_gameappNum_0422' using PigStorage('\t');

