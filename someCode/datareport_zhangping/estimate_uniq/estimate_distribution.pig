log = load '/tmp//part*' using PigStorage('\t') as (usr: chararray, lognum: int);

grpd = group log by lognum;

C = foreach grpd {generate flatten(group), COUNT(log);}

set default_parallel 1;
set job.name 'estimateDistribution';
store C into '/tmp/estimate_Distribution' using PigStorage('\t');
