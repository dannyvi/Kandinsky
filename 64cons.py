#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-

#from view import moView
import numpy as np
from colorconvertc import jch2rgb

def constructMagie(n,step):
    num = n**step
    color_index = [202.5, 247.5, 292.5, 337.5, 22.5, 67.5, 112.5, 157.5]
    #color_index = [202.5, 22.5, 292.5, 157.5, 247.5, 67.5, 112.5, 337.5]
    j_array = np.linspace(0,100,num)
    def convertHue(index):
        c = color_index[index%n] + (index//n)  * (360.0/num)
        d = CoerceNum(c,0,0,360)
        #print(d)
        return d
    ufunc_h = np.frompyfunc(convertHue,1,1)
    h_array = ufunc_h(np.arange(0,64))

    def maxChromebyJH(j,h):
        c = 0.0
        while True:
            R,G,B = jch2rgb([j,c,h])
            if R>255 or G>255 or B>255 or R<0 or G<0 or B<0 or j==0 or j==100:
                break
            c += 1.0
            #print(j,c,h,R,G,B)
        return c
    ufunc_c = np.frompyfunc(maxChromebyJH,2,1)
    c_array = ufunc_c(j_array,h_array)

    scale_array = np.ones(num)  + (np.arange(64)%8)/2

    return np.array([h_array,j_array,c_array,scale_array]).T



def CoerceNum(var,num,lower,higher):
    var+=num
    while var<lower or var>=higher:
        if var<lower:
            var+=higher-lower
        elif var>=higher:
            var-=higher-lower
    return var

if __name__=="__main__":
    from PyQt5 import QtCore,QtWidgets,QtOpenGL
    from view import moView
    from npcolorconvert import npjch2rgb
    from basefunctionalpart import *
    import sys

    app=QtWidgets.QApplication(sys.argv)
    v=moView()

    s = constructMagie(8,2).astype('float')

    H = s[:,0]
    J = s[:,1]
    C = s[:,2]
    S = s[:,3]

    #print(H,J,C,S)
    colorrgbnum = npjch2rgb(np.array([J,C,H]).T)
    R = colorrgbnum[:,0]
    G = colorrgbnum[:,1]
    B = colorrgbnum[:,2]

    child = moColorListPiece(color=colorrgbnum,hjcs=np.array([H,J,C,S]).T)
    v.scene().coloreditpanel.colorlists.addChild(child)

    v.show()

    sys.exit(app.exec_())
    #s = constructMagie(64)#.astype('int')
    #print(s)
