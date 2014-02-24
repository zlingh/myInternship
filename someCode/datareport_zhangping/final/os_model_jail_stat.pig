register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

log = load '/logs/app_logs/$yearmonth[0-2][1-2]/*' using ua_loader; 

cnlog = filter log by LOWER(country) == 'cn';

glog = foreach cnlog generate device_info.os as os, device_info.model as model, device_info.os_version as os_version, device_info.id as id,device_info.is_jailbroken as jailbreak, SUBSTRING(device_info.id, 0, 2) as flag;

grlog = group glog by (os, os_version, model, jailbreak, flag);

C = foreach grlog { users = distinct glog.id; generate flatten(group), COUNT(users); } 

set default_parallel 20;
set job.name 'Device_osmodeljail_$yearmonth';
store C into '/tmp/device_index/device_osmodeljail_$yearmonth' using PigStorage('\t');
