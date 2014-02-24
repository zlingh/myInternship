register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';
register 'udf_getft.py' using jython as getft_udf;
log = load '/logs/app_logs/2012{112[0-9],1130,12*}/*' using ua_loader; 

--log = load '/logs/app_logs/20121226/{22,23}' using ua_loader; 
--cnlog = filter log by LOWER(country) == 'cn';

goodlog =filter log by (COUNT(feedback)>0);

log1 = foreach goodlog generate device_info.id as id, flatten(feedback);

glog = foreach log1 generate id, gender, age;

grlog = group glog by (id);

C = foreach grlog { genders = distinct glog.gender; ages =distinct glog.age; generate flatten(group), getft_udf.getFGen(genders) as gen, getft_udf.getFAg(ages) as ag;}

set default_parallel 20;
set job.name 'Device_gender_11to12';
store C into '/tmp/device_index/device_gender_11to12' using PigStorage('\t');
