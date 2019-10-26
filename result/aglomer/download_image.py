from sklearn.cluster import AgglomerativeClustering as AC
#from collections import Counter
#from matplotlib import pyplot as plt
import math, os, hashlib
import numpy as np
import urllib.request as req

f = open("file_new.txt", 'r')
StrF = f.read()
f.close()
ListF = StrF.split()
ListKey = ListF[0::8]
ListKey = [x[10:] for x in ListKey]
ListKey = ["https://chimera.biomed.kiev.ua/video/pendel-3d/tst.php?res=" + x.split('/')[0] + "#" + x + '/' for x in ListKey]
del ListF[0::8]
ListF = [float(x) for x in ListF]
a = 0
b = 7
ListVal = []
while b <= len(ListF):
    ListVal.append(ListF[a:b])
    a = b
    b = b + 7

# Del NaN and 1
ListKey = [y for x,y in zip(ListVal, ListKey) if not (math.isnan(x[0]) or (x[0] == 1 and x[1] == 1))]
ListVal = [x for x in ListVal if not (math.isnan(x[0]) or (x[0] == 1 and x[1] == 1))]

DictF = {x: y for x, y in zip(ListKey, ListVal)}

print(len(ListKey))
for url in ListKey:
    temp = url.split('tst.php?res=')
    if not os.path.isfile('/media/roman/10A2FE37A2FE20C0/Clustering2/' + hashlib.sha1(url.encode()).hexdigest() + '.png'):
        try:
            req.urlretrieve(temp[0] + temp[1][temp[1].index('#')+1:]  + 'screenshot1.png', '/media/roman/10A2FE37A2FE20C0/Clustering2/' + hashlib.sha1(url.encode()).hexdigest() + '.png')
        except:
            open('/media/roman/10A2FE37A2FE20C0/Clustering2/' + hashlib.sha1(url.encode()).hexdigest() + '.txt','a').close()
