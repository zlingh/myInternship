user4 = load '/tmp/estimate_12_unode4_Raw_stat/part*' using PigStorage('\t') as (usr: chararray, lognum: int);
user5 = load '/tmp/estimate_12_unode5_Raw_stat/part*' using PigStorage('\t') as (usr: chararray, lognum: int);
grpd = join user4 by $0, user5 by $0;

set default_parallel 10;
set job.name 'recapatureEst';
store grpd into '/tmp/recapturejoinEst' using PigStorage('\t');
