register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

dlilog = load '/logs/app_logs/2012121[0-6]/*' using ua_loader;

fltd = filter dlilog by LOWER(country) == 'th';

gnrd = foreach fltd generate app_info.key as app, device_info.id as user, COUNT(session_start) as launches;
grpd = group gnrd by app;

C = foreach grpd {
	uniquser = distinct gnrd.user;
	generate flatten(group), COUNT(uniquser), SUM(gnrd.launches);
}
set default_parallel 10;
set job.name 'TH_stat' ;
store C into '/tmp/th_stat' using PigStorage('\t');
