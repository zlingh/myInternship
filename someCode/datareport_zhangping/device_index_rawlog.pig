register '/home/yunbg/datareport/jars/elephant-bird-2.1.11.jar';
register '/home/yunbg/datareport/jars/elephant-bird-examples-2.1.11.jar';
import '/home/yunbg/datareport/import.pig';

log = load '/user/yunbg/logsample/2012121205*' using ua_loader; 

cnlog= filter log by LOWER(country)== 'cn';

glog = foreach cnlog generate device_info.os as os, device_info.os_version as os_version, device_info.model as model, device_info.cpu as cpu, device_info.resolution.height as height, device_info.resolution.width as width, device_info.is_jailbroken as jailbreak, device_info.id as id, COUNT(session_start) as launchs;

grlog = group glog by (os, os_version, model, cpu, height, width, jailbreak);

C = foreach grlog { dist = distinct glog.id; generate flatten(group), COUNT(dist) as modelNum, SUM(launchs) as launchNum; }

set default_parallel 10;
set job.name 'Device_index_rawlog';
store C into '/tmp/device_index_rawlog' using PigStorage('\t');

--get the data from rawlog for the datareport pigs to compute,can be used to get the os from rawlog's one day's data
