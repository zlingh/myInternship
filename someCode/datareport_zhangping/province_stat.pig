register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

dlilog = load '/dp/dailylaunch/2012111[1-7]/compacted/*' using dli_loader;

fltd = filter dlilog by LOWER(country) == 'cn';

gnrd = foreach fltd generate province as pro, model, access_type as access, access_subtype as subtype, session_summary.launch_count as launches;
grpd = group gnrd by (pro, model, access, subtype);

C = foreach grpd generate flatten(group), SUM(gnrd.launches);

set default_parallel 10;
set job.name 'proAccessStat' ;
store C into '/tmp/pro_access_stat_nov' using PigStorage('\t');
