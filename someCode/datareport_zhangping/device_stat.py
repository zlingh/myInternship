'''
Author: zhanping
Company: Umeng
Founction: Compute how many devices there are of each device_model from log20121201 to log20121227
Date: 20121227
'''

import traceback
import MySQLdb

dfp = open('device_stat_result', 'w')
def compute_device():  
    #use model_counters to save the answers from mysql,we let device_model+resolution+device_id as the key,value is 0
    #use answer to get the result
    model_counters={}
    answer={}
    logdb_conn=None
    try:
        #get the log from request_log_20121201 to request_log_20121225
        logdb_conn=MySQLdb.connect(host="10.18.11.10", user="ads", passwd="ads", db="umeng", charset="utf8")
        for day in range(1201,1226):
            sql="SELECT device_model, device_id, resolution FROM request_log_2012" + str(day) \
                 +" WHERE device_id IS NOT NULL limit 100"
            cur=logdb_conn.cursor()
            cur.execute(sql)
            cn=[v[0] for v in cur.description]
            r=cur.fetchone()
            while r!=None:
                plog=dict((cn[k], r[k].encode("utf8")) for k in range(len(cn)))
                modeltype=plog['device_model']+'\t'+plog['resolution']+'\t'+plog['device_id']
                if modeltype!=None:
                    model_counters[modeltype]=1
                r=cur.fetchone()
            cur.close()
    except:
        traceback.print_exc()
    finally:
        if logdb_conn:
            logdb_conn.close()
    
    try:
        for model1 in model_counters:
            tmp=model1.strip().split('\t')
            tmp1=tmp[0]+'\t'+tmp[1]
            if tmp1 not in answer:
                answer[tmp1]=1
            else:
                answer[tmp1]+=1
        for model2 in answer:
            dfp.write(model2+'\t'+str(answer[model2])+'\n')

    except:
        traceback.print_exc()


if __name__=='__main__':
    compute_device()
