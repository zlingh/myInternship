register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';
register 'udf_reso.py' using jython as reso_udf;
dlilog = load '/dp/dailylaunch/201212*/compacted/*' using dli_loader;
statlog = foreach dlilog generate umid, model, session_summary.launch_count as launches, reso_udf.getreso(resolution.height, resolution.width) as reso, SUBSTRING(umid,0,2) as flag;

grpmodel = group statlog by (model, reso, flag);

gnrd = foreach grpmodel {
	users = distinct statlog.umid;
	generate flatten(group), COUNT(users), SUM(statlog.launches) ;}

set default_parallel 20;
set job.name 'active_device_201212' ;
store gnrd into '/tmp/device_index/active_device_201212_withreso' using PigStorage('\t');
