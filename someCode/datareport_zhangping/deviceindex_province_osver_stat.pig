register '/home/xiarong/pigs/jars/elephant-bird-2.1.11.jar';
register '/home/xiarong/pigs/jars/elephant-bird-examples-2.1.11.jar';
import '/home/xiarong/pigs/import.pig';

dlilog = load '/dp/dailylaunch/201212[0-2][1-2]/compacted/*' using dli_loader;

fltd = filter dlilog by LOWER(country) == 'cn';

gnrd = foreach fltd generate umid, os_version, province as pro, model, access_type as access, access_subtype as subtype, session_summary.launch_count as launches;
grpd = group gnrd by (os_version, pro, model, access, subtype);

C = foreach grpd {
     users = distinct gnrd.umid;
     generate flatten(group), COUNT(users), SUM(gnrd.launches);}

set default_parallel 10;
set job.name 'proAccessOsverStat' ;
store C into '/tmp/device_index/pro_access_osver_stat_201209' using PigStorage('\t');
