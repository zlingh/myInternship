import json
tmpf=open('tmp2','r')
for line in tmpf:
    k=json.loads(line)
    if "category_detail" in k and "category_general" in k:
        print k["category_detail"].encode('utf-8'), k["category_general"].encode('utf-8')
