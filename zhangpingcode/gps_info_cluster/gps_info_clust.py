'''
Created on Dec 27, 2012
company: umeng
@author: zhangping
'''

from matplotlib.pyplot import plot,savefig  
import sys, math, random 
import numpy as np 
import pylab as plt  
import time
lnglatrate=1.30467#the rate of lng and rate for the same distancebackg=plt.imread("beijing.png")

class Point:
    def __init__(self, coords, appkey='unknowapp',nowtime='unknowtime',reference=None):
        self.coords = coords#a list, so construct function 's param can be a list
        self.n = len(coords)
        self.reference = reference
        self.nowtime=nowtime
        self.appkey=appkey
    def __repr__(self):
        return str(self.coords)

class Cluster:
    def __init__(self, points):
        if len(points) == 0: raise Exception("ILLEGAL: EMPTY CLUSTER")
        self.points = points
        self.n = points[0].n
        for p in points:
            if p.n != self.n: raise Exception("ILLEGAL: MULTISPACE CLUSTER")
        self.centroid , self.dissum= self.calculateCentroidmedoid()
    def __repr__(self):
        return str(self.points)
    
    def update(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid ,self.dissum= self.calculateCentroidmedoid()
        return getDistancek(old_centroid, self.centroid)    

    def calculateCentroidmedoid(self):#find the median
        if len(self.points)==0:
            return self.centroid, 0
        minp=0
        mindissum=-1
        minsumfang=0.0        
        for i in range(len(self.points)):
            dissum=0.0
            sumfang=0.0
            for j in range(len(self.points)):
                if i!=j:
                    dis=getDistancek(self.points[i],self.points[j])
                    dissum+=dis
                    sumfang+=dis*dis
                else:
                    continue
            if mindissum>dissum or mindissum<0:
                mindissum=dissum
                minp=i
                minsumfang=sumfang         
        return self.points[minp], minsumfang

def selectkcen(points, k):#find k init points， we use k-means++'s method 
    result=[]
    d=[0.0 for t in points]#record the distance of points to cluster
    first=random.choice(points)
    clusters=[]
    clusters.append(Cluster([first]))
    for i in range(k):
        sum=0
        for k,pk in enumerate(points):
            smdis=getDistancek(pk,clusters[0].centroid)
            #smdis=v[tuple(pk.coords)][tuple(clusters[0].centroid.coords)]
            for j in range(i):
                dis=getDistancek(pk,clusters[j+1].centroid)
                #dis=v[tuple(pk.coords)][tuple(clusters[0].centroid.coords)]
                if dis<smdis:
                    smdis=dis              
            d[k]=smdis
            sum+=smdis
        sum*=random.random()
        for ii, di in enumerate(d):
            sum-=di
            if sum >0:
                continue
            clusters.append(Cluster([points[ii]]))
            result.append(points[ii])
            break
    return result

def kmeans(points, k, cutoff):
    # Randomly sample k Points from the points list, build Clusters around them
    #initial = random.sample(points, k)
    initial =selectkcen(points, k)    
    #print initial
    #print initial2
    clusters = []
    for p in initial:
        clusters.append(Cluster([p]))
    while True:
        lists = []
        for c in clusters: lists.append([])
        for p in points:
            smallest_distance = getDistancek(p, clusters[0].centroid)
            #smallest_distance=v[tuple(p.coords)][tuple(clusters[0].centroid.coords)]
            index = 0
            for i in range(len(clusters[1:])):
                distance = getDistancek(p, clusters[i+1].centroid)
                #distance = v[tuple(p.coords)][tuple(clusters[i+1].centroid.coords)]
                if distance < smallest_distance:
                    smallest_distance = distance
                    index = i+1
            lists[index].append(p)
    
        biggest_shift = 0.0
        for i in range(len(clusters)):
            shift = clusters[i].update(lists[i])
            biggest_shift = max(biggest_shift, shift)
        if biggest_shift < cutoff:
            break
    return clusters

def getDistancer(a, b):
    # Forbid measurements between Points in different spaces
    if a.n != b.n:
        raise Exception("ILLEGAL: NON-COMPARABLE POINTS")
    # Euclidean distance between a and b is sqrt(sum((a[i]-b[i])^2) for all i)
    ret = 0.0
    lng1=a.coords[0]
    lng2=b.coords[0]
    lat1=a.coords[1]
    lat2=b.coords[1]
    return disfromgt(lat1,lng1,lat2,lng2)
def getDistancek(a, b):
    ai=tuple(a.coords)
    bi=tuple(b.coords)
    if ai==bi:
        return 0.0
    if ai[0]<bi[0]:
        return v[ai][bi]
    if ai[0]>bi[0]:
        return v[bi][ai]
    if ai[1]<bi[1]:
        return v[ai][bi]
    if ai[1]>bi[1]:
        return v[bi][ai]
def makeRandomPoint(n, lower, upper):
    coords = []
    for i in range(n):
        coords.append(random.uniform(lower, upper))
    return Point(coords)


def plotpoint(points,clo):
    x=[p.coords[0] for p in points]
    #y=[p.coords[1] for p in points]
    y=[(p.coords[1]-39.668)*lnglatrate+39.668 for p in points]
    plt.plot(x,y,'.'+clo)

def disfromgt(lat,lng,glat,glng):
    EARTH_RADIUS = 6378.137
    PI=3.1415926535
    radLat1 = lat * PI / 180.0
    radLat2 = glat * PI / 180.0
    a = lat * PI / 180.0 - glat * PI / 180.0
    b = lng * PI / 180.0 - glng * PI / 180.0
    s = 2.0 * math.asin(math.sqrt(math.pow(math.sin(a/2),2) + math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(b/2),2)));
    s = s * EARTH_RADIUS;
    s = math.ceil(s * 10000) / 10000;
    return s



