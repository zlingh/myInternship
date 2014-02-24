register '/home/yunbg/datareport/jars/elephant-bird-2.1.11.jar';
register '/home/yunbg/datareport/jars/elephant-bird-examples-2.1.11.jar';
import '/home/yunbg/datareport/import.pig';

dlilog = load '/user/yunbg/logsample/part*' using dli_loader; 
statlog = foreach dlilog generate cli_date, os_version, model, resolution.height as height, resolution.width as width, umid;

grpmodel = group statlog by (cli_date, model, os_version, height, width);

gnrd = foreach grpmodel {
        users = distinct statlog.umid;
        generate flatten(group), COUNT(users);}

set default_parallel 20;
set job.name 'yuandan_device' ;
store gnrd into '/tmp/yuandan_device' using PigStorage('\t');

--元旦新增设备
