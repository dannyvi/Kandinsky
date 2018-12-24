#!/usr/local/bin/python3.4
#-*- coding:utf-8 -*-
import icons
from basefunctionalpart import *
from frame import *

from colorconvertc import jch2rgb,rgb2jch

class moColorM(object):
    def __init__(self,red=0,green=0,blue=0):
        super(moColorM,self).__init__()
        self._r=0
        self._g=0
        self._b=0
        self._j=0
        self._c=0
        self._h=0

    def _setRGB(self,r,g,b):
        self._r = r
        self._g = g
        self._b = b
        if self._r>255:
            self._r = 255
        elif self._r < 0:
            self._r = 0
        elif self._g > 255:
            self._g = 255
        elif self._g < 0:
            self._g = 0
        elif self._b > 255:
            self._b = 255
        elif self._b < 0:
            self._b = 0
        self._j,self._c,self._h =map(lambda x:int(x),\
                                     rgb2jch([self._r,self._g,self._b]))

    def _setJCH(self,j,c,h):
        self._j = j
        self._c = c
        self._h = h

        self._r,self._g,self._b=map(lambda x:int(x),\
                                    jch2rgb([self._j,self._c,self._h]))
        while(self._r<0 or self._r>255 or\
              self._g<0 or self._g>255 or\
              self._b<0 or self._b>255):
            if self._c>0:
                self._c-=1
            elif self._c<1:
                self._c +=1
            else:
                break
            self._r,self._g,self._b=map(lambda x:int(x),\
                                        jch2rgb([self._j,self._c,self._h]))
            #        print self._r,self._g,self._b

    def modifyColor(self,name,value):
        if name == "R":
            self._setRGB(value[0],self._g,self._b)
        elif name == "G":
            self._setRGB(self._r,value[0],self._b)
        elif name == "B":
            self._setRGB(self._r,self._g,value[0])
        elif name == "RGB":
            self._setRGB(value[0],value[1],value[2])
        elif name == "J":
            self._setJCH(value[0],self._c,self._h)
        elif name == "C":
            self._setJCH(self._j,value[0],self._h)
        elif name == "H":
            self._setJCH(self._j,self._c,value[0])
        elif name == "JCH":
            self._setJCH(value[0],value[1],value[2])
        return [self._r,self._g,self._b,self._j,self._c,self._h]

    def getColorValue(self):
        return [self._r,self._g,self._b,self._j,self._c,self._h]


class moColorInfoPanel(QtWidgets.QGraphicsObject):
    Broadcast = QtCore.pyqtSignal(list)
    def __init__(self,parent=None):
        super(moColorInfoPanel,self).__init__(parent)
        #        self.setFlag(QtWidgets.QGraphicsItem.ItemIsPanel)
        self.colorcase = moColorM()
        self.colorframe=moColorFrame(self)
        self.__hcontrol=moInputFrame(self,30,3,u'色相:',30,20,moInputFrame.H)
        self.__jcontrol=moInputFrame(self,30,3,u'明度:',30,20,moInputFrame.J)
        self.__ccontrol=moInputFrame(self,30,3,u'彩度:',30,20,moInputFrame.C)
        self.__rcontrol=moInputFrame(self,30,3,'R:',12,20,moInputFrame.R)
        self.__gcontrol=moInputFrame(self,30,3,'G:',12,20,moInputFrame.G)
        self.__bcontrol=moInputFrame(self,30,3,'B:',12,20,moInputFrame.B)

        self.infolist = [self.colorframe,self.__hcontrol,self.__jcontrol,self.__ccontrol,\
                         self.__rcontrol,self.__gcontrol,self.__bcontrol]
        self.infoobj = []
        self.__hcontrol.setZValue(self.zValue()+2)
        self.__jcontrol.setZValue(self.zValue()+2)
        self.__ccontrol.setZValue(self.zValue()+2)
        self.__rcontrol.setZValue(self.zValue()+2)
        self.__gcontrol.setZValue(self.zValue()+2)
        self.__bcontrol.setZValue(self.zValue()+2)

        self.colorframe.setPos(4,4)
        self.__hcontrol.setPos(98,1)
        self.__jcontrol.setPos(98,21)
        self.__ccontrol.setPos(98,41)
        self.__rcontrol.setPos(4,63)
        self.__gcontrol.setPos(60,63)
        self.__bcontrol.setPos(116,63)

