register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

log = load '/logs/app_logs/$ymd/*/*' using ua_loader;
andlog = filter log by LOWER(device_info.os) == 'android';
ses_start = foreach andlog generate device_info.id as id, app_info.key as appkey, flatten(session_start);

ses_end = foreach andlog generate device_info.id as id, app_info.key as appkey, flatten(session_end);

gps_start = filter ses_start by session_start::lng is not null and session_start::lat is not null and session_start::lng>116.08 and session_start::lng<116.74 and session_start::lat>39.68 and session_start::lat<40.20;

gps_end = filter ses_end by session_end::lng is not null and session_end::lat is not null and session_end::lng>116.08 and session_end::lng<116.74 and session_end::lat>39.68 and session_end::lat<40.20;

gps_ds = foreach gps_start generate id, appkey, session_start::lng as lng, session_start::lat as lat, session_start::gps_time as time;

gps_de = foreach gps_end generate id, appkey, session_end::lng as lng, session_end::lat as lat, session_end::gps_time as time;

gps_tmp = union gps_ds, gps_de;

gps_tmpg = group gps_tmp by id;

gps_res = foreach gps_tmpg generate flatten(gps_tmp);

set default_parallel 10;
set job.name 'GPS_LogStat_$ymd';
store gps_res into '/tmp/gps_log/gps_beijing_201301/gps_beijing_$ymd' using PigStorage('\t');
--store gps_he into '/tmp/gps_head' using PigStorage('\t');
