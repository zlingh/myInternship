register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

log = load '/logs/app_logs/20121212/*' using ua_loader;
andlog = filter log by LOWER(device_info.os) == 'android';
gps_start = filter andlog by session_start.lng is not null and session_start.lat is not null and ABS(latitude)>0 and ABS(longitude)>0;

latitude is not null and longitude is not null and ABS(latitude)>0 and ABS(longitude)>0;

gnrd = foreach fltd generate device_info.id as id, device_info.os as os, device_info.os_version as os_version, device_info.model as model, COUNT(error) as launches;
grpd = group gnrd by (model, os, os_version);

C = foreach grpd {dist = distinct gnrd.id; generate flatten(group), COUNT(dist), SUM(gnrd.launches);}

set default_parallel 10;
set job.name 'ErrorLogStat';
store C into '/tmp/errlog_stat' using PigStorage('\t');
