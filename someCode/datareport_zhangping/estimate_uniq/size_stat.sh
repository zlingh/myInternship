date=20121205
pa='estimate_05_unode4_Raw_stat'
npa='estimate05_Raw_stat'
a=`ls -l /mnt/hdfs/logs/app_logs/$date/*/*unode05*.lzo | awk 'BEGIN{s=0}{s=s+$5}END{print s}'`
b=`ls -l /mnt/hdfs/logs/app_logs/$date/*/*.lzo | awk 'BEGIN{s=0}{s=s+$5}END{print s}'`
echo "print $a/$b" | python 

cat /mnt/hdfs/tmp/$pa/part* | wc -l
cat /mnt/hdfs/tmp/$npa/part* | wc -l
