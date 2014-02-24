register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';
register 'center_udf.py' using jython as getc_udf;

log = load '/logs/app_logs/201301[0-2][1-3]/*' using ua_loader;
andlog = filter log by device_info.id is not null and LOWER(device_info.os) == 'android';
ses_start = foreach andlog generate device_info.id as id, flatten(session_start);

gps_start = filter ses_start by (session_start::lng is not null) and (session_start::lat is not null) and (ABS(session_start::lng)>0) and (session_start::lat >39.68) and (session_start::lat <40.20) and (session_start::lng>116.08)and (session_start::lng<116.74);

gps_center = foreach gps_start generate id, getc_udf.getlongcenter(session_start::lng) as lngc, getc_udf.getlatcenter(session_start::lat) as latc, SUBSTRING(id, 0, 2) as flag; 

gps_centerg1 = group gps_center by(lngc, latc, flag);

gps_centerdis1 = foreach gps_centerg1 { users=distinct gps_center.id; generate flatten(group), COUNT(gps_center.id) as launchNum, COUNT(users)as userNum; }

gps_centerg2 = group gps_centerdis1 by (lngc, latc);

gps_centerdis2 = foreach gps_centerg2 { generate flatten(group), SUM(gps_centerdis1.launchNum) as launchNum, SUM(gps_centerdis1.userNum) as userNum; }

set default_parallel 20;
set job.name 'gps_activef1';
store gps_centerdis2 into '/tmp/gps_centerdis201301f1' using PigStorage('\t');
--store gps_centerdis1 into '/tmp/gps_centerdis10219b2' using PigStorage('\t');
