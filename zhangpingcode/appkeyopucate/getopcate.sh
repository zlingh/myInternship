#!/bin/sh
td=`date +%Y%m%d`
#yd=`expr $td - 1`
yd=`date  +"%Y%m%d" -d  "-1 days"`
echo $yd
python /home/xiarong/appDB/appkeyopucate/get_app_op_exts.py $td
python /home/xiarong/appDB/appkeyopucate/getappkey_opucate.py $td
if test -s /home/xiarong/appDB/data/app_op_exts_mangoDB_${td}; then
	rm /home/xiarong/appDB/data/app_op_exts_mangoDB_${yd}
else
	echo "empty"
fi
if test -s /home/xiarong/appDB/data/appkey_opcate_${td}; then
	rm /home/xiarong/appDB/data/appkey_opcate_${yd}
else
	echo "empty"
fi
