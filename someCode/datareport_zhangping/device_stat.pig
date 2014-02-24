register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

log = load '/home/yunbg/logsample/part-r-00000.lzo' using ua_loader;

glog = foreach log generate device_info.model as model, device_info.resolution as resolution, device_info.cpu as cpu, device_info.os as os, device_info.os_version as os_version, device_info.id as id;
grlog = group glog by (model, resolution, cpu, os, os_version);

C = foreach grlog { dist = distinct glog.id; generate flatten(group), COUNT(dist); }

set default_parallel 10;
set job.name 'DeviceStat';
store C into '/tmp/device_stat' using PigStorage('\t');

