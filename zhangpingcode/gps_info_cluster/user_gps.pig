register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';
register 'bjses_udf.py' using jython as bjses;

--log = load '/logs/app_logs/$ymd/22/*unode04*' using ua_loader;
--log = load '/logs/app_logs/2013010*/*' using ua_loader;
log = load '/logs/app_logs/$ymd/*' using ua_loader;
andlog = filter log by device_info.id is not null and SIZE(device_info.id)>1 and app_info.key is not null and LOWER(device_info.os) == 'android';
ses_start = filter andlog by bjses.hasbj(session_start)=='y';
ses_end = filter andlog by bjses.hasbj(session_end)=='y';

ses_s = foreach ses_start generate device_info.id as id, app_info.key as appkey, flatten(bjses.bjbag_start(session_start));
ses_e = foreach ses_end generate device_info.id as id, app_info.key as appkey, flatten(bjses.bjbag_end(session_end));

gps_user_new = union ses_s, ses_e;

gps_user_newg= group gps_user_new by id;

new_res= foreach gps_user_newg generate flatten(gps_user_new); 

set default_parallel 12;
set job.name 'user_app_gps_$ymd';
store new_res into '/tmp/device_index/user_app_gps_new_$ymd' using PigStorage('\t');
--store gps_he into '/tmp/device_index/user_app_gps_old01' using PigStorage('\t');
