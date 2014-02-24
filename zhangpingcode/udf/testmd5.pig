register '/home/yunbg/datareport/jars/elephant-bird-2.1.11.jar';
register '/home/yunbg/datareport/jars/elephant-bird-examples-2.1.11.jar';
register 'pigudff.jar';
import '/home/yunbg/datareport/import.pig';
define toumid com.umeng.dm.pigudf.toumid();
DEFINE teststr `toumidstr.py` SHIP('toumidstr.py');

log = load '/logs/app_logs/20130121/*' using ua_loader;
--log = load '/logs/app_logs/20130120/22/*' using ua_loader;

log = foreach log generate device_info.id as did, device_info.idmd5 as idmd5;

log1 = foreach log generate did, idmd5, com.umeng.dm.pigudf.toumid(did, idmd5) as javaidmd5;

log1 = distinct log1;

log2 = STREAM log THROUGH teststr as (pdid:chararray,pidmd5:chararray,pymd5:chararray);

log2 =distinct log2;

log11 = foreach log1 generate CONCAT(did, idmd5) as j, javaidmd5 as jmd5;

log22 = foreach log2 generate CONCAT(pdid, pidmd5) as p, pymd5;

log3 = join log11 by j , log22 by p;

log4 = filter log3 by jmd5!=pymd5;




set job.name 'umidtest2zhangping';
set default_parallel 7
store log4 into '/tmp/zhangping/testumidc9' using PigStorage('\t');
--store logido into '/tmp/zhangping/testdevicid' using PigStorage('\t');






	
