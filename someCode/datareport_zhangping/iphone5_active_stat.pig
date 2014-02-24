register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

dlilog = load '/dp/dailylaunch/2012121[0-6]/compacted/*' using dli_loader;

cntd = filter dlilog by LOWER(country) == 'cn';
fltd = filter cntd by (LOWER(model) == 'iphone5,1' or LOWER(model) == 'iphone5,2');

gnrd = foreach fltd generate model, access_type as access, access_subtype as subtype, province as pro, carrier, svr_date as date, session_summary.launch_count as num;
grpd = group gnrd by (date, model, access, subtype, pro, carrier);
K = foreach grpd generate flatten(group), SUM(gnrd.num);

ngnrd = foreach fltd generate model, umid, svr_date as date;
ngrpd = group ngnrd by (date, model);

C = foreach ngrpd {
	uniquser = distinct ngnrd.umid;
	generate flatten(group), COUNT(uniquser);
}
set default_parallel 5;
set job.name 'iPhone_5_stat_adhoc' ;
store C into '/tmp/iphone5_adhoc_stat/uniqdevice' using PigStorage('\t');
store K into '/tmp/iphone5_adhoc_stat/launches' using PigStorage('\t');
