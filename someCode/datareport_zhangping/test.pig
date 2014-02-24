register '/home/shiwen/jars/elephant-bird-2.1.11.jar';
register '/home/shiwen/jars/elephant-bird-examples-2.1.11.jar';
import '/home/shiwen/import.pig';

log = load '/logs/app_logs/2012112[1-7]/*' using ua_loader;
fltd = filter log by COUNT(error)>0;

gnrd = foreach fltd generate device_info.id as id, device_info.os as os, device_info.os_version as os_version, device_info.model as model, COUNT(error) as launches;
grpd = group gnrd by model;

C = foreach grpd {dist = distinct gnrd.id; generate flatten(group), COUNT(dist), SUM(gnrd.launches);}

set default_parallel 10;
set job.name 'ErrorLogStat';
store C into '/tmp/errtest' using PigStorage('\t');