def getpdt(filename):
    pdt={}
    gpsfil=open(filename,'r')
    for line in gpsfil:
        tmp=line.strip('\n').split('\t')
        user=tmp[0]
        lng=float(tmp[2])
        lat=float(tmp[3])
        p=Point([lng,lat])
        if user not in pdt:
            pdt[user]=[p]
        else:
            pdt[user].append(p)
    return pdt

def initv(points):    
    global v
    v={}
    icoords=[]
    jcoords=[]
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            icoords=points[i].coords
            jcoords=points[j].coords
            if tuple(icoords) not in v:
                v[tuple(icoords)]={}
            if tuple(jcoords) not in v:
                v[tuple(jcoords)]={}    
            if tuple(jcoords)==tuple(icoords):
                continue
            dis=getDistancer(points[i],points[j])
            if (icoords[0]<jcoords[0] or (icoords[0]==jcoords[0] and icoords[1]<jcoords[1])):
                v[tuple(icoords)][tuple(jcoords)]=dis
            else:
                v[tuple(jcoords)][tuple(icoords)]=dis

def getscore(k,points):
    cutoff=0.0000001    
    clusters = kmeans(points, k, cutoff)
    inter=-1
    intra=0
    for i in range(k):
        for j in range(i+1,k):
            dis=getDistancek(clusters[i].centroid,clusters[j].centroid)
            if dis<inter or inter<0:
                inter=dis
        intra+=clusters[i].dissum
    if inter==0:
        inter=0.00000001
                                                                                                                                                     
    score=intra/len(points)/inter/inter
    return score, clusters

def count200():
    userfil=open('user_top200','r')
    for line in userfil:
        tmp=line.strip('\n').split('\t')
        userid=tmp[0]
        compid(userid)
  
   
    
