register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

log = load '/logs/app_logs/20121225/*' using ua_loader; 

cnlog= filter log by LOWER(country)== 'cn';

glog = foreach cnlog generate device_info.os as os, device_info.os_version as os_version, device_info.model as model, device_info.cpu as cpu, device_info.resolution.height as height, device_info.resolution.width as width, device_info.is_jailbroken as jailbreak, device_info.id as id, COUNT(session_start) as launches;

grlog = group glog by (os, os_version, model, cpu, height, width, jailbreak);

C = foreach grlog {
	dist = distinct glog.id; 
	generate flatten(group), COUNT(dist) as modelNum, SUM(glog.launches) as launchNum; }

set default_parallel 20;
set job.name 'Device_index_rawlog_201212';
store C into '/tmp/device_index/device_stat_raw_20121225' using PigStorage('\t');
