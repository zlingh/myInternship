register '/home/yunbg/datareport/jars/elephant-bird-2.1.11.jar';
register '/home/yunbg/datareport/jars/elephant-bird-examples-2.1.11.jar';
import '/home/yunbg/datareport/import.pig';

log = load '/user/yunbg/logsample/2012121205*' using ua_loader; 

glog = foreach log generate device_info.model as model, device_info.resolution as resolution, device_info.cpu as cpu, device_info.os as os, device_info.os_version as os_version, device_info.id as id, session_start;

grlog = group glog by (model, resolution, cpu, os, os_version,id);

--统计每个device_id的启动次数
B = foreach grlog { generate flatten(group), COUNT(glog.session_start) as times; }

D = group B by(model, resolution, cpu, os, os_version);

C = foreach D { dist = distinct B.id; generate flatten(group), COUNT(dist), SUM(B.times); }

set default_parallel 10;
set job.name 'DeviceStat';
store C into '/tmp/device_stat2' using PigStorage('\t');

