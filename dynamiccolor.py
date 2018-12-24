#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-
from PyQt5 import QtCore, QtGui
from functools import reduce

class dynamicColor(object):
    colorModeLighterBG,colorModeDarkerBG = range(2)
    def __init__(self,*arg):
        super(dynamicColor,self).__init__()
        self.basecolor=[0,0,0,0]
        self.increasecolor=30
        self.panel=[QtGui.QPen(QtGui.QColor(0,0,0,0)),QtGui.QBrush(QtGui.QColor(0,0,0,0))]
        self.panel[0].setWidth(1)
        self.icon={'enabled': [QtGui.QColor(),QtGui.QColor(),\
                               QtGui.QColor(),QtGui.QColor()],\
                   'undermouse': [QtGui.QColor(),QtGui.QColor(),\
                                  QtGui.QColor(),QtGui.QColor()],\
                   'disabled':[QtGui.QColor(),QtGui.QColor(),\
                               QtGui.QColor(),QtGui.QColor()]}
                         # bg              fgback         fgfront     selecting
        self.labeltext=QtGui.QColor()
        self.containerborder=QtGui.QPen(QtGui.QColor(0,0,0,0))
        self.containerborder.setWidthF(1)
        self.inputarea={'hasfocus':[QtGui.QPen(QtGui.QColor(0,0,0,0)),\
                                    QtGui.QBrush(QtGui.QColor(0,0,0,0)),\
                              QtGui.QBrush(QtGui.QColor(0,0,0,0)),\
                                    QtGui.QPen(QtGui.QColor(0,0,0,0))],\
                        'nofocus':[QtGui.QPen(QtGui.QColor(0,0,0,0)),\
                                   QtGui.QBrush(QtGui.QColor(0,0,0,0)),\
                               QtGui.QBrush(QtGui.QColor(0,0,0,0)),\
                                   QtGui.QPen(QtGui.QColor(0,0,0,0))]}
                    #frameborder     framebg        txt              outline
        self.inputarea['hasfocus'][0].setWidth(1)
        self.inputarea['hasfocus'][3].setWidth(30)
        self.inputarea['nofocus'][0].setWidth(1)
        self.inputarea['nofocus'][3].setWidth(30)
        self.resetColor(arg)
    def __del__(self):
        del self.basecolor
        del self.panel
        del self.icon
        del self.labeltext
        del self.inputarea
    def getBaseColor(self):
        return self.basecolor
    def getBaseColorF(self):
        return [self.basecolor[0]/255.0,self.basecolor[1]/255.0,\
                self.basecolor[2]/255.0,self.basecolor[3]/255.0]

    def resetColor(self,*args):
        arg = list(args)
        def needtochangecolor(a,b):
            if (int(a) & 0x80) ^ (int(b) & 0x80):
                return True
            else:
                return False
        def refreshColors(mode):
            if mode==dynamicColor.colorModeLighterBG:
                self.panel[0].setColor(QtGui.QColor(20,20,20,20))
                self.panel[1].setColor(QtGui.QColor(0,0,0,17))
                self.increasecolor=-30

                self.icon['enabled'][0].setRgb(25,25,25,43)
                self.icon['enabled'][1].setRgb(37,37,37,97)
                self.icon['enabled'][2].setRgb(210,210,210,5)
                self.icon['enabled'][3].setRgb(24,24,24,37)
                self.icon['undermouse'][0].setRgb(20,20,20,100)
                self.icon['undermouse'][1].setRgb(37,37,37,97)
                self.icon['undermouse'][2].setRgb(255,255,255,80)
                self.icon['undermouse'][3].setRgb(24,24,24,37)
                self.icon['disabled'][0].setRgb(128,128,128,0)
                self.icon['disabled'][1].setRgb(20,20,20,30)
                self.icon['disabled'][2].setRgb(93,93,93,30)
                self.icon['disabled'][3].setRgb(24,24,24,0)
                         # bg              fgback         fgfront     selecting
                self.labeltext=QtGui.QColor(60,60,60,156)
                self.containerborder.setColor(QtGui.QColor(20,20,20,16))
                self.inputarea['hasfocus'][0].setColor(QtGui.QColor(97,97,97,60))
                self.inputarea['hasfocus'][1].setColor(QtGui.QColor(255,255,255,128))
                self.inputarea['hasfocus'][2].setColor(QtGui.QColor(37,37,37,156))
                self.inputarea['hasfocus'][3].setColor(QtGui.QColor(195,195,195,156))
                self.inputarea['nofocus'][0].setColor(QtGui.QColor(97,97,97,37))
                self.inputarea['nofocus'][1].setColor(QtGui.QColor(255,255,255,30))
                self.inputarea['nofocus'][2].setColor(QtGui.QColor(37,37,37,128))
                self.inputarea['nofocus'][3].setColor(QtGui.QColor(195,195,195,0))
            else:
                self.panel[0].setColor(QtGui.QColor(195,195,195,60))
                self.panel[1].setColor(QtGui.QColor(158,158,158,60))
                self.increasecolor=30

                self.icon['enabled'][0].setRgb(255,255,255,37)
                self.icon['enabled'][1].setRgb(210,210,210,97)
                self.icon['enabled'][2].setRgb(218,218,218,97)
                self.icon['enabled'][3].setRgb(233,233,233,156)
                self.icon['undermouse'][0].setRgb(255,255,255,90)
                self.icon['undermouse'][1].setRgb(210,210,210,97)
                self.icon['undermouse'][2].setRgb(226,226,226,97)
                self.icon['undermouse'][3].setRgb(233,233,233,60)
                self.icon['disabled'][0].setRgb(128,128,128,0)
                self.icon['disabled'][1].setRgb(162,162,162,20)
                self.icon['disabled'][2].setRgb(167,167,167,60)
                self.icon['disabled'][3].setRgb(233,233,233,156)

                self.labeltext=QtGui.QColor(195,195,195,156)
                self.containerborder.setColor(QtGui.QColor(220,220,220,30))
                self.inputarea['hasfocus'][0].setColor(QtGui.QColor(158,158,158,60))
                self.inputarea['hasfocus'][1].setColor(QtGui.QColor(99,99,99,60))
                self.inputarea['hasfocus'][2].setColor(QtGui.QColor(255,255,255,156))
                self.inputarea['hasfocus'][3].setColor(QtGui.QColor(60,60,60,156))
                self.inputarea['nofocus'][0].setColor(QtGui.QColor(158,158,158,37))
                self.inputarea['nofocus'][1].setColor(QtGui.QColor(99,99,99,24))
                self.inputarea['nofocus'][2].setColor(QtGui.QColor(255,255,255,128))
                self.inputarea['nofocus'][3].setColor(QtGui.QColor(195,195,195,0))
                    #frameborder     framebg        txt              outline

        beforecolor=self.basecolor
        #print('refreshing')
        #try:
        if len(arg)==1 and type(arg[0])==list:
            arg = arg[0]
            #print(arg)
        #if True:
        try:
            if len(arg)==0:
                self.basecolor=[128,128,128,255]
            if len(arg)==1 and type(arg[0])==QtGui.QColor:
                a=arg[0].rgba()
                self.basecolor=[(a&0xff0000)>>16,\
                                (a&0xff00)>>8,\
                                (a&0xff),(a&0xff000000)>>24]
            elif len(arg)==1 and type(arg[0])==int:
                if arg[0]<0:
                    arg[0]=0
                if arg[0]>255:
                    arg[0]=255
                self.basecolor=[arg[0],arg[0],arg[0],255]
            elif len(arg)==1 and type(arg[0])==float:
                if arg[0]<0:
                    arg[0]=0
                if arg[0]>1:
                    arg[0]=1
                a=int(arg[0]*255)
                self.basecolor=[a,a,a,255]
            elif len(arg)==3 \
                 and reduce(lambda x,y:x or y,[type(i)==float for i in arg]):
                #print('float',arg)
                for i in range(len(arg)):
                    if arg[i]>1:
                        arg[i]=1
                    if arg[i]<0:
                        arg[i]=0
                    arg[i]=int(arg[i]*255)
                self.basecolor=[arg[0],arg[1],arg[2],255]
            elif len(arg)==3 \
                 and reduce(lambda x,y:x and y,[type(i)==int for i in arg]):
                for i in range(len(arg)):
                    if arg[i]>255:
                        arg[i]=255
                    if arg[i]<0:
                        arg[i]=0
                self.basecolor=[arg[0],arg[1],arg[2],255]
            elif len(arg)==4 \
                 and reduce(lambda x,y:x or y,[type(i)==float for i in arg]):
                for i in range(len(arg)):
                    if arg[i]>1:
                        arg[i]=1
                    if arg[i]<0:
                        arg[i]=0
                    arg[i]=int(arg[i]*255)
                self.basecolor=[arg[0],arg[1],arg[2],arg[3]]
            elif len(arg)==4 \
                 and reduce(lambda x,y:x and y,[type(i)==int for i in arg]):
                for i in range(len(arg)):
                    if arg[i]>255:
                        arg[i]=255
                    if arg[i]<0:
                        arg[i]=0
                self.basecolor=[arg[0],arg[1],arg[2],arg[3]]
            else:
                self.basecolor=[128,128,128,256]
        except:
            print('exception')
            self.basecolor=[128,128,128,256]
        before=(beforecolor[0]+beforecolor[1]+beforecolor[2])//3
        now=(self.basecolor[0]+self.basecolor[1]+self.basecolor[2])//3
        if needtochangecolor(before,now):
            if now&0x80:
                refreshColors(dynamicColor.colorModeLighterBG)
            else:
                refreshColors(dynamicColor.colorModeDarkerBG)
        #print('finished',)
        #print(self.basecolor)
