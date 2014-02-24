register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

log = load '/logs/app_logs/20121205/*/*unode04*' using ua_loader;
--fltd = filter log by app_info.key == '4f8ce79d5270157c0f000053';

fltd = filter log by LOWER(device_info.os) == 'ios';

gnrd = foreach fltd generate device_info.id as id;
grpd = group gnrd by id;

C = foreach grpd {generate flatten(group), COUNT(gnrd);}

set default_parallel 10;
set job.name 'estimateRaw';
store C into '/tmp/estimate_ios_unode4_Raw_stat' using PigStorage('\t');
