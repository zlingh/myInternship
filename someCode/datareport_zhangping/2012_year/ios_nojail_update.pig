register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

seplog = load '/logs/app_logs/201209*/*' using ua_loader; 
declog = load '/logs/app_logs/201212*/*' using ua_loader;
--seplog = load '/logs/app_logs/20120929/{22,23}' using ua_loader; 
--declog = load '/logs/app_logs/20121229/{22,23}' using ua_loader;

cnseplog = filter seplog by LOWER(country) == 'cn' and LOWER(device_info.os) matches 'ios|iphoneos' and device_info.is_jailbroken ==1;
cndeclog = filter declog by LOWER(country) == 'cn' and LOWER(device_info.os) matches 'ios|iphoneos' and device_info.os_version matches '6.*';

gcnseplog = foreach cnseplog generate device_info.model as model1, device_info.id as id1;
dgcnseplog = distinct gcnseplog;
gcndeclog = foreach cndeclog generate device_info.model as model2, device_info.id as id2;
dgcndeclog = distinct gcndeclog;

jlog = join dgcnseplog by id1, dgcndeclog by id2;

fjlog = foreach jlog generate id1 as id, model1 as model, SUBSTRING(id1, 0, 2) as flag;

grlog = group fjlog by (model, flag);

C = foreach grlog { generate flatten(group), COUNT(fjlog.id); } 

set default_parallel 20;
set job.name 'IOS_nojackupdate_9c12';
store C into '/tmp/device_index/IOS_nojackupdate_9c12' using PigStorage('\t');
