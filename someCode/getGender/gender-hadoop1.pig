register '/home/yunbg/datareport/jars/elephant-bird-2.1.11.jar';
register '/home/yunbg/datareport/jars/elephant-bird-examples-2.1.11.jar';
import '/home/yunbg/datareport/import.pig';

log = load '/user/yunbg/logsample/201212120*' using ua_loader; 

--cnlog = filter log by LOWER(country) == 'cn';

goodlog =filter log by (NOT IsEmpty(feedback));

log1 = foreach goodlog generate device_info.id as id, flatten(feedback);

glog = foreach log1 generate id, gender, age;

grlog = group glog by (id);

C = foreach grlog { genders = distinct glog.gender; ages =distinct glog.age; generate flatten(group), (COUNT(genders)>1?'collision':MAX(genders)), (COUNT(ages)>1?'collision':(chararray)MAX(ages));}

set default_parallel 8;
set job.name 'Device_gender_11125';
store C into '/tmp/device_index/device_gender_11125' using PigStorage('\t');