#        self.colorframe._dockright.DockValue.connect(self.__jcontrol.setValue)
#        self.colorframe._docktop.DockValue.connect(self.__hcontrol.setValue)
#        self.colorframe._dockbottom.DockValue.connect(self.__ccontrol.setValue)

#        self.__rcontrol.InputSender.connect(self.colorframe.setR)
#        self.__gcontrol.InputSender.connect(self.colorframe.setG)
#        self.__bcontrol.InputSender.connect(self.colorframe.setB)
#        self.__jcontrol.InputSender.connect(self.colorframe.setJ)
#        self.__ccontrol.InputSender.connect(self.colorframe.setC)
#        self.__hcontrol.InputSender.connect(self.colorframe.setH)

        self.__rcontrol.InputSender.connect(self.rInfo)
        self.__gcontrol.InputSender.connect(self.gInfo)
        self.__bcontrol.InputSender.connect(self.bInfo)
        self.__jcontrol.InputSender.connect(self.jInfo)
        self.__ccontrol.InputSender.connect(self.cInfo)
        self.__hcontrol.InputSender.connect(self.hInfo)

        self.__rcontrol._input.FocusOut.connect(self.__changeFocus)
        self.__gcontrol._input.FocusOut.connect(self.__changeFocus)
        self.__bcontrol._input.FocusOut.connect(self.__changeFocus)

        self.colorframe.ColorSender.connect(self.colorInfoCenter)
#        self.colorframe.ColorSender.connect(self.broadcastColor)
    @QtCore.pyqtSlot(int)
    def rInfo(self,r):
        if r>255:
            r=255
        if r<0:
            r=0
        self.colorInfoCenter(self.__rcontrol,"R",[r])

    @QtCore.pyqtSlot(int)
    def gInfo(self,r):
        if r>255:
            r=255
        if r<0:
            r=0
        self.colorInfoCenter(self.__gcontrol,"G",[r])

    @QtCore.pyqtSlot(int)
    def bInfo(self,r):
        if r>255:
            r=255
        if r<0:
            r=0
        self.colorInfoCenter(self.__bcontrol,"B",[r])

    @QtCore.pyqtSlot(int)
    def jInfo(self,r):
        if r>100:
            r=100
        if r<0:
            r=0
        self.colorInfoCenter(self.__jcontrol,"J",[r])

    @QtCore.pyqtSlot(int)
    def cInfo(self,r):
        self.colorInfoCenter(self.__ccontrol,"C",[r])

    @QtCore.pyqtSlot(int)
    def hInfo(self,r):
        if r>359:
            r=359
        if r<0:
            r=0
        self.colorInfoCenter(self.__hcontrol,"H",[r])

    def boundingRect(self):
        return QtCore.QRectF(0,0,135,90)

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        #painter.setPen(QtWidgets.QPen(panelGetBorder()))
        #painter.setBrush(QtWidgets.QBrush(panelGetColor()))
        #painter.drawRoundedRect(self.boundingRect(),4,4)
        pass
    @QtCore.pyqtSlot(object)
    def __changeFocus(self,source):
        #print 'received'
        def choose(a):
            if a == self.__rcontrol._input:
                return self.__gcontrol._input
            elif a == self.__gcontrol._input:
                return self.__bcontrol._input
            elif a == self.__bcontrol._input:
                return self.__rcontrol._input
        dest=choose(source)
        dest.setFocus()
        dest.setSelected(True)

    def getRGB(self):
        return self.colorcase.getColorValue()[0:3]

#    def setRGB(self,rgb):
#        self.colorframe.setRGB(rgb)

