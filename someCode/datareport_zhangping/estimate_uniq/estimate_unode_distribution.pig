log = load '/tmp/estimate_11_unode4_Raw_stat/part*' using PigStorage('\t') as (usr: chararray, lognum: int);

grpd = group log by lognum;

C = foreach grpd {generate flatten(group), COUNT(log);}

set default_parallel 10;
set job.name 'estimateDistribution';
store C into '/tmp/estimate11_unode4_Distribution' using PigStorage('\t');
