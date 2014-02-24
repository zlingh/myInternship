#! /bin/sh
pig os_model_aug.pig;
pig os_model_sep.pig;
pig os_model_oct.pig;
pig ios_nojail_update.pig;

cat /mnt/hdfs/tmp/device_index/device_osmodel_201208/part* > osmodel_201208;
cat /mnt/hdfs/tmp/device_index/device_osmodel_201209/part* > osmodel_201209;
cat /mnt/hdfs/tmp/device_index/device_osmodel_201210/part* > osmodel_201210;
cat /mnt/hdfs/tmp/device_index/IOS_nojackupdate_9c12/part* > nojackupdate_9c12;

python model_dis.py osmodel_201208;
mv dataout aug_cn;
python model_dis.py osmodel_201209;
mv dataout sep_cn;
python model_dis.py osmodel_201210;
mv dataout oct_cn;
python nojialup.py nojackupdate_9c12;