#    @QtCore.pyqtSlot(list)
#    def broadcastColor(self,color):
#        self.__hcontrol.setValue(color[5])
#        self.__jcontrol.setValue(color[3])
#        self.__ccontrol.setValue(color[4])
#        self.__rcontrol.setValue(color[0])
#        self.__gcontrol.setValue(color[1])
#        self.__bcontrol.setValue(color[2])

#        self.Broadcast.emit(color)
#        self.update()

    @QtCore.pyqtSlot(object,str,list)
    def colorInfoCenter(self,source,name,value):
        t = self.colorcase.modifyColor(name,value)
        for i in self.infolist+self.infoobj:
            if i is not source:
                i.responseInfo(t)
        self.Broadcast.emit(t)
        self.update()

#    def addInfoObj(self,source):
#        self.infolist.append(source)

#    def clearInfoObj(self):
#        self.infolist = []



#    def broadcastcolor(self,color):
#        self.Broadcast.emit([self.colorframe._r,self.colorframe._g,\
#                             self.colorframe._b])
class moModePanel(QtWidgets.QGraphicsObject):
    MainModeExchange=QtCore.pyqtSignal(str)
    Ovelall,Panel,Plate=['overall','panel','plate',]
    SubModeExchange=QtCore.pyqtSignal()
    def __init__(self,scene=None,size=24):
        super(moModePanel,self).__init__()
        self.mainmodeframe=moModeFrame(self,size)
        self.__submodeicon = icons.moIconSubModeSelectOn(self,size)
        self.__initBoundingRect()
        self.mainmodeframe.setPos(4,4)
        self.__submodeicon.setPos(8+\
                    self.mainmodeframe.boundingRect().size().width(),6)
        if scene:
            scene.addItem(self)

        self.mainmodeframe.ModeExchange.connect(self.modeFrameExchange)
        self.__submodeicon.Onclicked.connect(self.subModeIconExchange)
            #self.setPos(4,scene.sceneRect().size().height()-self.__height-4)

    @QtCore.pyqtSlot(str)
    def modeFrameExchange(self,infomation):
        #print 'i got main mode'
        self.MainModeExchange.emit(infomation)

    @QtCore.pyqtSlot(object,str)
    def subModeIconExchange(self,icon,infomation):
        #print 'i got submode'
        self.SubModeExchange.emit()

    def __initBoundingRect(self):
        size1=self.mainmodeframe.boundingRect().size()
        size2=self.__submodeicon.boundingRect().size()
        self.__width  = size1.width()+size2.width()+12
        self.__height = size1.height()+8

    def boundingRect(self):
        #if not self.scene():
        return QtCore.QRectF(0,0,self.__width,self.__height)
        #else:
        #    x,y,w,h = self.scene().sceneRect().getRect()
        #    return QtCore.QRectF(x,y-self.__height-4,self.__width,self.__height)

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        painter.setPen(panelGetBorder())
        #painter.setBrush(QtWidgets.QBrush(QtWidgets.QColor(20,20,20,30)))
        painter.setBrush(panelGetColor())
        painter.drawRoundedRect(self.boundingRect(),4,4)

class moSceneFuncPanel(QtWidgets.QGraphicsObject):
    MoreColor,LessColor,BgLighter,BgDarker,TurnLeft,TurnUp,TurnDown,\
    TurnRight,SwitchUp,SwitchDown,ScaleIncrease,ScaleDecrease,\
    ViewNear,ViewFar = range(14)
    def __init__(self,scene=None,size=24):
        super(moSceneFuncPanel,self).__init__()
        self.icons = [icons.moIconModuleColorIncrease(self,size),\
                      icons.moIconModuleColorDecrease(self,size),\
                      icons.moIconBgLighter(self,size),\
                      icons.moIconBgDarker(self,size),\
                      icons.moIconTurnLeft(self,size),\
                      icons.moIconTurnUp(self,size),\
                      icons.moIconTurnDown(self,size),\
                      icons.moIconTurnRight(self,size),\
                      icons.moIconSwitchUp(self,size),\
                      icons.moIconSwitchDown(self,size),\
                      icons.moIconScaleIncrease(self,size),\
                      icons.moIconScaleDecrease(self,size),\
                      icons.moIconViewNear(self,size),\
                      icons.moIconViewFar(self,size)]
        self.__initBoundingRect()
        for i in range(len(self.icons)):
            self.icons[i].setPos(i*(size+4)+4,6)
        if scene:
            scene.addItem(self)

    def __initBoundingRect(self):
        size = self.icons[0].boundingRect().size()
        self.__width = (size.width()+4)*len(self.icons) + 4
        self.__height = size.height()+12

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def boundingRect(self):
        return QtCore.QRectF(0,0,self.__width,self.__height)

    def paint(self,painter,option,widget):
        painter.setPen(panelGetBorder())
        #painter.setBrush(QtWidgets.QBrush(QtWidgets.QColor(20,20,20,30)))
        painter.setBrush(panelGetColor())
        painter.drawRoundedRect(self.boundingRect(),4,4)

