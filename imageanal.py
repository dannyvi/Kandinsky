#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-

import numpy as np
from npcolorconvert import nprgb2jch
import PIL.Image as Image

def imageAnalyze(filename):
    f = Image.open(filename)
    widthf,heightf = f.size
    bignum= max(widthf,heightf)
    if (bignum>800):
        propotion = bignum/800.0
        if bignum==widthf:
            widthf = 800
            heightf = int(heightf/propotion)
        else:
            widthf = int(widthf/propotion)
            heightf = 800
        f = f.resize((widthf,heightf))

    data = np.array(f).reshape(-1,3)

    jch = nprgb2jch(data)

    j = jch[:,0]
    c = jch[:,1]
    h = jch[:,2]
    jsorted = (j/5).astype('int')
    csorted = (c/5).astype('int')
    hsorted = (h/9).astype('int')

    jchpack = (hsorted)*10000+(jsorted)*100+(csorted)
    jchpacksort = np.sort(jchpack)
    jchelement = np.unique(jchpacksort)

    jchhistobin = np.insert(jchelement,jchelement.size,1000001)

    jchstatistic = np.histogram(jchpacksort,jchhistobin)[0]

    H = (jchelement/10000).copy()
    J = ((jchelement/100)%100).copy()
    C = (jchelement%100).copy()

    scaler = f.size[0]*f.size[1]/40000.0
    if scaler<0: scaler=0.1
    jchstatistic = np.sqrt(jchstatistic/scaler).astype(int)
    scaler = jchstatistic.max()/10.0
    print(scaler)
    jchstatistic = jchstatistic / scaler
    result1 = np.array([H,J,C,jchstatistic]).T
    result = np.array(list(filter(lambda x:x[3]>1,result1)))
    return result

if __name__=='__main__':
    #s = imageAnalyze('/home/danlit/pic/picss/matisse.jpg')
    #np.set_printoptions(threshold='nan')

    #print s
    pass