def compid(userid):
    #userid='A000002CC29597'
    recordf=open('record','a')
    points, appdt=getfrof('gps_top200time',userid)
    print "appnum: "+str(len(appdt))    
    print "userid: "+userid    
    print "read points over"    
    recordf.write("start:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n')
    recordf.write("userid: "+userid+'\n'+"appNum: "+str(len(appdt))+'\n')
    recordf.close()
    if len(appdt)<10:
        clusterpoints(userid,points)

def getfrof(filename,userid):
    gpsfil=open(filename,'r')
    points=[]
    appdt={}
    for line in gpsfil:
        tmp=line.strip('\n').split('\t')
        if tmp[0]!=userid:#'358673013795895':#'a000004263b553':
            continue
        x=float(tmp[2])
        y=float(tmp[3])
        appkey=tmp[1]
        if appkey not in appdt:
            appdt[appkey]=0
        appdt[appkey]+=1
        #tm=tmp[6],time
        points.append(Point([x,y],appkey, tmp[6]))
    return points, appdt

def plottime(clusters):
    clo=['r','b','y','g','k']    
    wdt={5:1,6:1,12:1,13:1,19:1,20:1,26:1,27:1}
    appdt={}
    appindex=0
    for i,c in enumerate(clusters): 
        clen=len(clusters)                    
        timep=[0 for r in range(24)]        
        rtime=[]
        rweekend=[]
        rapp=[]                
        for po in c.points:
            day=int(po.nowtime[6:8])
            hour=int(po.nowtime[8:10])
            timep[hour]+=1    
            rtime.append(hour)             
            rweekend.append(day%7+1)
            appkey=po.appkey
            if appkey not in appdt:
                appdt[appkey]=appindex
                appindex+=1           
            rapp.append(appdt[appkey])
                        
        
        plt.figure(1)   
        plt.subplot(clen*100+10+i)      
        bins = range(0, 25) 
        plt.hist(rtime, bins,facecolor=clo[i],alpha=0.75)
        
       
        plt.figure(3)                
        plt.subplot(clen*100+10+i)  
        bins2 = range(1,9)
        plt.hist(rweekend, bins2,facecolor=clo[i],alpha=0.75)
        
        if appindex>10:
            continue
        plt.figure(4)                
        plt.subplot(clen*100+10+i)  
        bins3 = range(0,11)
        plt.hist(rapp, bins3,facecolor=clo[i],alpha=0.75)        
        
        
    
    
    
def clusterpoints(userid,points):
    clo=['r','b','y','g','k']
    #points=getfrof('20130102')
    initv(points)
    clusters=[]
    minscore=-1
    best=-1
    start= time.time()
    for k in range(2,6):
        score,tmpclusters=getscore(k,points)
        if minscore<0 or score<minscore:
            minscore=score
            clusters=tmpclusters
            best=k
    end= time.time()
    print "score: "+str(minscore)
   # print("end:"+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    #print "\nPOINTS:"
    #for p in points: print "P:", p
    recordf=open('record','a')
    
    plt.figure(3)        
    plt.figure(figsize=(8,6),dpi=120)
    
    plt.figure(1)
    plt.figure(figsize=(8,6),dpi=120)

    plt.figure(4)
    plt.figure(figsize=(8,6),dpi=120)    
    
    plottime(clusters)
    
    plt.figure(1)
    savefig("pic/"+userid+'h.jpg') 
    plt.clf()
    
    plt.figure(3)   
    savefig("pic/"+userid+'d.jpg') 
    
    plt.figure(4)   
    savefig("pic/"+userid+'a.jpg')
    
    plt.clf()
    
    plt.figure(2)
    backg=plt.imread("beijing.png")
    plt.figure(figsize=(8,6),dpi=120)
    im1=plt.imshow(backg,extent=[116.0,116.918,39.668,39.668+0.518*lnglatrate])
    plt.axis([116.0,116.918,39.668,39.668+0.518*lnglatrate])
    print "pointsNum:"+str(len(points))
    print "CLUSTERS:"
    recordf.write("pointsNum:"+str(len(points))+'\n'+"CLUSTERS:"+'\n')  
    for i,c in enumerate(clusters): 
        #print "C:", c
        plotpoint(c.points,clo[i])
        x=c.centroid.coords[0]
        y=(c.centroid.coords[1]-39.668)*lnglatrate+39.668
        print str(y)+','+str(x)+','+str(len(c.points))
        recordf.write(str(y)+','+str(x)+','+str(len(c.points))+'\n')
        #plt.text(0,.025,r'$\mu=100,\ \sigma=15$')
        plt.plot(x,y,clo[i]+'D')
        
    print "best K:"+str(best)  
    cost=end-start
    print "timecost:"+str(cost)+"s"+'\n'
    recordf.write("best K:"+str(best)+'\n'+"timecost:"+str(cost)+"s"+'\n'+'\n')
    recordf.close()
    savefig("pic/"+userid+'.jpg') 
    
    #plt.show()
    plt.clf()
    
if __name__ == "__main__": 
    count200() #compute the top 200 users
