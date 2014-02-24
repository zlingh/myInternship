#! /bin/sh
yearmonth=$1
pig -p yearmonth=$1 deviceindex_model_stat.pig;
pig -p yearmonth=$1 deviceindex_province_osver_stat.pig;
pig -p yearmonth=$1 os_model_jail_stat.pig;
# cat the file

modelreso=active_device_${yearmonth}_withreso;
verprovacc=pro_access_osver_stat_${yearmonth};
osmodeljail=device_osmodeljail_${yearmonth};

cat mnt/hdfs/tmp/device_index/active_device_${yearmonth}_withreso/par* > ./${modelreso};

cat mnt/hdfs/tmp/device_index/pro_access_osver_stat_${yearmonth}/par* > ./${verprovacc};

cat mnt/hdfs/tmp/device_index/device_osmodeljail_${yearmonth}/par* > ./${osmodeljail};


python compute.py ${modelreso} ${verprovacc} ${osmodeljail}


