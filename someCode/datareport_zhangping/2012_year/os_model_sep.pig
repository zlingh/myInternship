register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

log = load '/logs/app_logs/201209*/*' using ua_loader; 
--log = load '/logs/app_logs/20120829/{22,23}' using ua_loader; 

cnlog = filter log by LOWER(country)== 'cn';

glog = foreach cnlog generate device_info.os as os, device_info.model as model, device_info.id as id, SUBSTRING(device_info.id, 0, 2) as flag;

grlog = group glog by (os, model, flag);

C = foreach grlog { users = distinct glog.id; generate flatten(group), COUNT(users); } 

set default_parallel 20;
set job.name 'Device_osmodel_201209';
store C into '/tmp/device_index/device_osmodel_201209' using PigStorage('\t');
