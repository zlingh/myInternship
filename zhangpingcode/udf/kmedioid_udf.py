'''
Created on Mar 11, 2013

@author: zhangping
'''

from matplotlib.pyplot import plot,savefig  
import sys, math
import numpy as np 
import pylab as plt  
import time
def myrandom():
    a=time.time()
    a=a*100000
    a=a-int(a)    
    return a
class Point:
    def __init__(self, coords, reference=None):
        self.coords = coords
        self.n = len(coords)
        self.reference = reference
    def __repr__(self):
        return str(self.coords)

class Cluster:
    def __init__(self, points):
        if len(points) == 0: raise Exception("ILLEGAL: EMPTY CLUSTER")
        self.points = points
        self.n = points[0].n
        for p in points:
            if p.n != self.n: raise Exception("ILLEGAL: MULTISPACE CLUSTER")
        self.centroid = self.calculateCentroidmedoid()
    def __repr__(self):
        return str(self.points)
    
    def update(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroidmedoid()
        return getDistancek(old_centroid, self.centroid)
    
    def calculateCentroidmean(self):
        centroid_coords = []
        for i in range(self.n):
            centroid_coords.append(0.0)
            if len(self.points)==0:
                return self.centroid
            for p in self.points:
                centroid_coords[i] = centroid_coords[i]+p.coords[i]            
            centroid_coords[i] = centroid_coords[i]/len(self.points)
        return Point(centroid_coords)
    
    def calculateCentroidmedoid(self):
        if len(self.points)==0:
            return self.centroid, 0
        minp=0
        mindissum=-1        
        for i in range(len(self.points)):
            dissum=0.0
            for j in range(len(self.points)):
                if i!=j:
                    dis=getDistancek(self.points[i],self.points[j])
                    dissum+=dis
                else:
                    continue
            if mindissum>dissum or mindissum<0:
                mindissum=dissum
                minp=i         
        return self.points[minp]

def selectkcen(points, k):
    result=[]
    d=[0.0 for t in points]#record the distance of points to cluster
    first=points[int(myrandom()*len(points))]
    clusters=[]
    clusters.append(Cluster([first]))
    for i in range(k):
        sum=0
        for k,pk in enumerate(points):
            smdis=getDistancek(pk,clusters[0].centroid)
            for j in range(i):
                dis=getDistancek(pk,clusters[j+1].centroid)
                if dis<smdis:
                    smdis=dis              
            d[k]=smdis
            sum+=smdis
        sum*=myrandom()
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
            index = 0
            for i in range(len(clusters[1:])):
                distance = getDistancek(p, clusters[i+1].centroid)
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


def getDistancel(a, b):
    # Forbid measurements between Points in different spaces
    if a.n != b.n:
        raise Exception("ILLEGAL: NON-COMPARABLE POINTS")
    # Euclidean distance between a and b is sqrt(sum((a[i]-b[i])^2) for all i)
    ret = 0.0
    for i in range(a.n):
        ret = ret+pow((a.coords[i]-b.coords[i]), 2)
    return math.sqrt(ret)

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


def getfrof(filename):
    gpsfil=open(filename,'r')
    points=[]
    for line in gpsfil:
        tmp=line.strip('\n').split('\t')
        if tmp[0]!='863802013404426':
            continue
        lng=float(tmp[2])
        lat=float(tmp[3])
        points.append(Point([lng,lat]))
    return points
# main 

def clustmain(gpspoints):
    # num_points,    n,    k,      cutoff,         lower,        upper 
    num_points, n, k, cutoff, lower, upper = 100, 2, 3, 0.005, -200, 200
    clo=['r','b','y','g','r']
    outcen=[]
    points=[]
    for p in gpspoints:
        points.append(Point([p[0],p[1]]))
    clusters = kmeans(points, k, cutoff)   
    for i,c in enumerate(clusters): 
        x=c.centroid.coords[0]
        y=c.centroid.coords[1]
        outcen.append([x,y])
    return outcen
def plotpoint(points,clo):
    x=[p.coords[0] for p in points]
    y=[p.coords[1] for p in points]
    plt.plot(x,y,'.'+clo)

def main():
    # num_points,    n,    k,      cutoff,         lower,        upper 
    num_points, n, k, cutoff, lower, upper = 100, 2, 3, 0.005, -200, 200
    clo=['r','b','y','g','r']
    outcen=[]
    points=getfrof('20130102-1')
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
                #v[tuple(jcoords)][tuple(icoords)]=0.0  
                continue
            dis=getDistancer(points[i],points[j])
            if (icoords[0]<jcoords[0] or (icoords[0]==jcoords[0] and icoords[1]<jcoords[1])):
                v[tuple(icoords)][tuple(jcoords)]=dis
            else:
                v[tuple(jcoords)][tuple(icoords)]=dis            


    clusters = kmeans(points, k, cutoff)   
    for i,c in enumerate(clusters): 
        print "C:", c
        plotpoint(c.points,clo[i])
        x=c.centroid.coords[0]
        y=c.centroid.coords[1]
        print x,y
        plt.plot(x,y,clo[i]+'D')
    savefig('868943000240236.jpg') 
    plt.show()

def clust(bag):
    outBag = []
    gpspoints=[]
    for word in bag:
        lng=word[2]
        lat=word[3]
        gpspoints.append([lng,lat])
    outcen=clustmain(gpspoints)
    for c in outcen:
        tup=(bag[0][0], c[0], c[1])
        outBag.append(tup)
    return outBag

def clust1(bag):
    outBag = []
    tup=(bag[0][0], len(bag))
    outBag.append(tup)
    return outBag

if __name__ == "__main__": main()