moColor=dynamicColor()

def panelGetBorder():
    return moColor.panel[0]

def panelGetColor():
    return moColor.panel[1]

def iconGetBg(state):
    return moColor.icon[state][0]

def iconGetFgBase(state):
    return moColor.icon[state][1]

def iconGetFgFront(state):
    return moColor.icon[state][2]

def iconGetSelect(state):
    return moColor.icon[state][3]

def containerBorderGetColor():
    return moColor.containerborder

def labelGetColor():
    return moColor.labeltext

def inputGetFrameBorder(state):
    return moColor.inputarea[state][0]

def inputGetFrameBg(state):
    return moColor.inputarea[state][1]

def inputGetTextColor(state):
    return moColor.inputarea[state][2]

def inputGetTextOutline(state):
    return moColor.inputarea[state][3]
                #frameborder     framebg        txt              outline
def getIncreaseColor():
    return moColor.increasecolor

if __name__=="__main__":
    #a=dynamicColor()
    print("basecolor:",)
    print(moColor.basecolor)
    print("panel:",)
    print(hex(moColor.panel[0].color().rgba()))
    print(hex(moColor.panel[1].color().rgba()))
    print('icon:',)
    for i in moColor.icon:
        for j in moColor.icon[i]:
            print(hex(j.rgba()))
    print('labeltext:',)
    print(hex(moColor.labeltext.rgba()))
    print('inputarea:',)
    for i in moColor.inputarea:
        for j in moColor.inputarea[i]:
            print(hex(j.color().rgba()))