class moFileManagerPanel(QtWidgets.QGraphicsObject):
    New,Open,Save,SaveAs,Import = range(5)
    def __init__(self,scene=None,size=24):
        super(moFileManagerPanel,self).__init__()
        self.icons = [icons.moIconNewFile(self,size),\
                      icons.moIconOpenFile(self,size),\
                      icons.moIconSaveFile(self,size),\
                      icons.moIconSaveFileAs(self,size),\
                      icons.moIconAnalPic(self,size)]
        self.__initBoundingRect()
        for i in range(len(self.icons)):
            self.icons[i].setPos(i*(size+4)+4,6)
        if scene:
            scene.addItem(self)

    def __initBoundingRect(self):
        size = self.icons[0].boundingRect().size()
        self.__width = (size.width()+4)*len(self.icons) + 4
        self.__height = size.height()+12

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def boundingRect(self):
        return QtCore.QRectF(0,0,self.__width,self.__height)

    def paint(self,painter,option,widget):
        painter.setPen(panelGetBorder())
        #painter.setBrush(QtWidgets.QBrush(QtWidgets.QColor(20,20,20,30)))
        painter.setBrush(panelGetColor())
        painter.drawRoundedRect(self.boundingRect(),4,4)

class moColorGroupEditPanel(moExtensibleDragFrame):
    def __init__(self,parent=None,scene=None,width=168,height=500):
        super(moColorGroupEditPanel,self).__init__(parent,scene,width,height)
        #self.setFlag(QtWidgets.QGraphicsItem.ItemIsPanel)
        self.colorinfo = moColorInfoPanel(self)
        self.colorcontainer = autoTransformFrame(self,bindtop=92,bindbottom=106)
        self.colorlists = moColorPieceGroupFrame(self.colorcontainer)
        self.listoperation  = moColorManagerListOp(self)
        self.listtransform = moColorManagerListTransform(self)
        self.listmove = moColorManagerListMove(self)

        #self.tsttadd = icons.moIconColorManagerAddColor(self)

        self.colorinfo.setPos(4,4)
        self.colorinfo.setZValue(self.zValue()+10)
        self.setPos(762,300)
        self.refreshPos()
        #if scene:
        #   scene.addItem(self)
        #self.setPos(scene.sceneRect().size().width()-self.boundingRect().size().width(),scene.sceneRect().size().height()-self.boundingRect().size().height())
        self.colorinfo.Broadcast.connect(self.colorlists.changeSelectionColor)
        self.listoperation.addcolor.Onclicked.connect(self.addSingleColor)
        self.listoperation.addlist.Onclicked.connect(self.addColorGroup)
        self.listoperation.removeitem.Onclicked.connect(self.removeColors)
        self.colorlists.SelectedColor.connect(self.colorinfo.colorInfoCenter)#setRGB)

        self.listtransform.scalesize.ScaleSize.connect(self.colorlists.setSelectionScale)
        self.listtransform.scalesize.scalesizeup.Onclicked.connect(self.colorlists.addSelectionScale)
        self.listtransform.scalesize.scalesizedown.Onclicked.connect(self.colorlists.subSelectionScale)
        self.listtransform.rotate.RotateValue.connect(self.colorlists.setSelectionRotate)
        self.listtransform.rotate.rotatecw.Onclicked.connect(self.colorlists.subSelectionRotate)
        self.listtransform.rotate.rotateccw.Onclicked.connect(self.colorlists.addSelectionRotate)
        self.listtransform.scalepos.ScaleValue.connect(self.colorlists.setSelectionPosScale)
        self.listtransform.scalepos.scaleposup.Onclicked.connect(self.colorlists.addSelectionPosScale)
        self.listtransform.scalepos.scaleposdown.Onclicked.connect(self.colorlists.subSelectionPosScale)

        self.listmove.movex.MoveValue.connect(self.colorlists.setSelectionMoveX)
        self.listmove.movex.movexadd.Onclicked.connect(self.colorlists.addSelectionMoveX)
        self.listmove.movex.movexsub.Onclicked.connect(self.colorlists.subSelectionMoveX)
        self.listmove.movey.MoveValue.connect(self.colorlists.setSelectionMoveY)
        self.listmove.movey.moveyadd.Onclicked.connect(self.colorlists.addSelectionMoveY)
        self.listmove.movey.moveysub.Onclicked.connect(self.colorlists.subSelectionMoveY)
        self.listmove.movez.MoveValue.connect(self.colorlists.setSelectionMoveZ)
        self.listmove.movez.movezadd.Onclicked.connect(self.colorlists.addSelectionMoveZ)
        self.listmove.movez.movezsub.Onclicked.connect(self.colorlists.subSelectionMoveZ)
#        self.installEventFilter(self.colorinfo)
#        self.installEventFilter(self.listoperation)
#        self.installEventFilter(self.listtransform)
#        self.installEventFilter(self.listmove)

    @QtCore.pyqtSlot(object,str)
    def addSingleColor(self,wrap,wrap2):
        #print 'ireceived add instruction'
        color=self.colorinfo.getRGB()
        a = moColorPiece(color=color)
        self.colorlists.addChild(a)
        #print self.colorlists
        self.update()

    def addColorGroup(self,wrap,wrap2):
        a = moColorGroupPiece()
        self.colorlists.addChild(a)

    def removeColors(self,wrap,wrap2):
        #print 'ireceived'
        for i in self.colorlists.selecteditem:
            self.colorlists.removeChild(i)

    def extendEvents(self,dpos,event):
        super(moColorGroupEditPanel,self).extendEvents(dpos,event)
        self.refreshPos()

    def refreshPos(self):
        self.listoperation.setPos(0,self.boundingRect().size().height()-106)
        self.listtransform.setPos(0,self.boundingRect().size().height()-78)
        self.listmove.setPos(0,self.boundingRect().size().height()-42)
        #self.tsttadd.setPos(140,self.boundingRect().size().height()-106)

#    def itemChange(self,change,value):
#        if change == self.ItemPositionChange and self.scene():
#            self.refreshPos()
#        return super(moColorGroupEditPanel,self).itemChange(change,value)
        #return arg

#    def mousePressEvent(self,event):
#        print 'panel received event',
#        print event.pos()
#        super(moColorGroupEditPanel,self).mousePressEvent(event)
#        self.update()

#    def mouseReleaseEvent(self,event):
#        super(moColorGroupEditPanel,self).mouseReleaseEvent(event)
        #event.accept()

class moPanelHelpInfo(QtWidgets.QGraphicsObject):
    def __init__(self,scene=None):
        super(moPanelHelpInfo,self).__init__()
        self._icon = icons.moIconHelpInfo(self)
        self.__label = ''
        if scene:
            scene.addItem(self)


    def boundingRect(self):
        return QtCore.QRectF(0,0,32,200)


    def paint(self,painter,option,widget):
        if self._icon.testSelected():
            pen=QtGui.QPen(labelGetColor())
            painter.setPen(pen)
            painter.setFont(QtGui.QFont("sansserif",12))
            painter.drawText(0,-44,400,32,\
                             QtCore.Qt.AlignBottom,self.__label)

    def assignText(self,text):
        self.__label = text

    def cancelText(self):
        self.__label = ''
