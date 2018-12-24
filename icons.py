#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-

from PyQt5 import QtCore,QtGui,QtWidgets
from dynamiccolor import *

class moBaseIcon(QtWidgets.QGraphicsObject):
    Type=QtWidgets.QGraphicsItem.UserType+100
    Enabled,Disabled,UnderMouse=['enabled','disabled','undermouse']
    SelectClick,SelectStay,SelectRotate = range(3)
    Onclicked = QtCore.pyqtSignal(QtWidgets.QGraphicsObject,str)
    Info = ''
    Tips =  ''
    def __init__(self,parent=None,size=24,selection=0):
        super(moBaseIcon,self).__init__(parent)
        self._allowselect=selection
        self._selecting=False

        self._size=size
        self._linkeditem=[]
        if self.parentItem():
            self.setZValue(self.parentItem().zValue()+2)
        self.setAcceptHoverEvents(True)

    def type(self):
        return moBaseIcon.Type

    def setSelecting(self,selection):
        self._selecting=selection

    def boundingRect(self):
        return QtCore.QRectF(0,0,self._size,self._size)

    def shape(self):
        path=QtGui.QPainterPath()
        path.addRect(0,0,self._size,self._size)
        return path

    def paint(self,painter,option,widget):
        painter.setPen(QtCore.Qt.NoPen)
        color=iconGetBg(self.findState())
        radial=QtGui.QRadialGradient(self._size/2,self._size/2,(self._size-4)/2)
        radial.setColorAt(0,color)
        radial.setColorAt(1,QtGui.QColor(0,0,0,0))
        brush=QtGui.QBrush(radial)
        painter.setBrush(brush)
        painter.drawEllipse(self.boundingRect())
        if self._selecting:
            br = iconGetSelect(self.findState())
            painter.setBrush(br)
            painter.drawRoundedRect(self.boundingRect(),1,1)

    def mousePressEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton:
            if self._allowselect == moBaseIcon.SelectRotate:
                self._selecting=not self._selecting
            elif self._allowselect == moBaseIcon.SelectStay:
                if self._selecting == True:
                    return
                else: self._selecting=True
            self.Onclicked.emit(self,self.Info)
            self.update()
            if self._linkeditem:
                for i in self._linkeditem:
                    try:
                        i.clearSelecting()
                    except AttributeError:
                        pass
            #print(self.Info,"icon pressed")                          ###########test
        super(moBaseIcon,self).mousePressEvent(event)

    def hoverEnterEvent(self,event):
        if self.scene() and self.Tips:
            try:
                self.scene().showTips(self.Tips)
            except:
                pass
        super(moBaseIcon,self).hoverEnterEvent(event)

    def hoverLeaveEvent(self,event):
        if self.scene() and self.Tips:
            try:
                self.scene().cancelTips()
            except:
                pass

    def findState(self):
        if self.isEnabled():
            if self.isUnderMouse():
                return moBaseIcon.UnderMouse
            else:
                return moBaseIcon.Enabled
        else:
            return moBaseIcon.Disabled

    def clearSelecting(self):
        self._selecting=False
        self.update()

    def testSelected(self):
        return self._selecting

class moABaseIcon(moBaseIcon):
    def __init__(self,parent=None,size=24,selection=moBaseIcon.SelectClick):
        super(moABaseIcon,self).__init__(parent,size,selection)
        self._path=QtGui.QPainterPath()
        self.mPath()

    def paint(self,painter,option,widget):
        state=self.findState()
        colorfgb=iconGetFgBase(state)
        colorfgf=iconGetFgFront(state)
        painter.setPen(QtCore.Qt.NoPen)
        radial=QtGui.QRadialGradient(self._size/2,self._size/2,(self._size-10)/2)
        radial.setColorAt(0,colorfgf)
        radial.setColorAt(1,colorfgb)
        brush=QtGui.QBrush(radial)
        painter.setBrush(brush)

        painter.drawPath(self._path)
        super(moABaseIcon,self).paint(painter,option,widget)

    def mPath(self):
        pass

class moIconModeOverall(moABaseIcon):
    Info ='overall'
    Tips = '显示色立体所有色块    X'
    def __init__(self,parent=None,size=24):
        super(moIconModeOverall,self).__init__(parent,size,selection=moBaseIcon.SelectStay)
    def mPath(self):
        unit=self._size/16.0
        self._path.addRoundedRect(6*unit,unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(6*unit,6*unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(6*unit,11*unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(unit,6*unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(11*unit,6*unit,4*unit,4*unit,int(unit),int(unit))


class moIconModePanel(moABaseIcon):
    Info  = 'panel'
    Tips = '显示同色相和互补色相  C'
    def __init__(self,parent=None,size=24):
        super(moIconModePanel,self).__init__(parent,size,selection=moBaseIcon.SelectStay)
    def mPath(self):
        unit=self._size/16.0
        self._path.addRoundedRect(6*unit,unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(6*unit,6*unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(6*unit,11*unit,4*unit,4*unit,int(unit),int(unit))


class moIconModePlate(moABaseIcon):
    Info = 'plate'
    Tips = '显示同一明度        V'
    def __init__(self,parent=None,size=24):
        super(moIconModePlate,self).__init__(parent,size,selection=moBaseIcon.SelectStay)
    def mPath(self):
        unit=self._size/16.0
        self._path.addRoundedRect(6*unit,6*unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(unit,6*unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(11*unit,6*unit,4*unit,4*unit,int(unit),int(unit))

    def getinfo(self):
        return 'plate'

class moIconSubModeSelectOn(moABaseIcon):
    Tips = '切换 ciecam02 / 孟塞尔 色立体'
    def __init__(self,parent=None,size=24):
        super(moIconSubModeSelectOn,self).__init__(parent,size,selection=moBaseIcon.SelectRotate)
        self._selecting=True
    def mPath(self):
        unit=self._size/16.0
        self._path.addRoundedRect(7*unit,2*unit,2*unit,2*unit,int(unit),int(unit))
        self._path.addRoundedRect(7*unit,7*unit,2*unit,2*unit,int(unit),int(unit))
        self._path.addRoundedRect(7*unit,12*unit,2*unit,2*unit,int(unit),int(unit))
        self._path.addRoundedRect(2*unit,7*unit,2*unit,2*unit,int(unit),int(unit))
        self._path.addRoundedRect(12*unit,7*unit,2*unit,2*unit,int(unit),int(unit))
        self._path.addRoundedRect(9*unit,3*unit,4*unit,4*unit,int(unit),int(unit))
        self._path.addRoundedRect(3*unit,9*unit,4*unit,4*unit,int(unit),int(unit))

class moIconModuleColorIncrease(moABaseIcon):
    Tips = '增加ciecam02色数量      d'
    def __init__(self,parent=None,size=24):
        super(moIconModuleColorIncrease,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        self._path.addEllipse(2*u,2*u,2*u,2*u)
        self._path.addEllipse(12*u,2*u,2*u,2*u)
        self._path.addEllipse(2*u,12*u,2*u,2*u)
        self._path.addEllipse(12*u,12*u,2*u,2*u)
        self._path.addEllipse(7*u,1*u,2*u,2*u)
        self._path.addEllipse(7*u,13*u,2*u,2*u)
        self._path.addEllipse(1*u,7*u,2*u,2*u)
        self._path.addEllipse(13*u,7*u,2*u,2*u)
        self._path.addEllipse(4*u,4*u,8*u,8*u)

class moIconModuleColorDecrease(moABaseIcon):
    Tips = '减少ciecam02色数量      s'
    def __init__(self,parent=None,size=24):
        super(moIconModuleColorDecrease,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        self._path.addEllipse(7*u,2*u,2*u,2*u)
        self._path.addEllipse(7*u,12*u,2*u,2*u)
        self._path.addEllipse(2*u,7*u,2*u,2*u)
        self._path.addEllipse(12*u,7*u,2*u,2*u)
        self._path.addEllipse(6*u,6*u,4*u,4*u)

class moIconBgLighter(moABaseIcon):
    Info = '20'
    Tips = '背景变亮              A'
    def __init__(self,parent=None,size=24):
        super(moIconBgLighter,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        unit=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(2*unit,4*unit)
        path.lineTo(2*unit,14*unit)
        path.lineTo(4*unit,14*unit)
        path.lineTo(4*unit,4*unit)
        path.lineTo(14*unit,4*unit)
        path.lineTo(14*unit,2*unit)
        path.lineTo(2*unit,2*unit)
        path.closeSubpath()
        self._path.addPath(path)

class moIconBgDarker(moABaseIcon):
    Info = '-20'
    Tips = '背景变暗              Z'
    def __init__(self,parent=None,size=24):
        super(moIconBgDarker,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        unit=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(14*unit,12*unit)
        path.lineTo(14*unit,2*unit)
        path.lineTo(12*unit,2*unit)
        path.lineTo(12*unit,12*unit)
        path.lineTo(2*unit,12*unit)
        path.lineTo(2*unit,14*unit)
        path.lineTo(14*unit,14*unit)
        path.closeSubpath()
        self._path.addPath(path)

class moIconTurnLeft(moABaseIcon):
    Info = '-10'
    Tips = '向左旋转             左箭头'
    def __init__(self,parent=None,size=24):
        super(moIconTurnLeft,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        unit=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(12*unit,6*unit)
        path.lineTo(6*unit,6*unit)
        path.lineTo(6*unit,4*unit)
        path.lineTo(2*unit,8*unit)
        path.lineTo(6*unit,12*unit)
        path.lineTo(6*unit,10*unit)
        path.lineTo(12*unit,10*unit)
        path.closeSubpath()
        self._path.addPath(path)

class moIconTurnRight(moABaseIcon):
    Info = '10'
    Tips = '向右旋转             右箭头'
    def __init__(self,parent=None,size=24):
        super(moIconTurnRight,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(4*u,6*u)
        path.lineTo(4*u,10*u)
        path.lineTo(10*u,10*u)
        path.lineTo(10*u,12*u)
        path.lineTo(14*u,8*u)
        path.lineTo(10*u,4*u)
        path.lineTo(10*u,6*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconTurnUp(moABaseIcon):
    Info = '10'
    Tips = '向上旋转             上箭头'
    def __init__(self,parent=None,size=24):
        super(moIconTurnUp,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(10*u,12*u)
        path.lineTo(10*u,6*u)
        path.lineTo(12*u,6*u)
        path.lineTo(8*u,2*u)
        path.lineTo(4*u,6*u)
        path.lineTo(6*u,6*u)
        path.lineTo(6*u,12*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconTurnDown(moABaseIcon):
    Info = '-10'
    Tips = '向下旋转             下箭头'
    def __init__(self,parent=None,size=24):
        super(moIconTurnDown,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(6*u,4*u)
        path.lineTo(6*u,10*u)
        path.lineTo(4*u,10*u)
        path.lineTo(8*u,14*u)
        path.lineTo(12*u,10*u)
        path.lineTo(10*u,10*u)
        path.lineTo(10*u,4*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconSwitchUp(moABaseIcon):
    Info = '1'
    Tips = '切换到上一色组              ;'
    def __init__(self,parent=None,size=24):
        super(moIconSwitchUp,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(2*u,9*u)
        path.lineTo(7*u,14*u)
        path.lineTo(9*u,12*u)
        path.lineTo(8*u,11*u)
        path.lineTo(11*u,8*u)
        path.lineTo(13*u,10*u)
        path.lineTo(13*u,3*u)
        path.lineTo(6*u,3*u)
        path.lineTo(8*u,5*u)
        path.lineTo(5*u,8*u)
        path.lineTo(4*u,7*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconSwitchDown(moABaseIcon):
    Info = '-1'
    Tips = '切换到下一色组             \''
    def __init__(self,parent=None,size=24):
        super(moIconSwitchDown,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(14*u,7*u)
        path.lineTo(9*u,2*u)
        path.lineTo(7*u,4*u)
        path.lineTo(8*u,5*u)
        path.lineTo(5*u,8*u)
        path.lineTo(3*u,6*u)
        path.lineTo(3*u,13*u)
        path.lineTo(10*u,13*u)
        path.lineTo(8*u,11*u)
        path.lineTo(11*u,8*u)
        path.lineTo(12*u,9*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconScaleIncrease(moABaseIcon):
    Info = '1'
    Tips = '增大色块                    .'
    def __init__(self,parent=None,size=24):
        super(moIconScaleIncrease,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(2*u,3*u)
        path.lineTo(2*u,7*u)
        path.lineTo(4*u,7*u)
        path.lineTo(4*u,12*u)
        path.lineTo(10*u,12*u)
        path.lineTo(12*u,10*u)
        path.lineTo(12*u,4*u)
        path.lineTo(7*u,4*u)
        path.lineTo(7*u,2*u)
        path.lineTo(3*u,2*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconScaleDecrease(moABaseIcon):
    Info = '-1'
    Tips = '减小色块                    ,'
    def __init__(self,parent=None,size=24):
        super(moIconScaleDecrease,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(2*u,4*u)
        path.lineTo(2*u,10*u)
        path.lineTo(7*u,10*u)
        path.lineTo(7*u,12*u)
        path.lineTo(11*u,12*u)
        path.lineTo(12*u,11*u)
        path.lineTo(12*u,7*u)
        path.lineTo(10*u,7*u)
        path.lineTo(10*u,2*u)
        path.lineTo(4*u,2*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconViewNear(moABaseIcon):
    Info = '-0.5'
    Tips = '放大场景                   ]'
    def __init__(self,parent=None,size=24):
        super(moIconViewNear,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(8*u,3*u)
        path.lineTo(6*u,5*u)
        path.lineTo(7*u,5*u)
        path.lineTo(7*u,7*u)
        path.lineTo(5*u,7*u)
        path.lineTo(5*u,6*u)
        path.lineTo(3*u,8*u)
        path.lineTo(5*u,10*u)
        path.lineTo(5*u,9*u)
        path.lineTo(7*u,9*u)
        path.lineTo(7*u,11*u)
        path.lineTo(6*u,11*u)
        path.lineTo(8*u,13*u)
        path.lineTo(10*u,11*u)
        path.lineTo(9*u,11*u)
        path.lineTo(9*u,9*u)
        path.lineTo(11*u,9*u)
        path.lineTo(11*u,10*u)
        path.lineTo(13*u,8*u)
        path.lineTo(11*u,6*u)
        path.lineTo(11*u,7*u)
        path.lineTo(9*u,7*u)
        path.lineTo(9*u,5*u)
        path.lineTo(10*u,5*u)
        path.closeSubpath()
        path.addRect(7*u,7*u,2*u,2*u)
        self._path.addPath(path)

class moIconViewFar(moABaseIcon):
    Info = '0.5'
    Tips = '缩小场景                   ['
    def __init__(self,parent=None,size=24):
        super(moIconViewFar,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(7*u,3*u)
        path.lineTo(7*u,5*u)
        path.lineTo(6*u,5*u)
        path.lineTo(8*u,7*u)
        path.lineTo(10*u,5*u)
        path.lineTo(9*u,5*u)
        path.lineTo(9*u,3*u)
        path.closeSubpath()

        path.moveTo(3*u,7*u)
        path.lineTo(3*u,9*u)
        path.lineTo(5*u,9*u)
        path.lineTo(5*u,10*u)
        path.lineTo(7*u,8*u)
        path.lineTo(5*u,6*u)
        path.lineTo(5*u,7*u)
        path.closeSubpath()

        path.moveTo(7*u,13*u)
        path.lineTo(9*u,13*u)
        path.lineTo(9*u,11*u)
        path.lineTo(10*u,11*u)
        path.lineTo(8*u,9*u)
        path.lineTo(6*u,11*u)
        path.lineTo(7*u,11*u)
        path.closeSubpath()

        path.moveTo(13*u,9*u)
        path.lineTo(13*u,7*u)
        path.lineTo(11*u,7*u)
        path.lineTo(11*u,6*u)
        path.lineTo(9*u,8*u)
        path.lineTo(11*u,10*u)
        path.lineTo(11*u,9*u)
        path.closeSubpath()

        self._path.addPath(path)
class moIconColorManagerAddColor(moABaseIcon):
    Tips = '添加选色'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerAddColor,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(2*u,6*u)
        path.lineTo(2*u,8*u)
        path.lineTo(4*u,8*u)
        path.lineTo(4*u,9*u)
        path.lineTo(6*u,7*u)
        path.lineTo(4*u,5*u)
        path.lineTo(4*u,6*u)
        path.closeSubpath()
        path.addRect(2*u,10*u,4*u,4*u)
        path.addRect(6*u,2*u,6*u,6*u)
        path2 = QtGui.QPainterPath()
        path2.addRect(8*u,4*u,6*u,6*u)
        path=path.united(path2)
        path.setFillRule(QtCore.Qt.WindingFill)
        self._path.addPath(path)

class moIconColorManagerAddColorGroup(moABaseIcon):
    Tips = '添加选色组'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerAddColorGroup,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(2*u,6*u)
        path.lineTo(2*u,8*u)
        path.lineTo(4*u,8*u)
        path.lineTo(4*u,9*u)
        path.lineTo(6*u,7*u)
        path.lineTo(4*u,5*u)
        path.lineTo(4*u,6*u)
        path.closeSubpath()
        path.addRect(2*u,12*u,2*u,2*u)
        path.addRect(5*u,12*u,2*u,2*u)
        path.addRect(8*u,12*u,2*u,2*u)
        path.addRect(6*u,2*u,6*u,6*u)
        path2 = QtGui.QPainterPath()
        path2.addRect(8*u,4*u,6*u,6*u)
        path=path.united(path2)
        path.setFillRule(QtCore.Qt.WindingFill)
        self._path.addPath(path)

class moIconColorManagerRemoveColor(moABaseIcon):
    Tips = '移除选色／选色组'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerRemoveColor,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(13*u,6*u)
        path.lineTo(11*u,6*u)
        path.lineTo(11*u,8*u)
        path.lineTo(10*u,8*u)
        path.lineTo(12*u,10*u)
        path.lineTo(14*u,8*u)
        path.lineTo(13*u,8*u)
        path.closeSubpath()
        path.addRect(4*u,2*u,6*u,6*u)
        path.addRect(10*u,10*u,4*u,4*u)
        path.addRect(7*u,12*u,2*u,2*u)
        path2 = QtGui.QPainterPath()
        path2.addRect(2*u,4*u,6*u,6*u)
        path=path.united(path2)
        path.setFillRule(QtCore.Qt.WindingFill)
        self._path.addPath(path)

class moIconColorManagerExplode(moABaseIcon):
    Tips = '未实现'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerExplode,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(4*u,4*u)
        path.lineTo(4*u,7*u)
        path.lineTo(5*u,6*u)
        path.lineTo(7*u,8*u)
        path.lineTo(5*u,10*u)
        path.lineTo(4*u,9*u)
        path.lineTo(4*u,12*u)
        path.lineTo(7*u,12*u)
        path.lineTo(6*u,11*u)
        path.lineTo(8*u,9*u)
        path.lineTo(10*u,11*u)
        path.lineTo(9*u,12*u)
        path.lineTo(12*u,12*u)
        path.lineTo(12*u,9*u)
        path.lineTo(11*u,10*u)
        path.lineTo(9*u,8*u)
        path.lineTo(11*u,6*u)
        path.lineTo(12*u,7*u)
        path.lineTo(12*u,4*u)
        path.lineTo(9*u,4*u)
        path.lineTo(10*u,5*u)
        path.lineTo(8*u,7*u)
        path.lineTo(6*u,5*u)
        path.lineTo(7*u,4*u)
        path.closeSubpath()
        path.addRect(2*u,2*u,2*u,2*u)
        path.addRect(12*u,2*u,2*u,2*u)
        path.addRect(2*u,12*u,2*u,2*u)
        path.addRect(12*u,12*u,2*u,2*u)
        self._path.addPath(path)

class moIconColorManagerReduce(moABaseIcon):
    Tips = '未实现'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerReduce,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(3*u,2*u)
        path.lineTo(2*u,3*u)
        path.lineTo(3*u,4*u)
        path.lineTo(2*u,5*u)
        path.lineTo(5*u,5*u)
        path.lineTo(5*u,2*u)
        path.lineTo(4*u,3*u)
        path.closeSubpath()

        path.moveTo(2*u,13*u)
        path.lineTo(3*u,14*u)
        path.lineTo(4*u,13*u)
        path.lineTo(5*u,14*u)
        path.lineTo(5*u,11*u)
        path.lineTo(2*u,11*u)
        path.lineTo(3*u,12*u)
        path.closeSubpath()

        path.moveTo(13*u,14*u)
        path.lineTo(14*u,13*u)
        path.lineTo(13*u,12*u)
        path.lineTo(14*u,11*u)
        path.lineTo(11*u,11*u)
        path.lineTo(11*u,14*u)
        path.lineTo(12*u,13*u)
        path.closeSubpath()

        path.moveTo(14*u,3*u)
        path.lineTo(13*u,2*u)
        path.lineTo(12*u,3*u)
        path.lineTo(11*u,2*u)
        path.lineTo(11*u,5*u)
        path.lineTo(14*u,5*u)
        path.lineTo(13*u,4*u)
        path.closeSubpath()

        path.addRect(5*u,5*u,2*u,2*u)
        path.addRect(9*u,5*u,2*u,2*u)
        path.addRect(5*u,9*u,2*u,2*u)
        path.addRect(9*u,9*u,2*u,2*u)
        self._path.addPath(path)

class moIconColorManagerCWRotate(moABaseIcon):
    Tips = '顺时针旋转 选色／选色组'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerCWRotate,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(8*u,6*u)
        path.lineTo(8*u,8*u)
        path.lineTo(10*u,5*u)
        path.lineTo(8*u,2*u)
        path.lineTo(8*u,4*u)
        path.arcTo(4*u,4*u,8*u,8*u,90,180)
        path.lineTo(8*u,10*u)
        path.arcTo(6*u,6*u,4*u,4*u,270,-180)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerCWRotate,self).paint(painter,option,widget)

class moIconColorManagerCCWRotate(moABaseIcon):
    Tips = '逆时针旋转  选色／选色组'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerCCWRotate,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(8*u,4*u)
        path.lineTo(8*u,2*u)
        path.lineTo(6*u,5*u)
        path.lineTo(8*u,8*u)
        path.lineTo(8*u,6*u)
        path.arcTo(6*u,6*u,4*u,4*u,90,-180)
        path.lineTo(8*u,10*u)
        path.arcTo(4*u,4*u,8*u,8*u,270,180)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerCCWRotate,self).paint(painter,option,widget)

class moIconColorManagerScaleUpPos(moABaseIcon):
    Tips = '远离中心'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerScaleUpPos,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(8*u,3*u)
        path.lineTo(6*u,5*u)
        path.lineTo(7*u,5*u)
        path.lineTo(7*u,7*u)
        path.lineTo(5*u,7*u)
        path.lineTo(5*u,6*u)
        path.lineTo(3*u,8*u)
        path.lineTo(5*u,10*u)
        path.lineTo(5*u,9*u)
        path.lineTo(7*u,9*u)
        path.lineTo(7*u,11*u)
        path.lineTo(6*u,11*u)
        path.lineTo(8*u,13*u)
        path.lineTo(10*u,11*u)
        path.lineTo(9*u,11*u)
        path.lineTo(9*u,9*u)
        path.lineTo(11*u,9*u)
        path.lineTo(11*u,10*u)
        path.lineTo(13*u,8*u)
        path.lineTo(11*u,6*u)
        path.lineTo(11*u,7*u)
        path.lineTo(9*u,7*u)
        path.lineTo(9*u,5*u)
        path.lineTo(10*u,5*u)
        path.closeSubpath()
        path.addRect(7*u,7*u,2*u,2*u)
        self._path.addPath(path)

class moIconColorManagerScaleDownPos(moABaseIcon):
    Tips = '趋近中心'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerScaleDownPos,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(7*u,3*u)
        path.lineTo(7*u,5*u)
        path.lineTo(6*u,5*u)
        path.lineTo(8*u,7*u)
        path.lineTo(10*u,5*u)
        path.lineTo(9*u,5*u)
        path.lineTo(9*u,3*u)
        path.closeSubpath()

        path.moveTo(3*u,7*u)
        path.lineTo(3*u,9*u)
        path.lineTo(5*u,9*u)
        path.lineTo(5*u,10*u)
        path.lineTo(7*u,8*u)
        path.lineTo(5*u,6*u)
        path.lineTo(5*u,7*u)
        path.closeSubpath()

        path.moveTo(7*u,13*u)
        path.lineTo(9*u,13*u)
        path.lineTo(9*u,11*u)
        path.lineTo(10*u,11*u)
        path.lineTo(8*u,9*u)
        path.lineTo(6*u,11*u)
        path.lineTo(7*u,11*u)
        path.closeSubpath()

        path.moveTo(13*u,9*u)
        path.lineTo(13*u,7*u)
        path.lineTo(11*u,7*u)
        path.lineTo(11*u,6*u)
        path.lineTo(9*u,8*u)
        path.lineTo(11*u,10*u)
        path.lineTo(11*u,9*u)
        path.closeSubpath()

        self._path.addPath(path)

class moIconColorManagerScaleUpSize(moABaseIcon):
    Tips = '放大 选色／选色组      L'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerScaleUpSize,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.addEllipse(2*u,10*u,4*u,4*u)
        path.addEllipse(6*u,2*u,8*u,8*u)

        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerScaleUpSize,self).paint(painter,option,widget)

class moIconColorManagerScaleDownSize(moABaseIcon):
    Tips = '缩小 选色／选色组      K'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerScaleDownSize,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.addEllipse(2*u,2*u,8*u,8*u)
        path.addEllipse(10*u,10*u,4*u,4*u)

        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerScaleDownSize,self).paint(painter,option,widget)

class moIconColorManagerSymmetry(moABaseIcon):
    Tips = '镜像（未实现）'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerSymmetry,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(3*u,6*u)
        path.lineTo(6*u,12*u)
        path.lineTo(6*u,4*u)
        path.closeSubpath()

        path.moveTo(10*u,4*u)
        path.lineTo(10*u,12*u)
        path.lineTo(13*u,6*u)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerSymmetry,self).paint(painter,option,widget)

class moIconColorManagerMoveXAdd(moABaseIcon):
    Tips = 'X方向移动＋ 选色'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerMoveXAdd,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(3*u,9*u)
        path.lineTo(8*u,9*u)
        path.lineTo(6*u,11*u)
        path.lineTo(13*u,8*u)
        path.lineTo(12*u,5*u)
        path.lineTo(10*u,7*u)
        path.lineTo(5*u,7*u)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerMoveXAdd,self).paint(painter,option,widget)

class moIconColorManagerMoveXSub(moABaseIcon):
    Tips = '-X方向移动 选色'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerMoveXSub,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(13*u,9*u)
        path.lineTo(8*u,9*u)
        path.lineTo(10*u,11*u)
        path.lineTo(3*u,8*u)
        path.lineTo(4*u,5*u)
        path.lineTo(6*u,7*u)
        path.lineTo(10*u,7*u)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerMoveXSub,self).paint(painter,option,widget)

class moIconColorManagerMoveYSub(moABaseIcon):
    Tips = '-Y方向移动'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerMoveYSub,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(7*u,5*u)
        path.lineTo(7*u,10*u)
        path.lineTo(5*u,12*u)
        path.lineTo(8*u,13*u)
        path.lineTo(11*u,6*u)
        path.lineTo(9*u,8*u)
        path.lineTo(9*u,3*u)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerMoveYSub,self).paint(painter,option,widget)

class moIconColorManagerMoveYAdd(moABaseIcon):
    Tips = 'Y方向移动'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerMoveYAdd,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(7*u,13*u)
        path.lineTo(7*u,8*u)
        path.lineTo(5*u,10*u)
        path.lineTo(8*u,3*u)
        path.lineTo(11*u,4*u)
        path.lineTo(9*u,6*u)
        path.lineTo(9*u,11*u)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerMoveYAdd,self).paint(painter,option,widget)

class moIconColorManagerMoveZAdd(moABaseIcon):
    Tips = 'Z方向移动'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerMoveZAdd,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(12*u,6*u)
        path.lineTo(9*u,6*u)
        path.lineTo(6*u,9*u)
        path.lineTo(4*u,9*u)
        path.lineTo(5*u,12*u)
        path.lineTo(12*u,9*u)
        path.lineTo(9*u,9*u)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerMoveZAdd,self).paint(painter,option,widget)

class moIconColorManagerMoveZSub(moABaseIcon):
    Tips = '-Z方向移动'
    def __init__(self,parent=None,size=24):
        super(moIconColorManagerMoveZSub,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(4*u,10*u)
        path.lineTo(7*u,10*u)
        path.lineTo(10*u,7*u)
        path.lineTo(12*u,7*u)
        path.lineTo(11*u,4*u)
        path.lineTo(4*u,7*u)
        path.lineTo(7*u,7*u)
        path.closeSubpath()
        self._path.addPath(path)

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        super(moIconColorManagerMoveZSub,self).paint(painter,option,widget)


class moIconNewFile(moABaseIcon):
    Tips = '新建文件'
    def __init__(self,parent=None,size=24):
        super(moIconNewFile,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.addRect(6*u,4*u,6*u,8*u)
        self._path.addPath(path)

class moIconOpenFile(moABaseIcon):
    Tips = '打开文件'
    def __init__(self,parent=None,size=24):
        super(moIconOpenFile,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(6*u,4*u)
        path.lineTo(6*u,8*u)
        path.lineTo(2*u,8*u)
        path.lineTo(6*u,12*u)
        path.lineTo(12*u,12*u)
        path.lineTo(12*u,4*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconSaveFile(moABaseIcon):
    Tips = '保存文件'
    def __init__(self,parent=None,size=24):
        super(moIconSaveFile,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(7*u,2*u)
        path.lineTo(7*u,4*u)
        path.lineTo(6*u,4*u)
        path.lineTo(8*u,6*u)
        path.lineTo(10*u,4*u)
        path.lineTo(9*u,4*u)
        path.lineTo(9*u,2*u)
        path.closeSubpath()
        path.addRect(4*u,6*u,8*u,6*u)
        self._path.addPath(path)

class moIconSaveFileAs(moABaseIcon):
    Tips = '另存文件'
    def __init__(self,parent=None,size=24):

        super(moIconSaveFileAs,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(10*u,2*u)
        path.lineTo(10*u,4*u)
        path.lineTo(12*u,4*u)
        path.lineTo(12*u,5*u)
        path.lineTo(14*u,3*u)
        path.lineTo(12*u,1*u)
        path.lineTo(12*u,2*u)
        path.closeSubpath()
        path.addRect(4*u,6*u,8*u,6*u)
        self._path.addPath(path)

class moIconAnalPic(moABaseIcon):
    Tips = '分析图片'
    def __init__(self,parent=None,size=24):
        super(moIconAnalPic,self).__init__(parent,size,selection=moBaseIcon.SelectClick)
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(10*u,3*u)
        path.lineTo(10*u,6*u)
        path.lineTo(13*u,6*u)
        path.lineTo(12*u,5*u)
        path.lineTo(14*u,3*u)
        path.lineTo(13*u,2*u)
        path.lineTo(11*u,4*u)
        path.closeSubpath()
        path.addRect(4*u,6*u,6*u,6*u)
        self._path.addPath(path)

class moIconHelpInfo(moABaseIcon):
    Tips = '显示帮助信息'
    def __init__(self,parent=None,size=24):
        super(moIconHelpInfo,self).__init__(parent,size,selection=moBaseIcon.SelectRotate)
        self._selecting=True
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.moveTo(6*u,2*u)
        path.lineTo(6*u,4*u)
        path.lineTo(7*u,4*u)
        path.lineTo(7*u,12*u)
        path.lineTo(6*u,12*u)
        path.lineTo(6*u,14*u)
        path.lineTo(10*u,14*u)
        path.lineTo(10*u,12*u)
        path.lineTo(9*u,12*u)
        path.lineTo(9*u,4*u)
        path.lineTo(10*u,4*u)
        path.lineTo(10*u,2*u)
        #path.lineTo(10*u,14*u)
        path.closeSubpath()
        self._path.addPath(path)

class moIconSetBgColor(moABaseIcon):
    Tips = '设置背景色'
    def __init__(self,parent=None,size=24):
        super(moIconSetBgColor,self).__init__(parent,size,selection=moBaseIcon.SelectRotate)
        self._selecting=False
    def mPath(self):
        u=self._size/16.0
        path=QtGui.QPainterPath()
        path.addRect(2*u,2*u,12*u,12*u)
        #path.moveTo(2*u,2*u)
        #path.lineTo(14*u,2*u)
        #path.lineTo(14*u,14*u)
        #path.lineTo(2*u,14*u)
        #path.lineTo(10*u,14*u)
        #path.closeSubpath()
        self._path.addPath(path)


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    view=QtWidgets.QGraphicsView()
    view.setFrameStyle(QtWidgets.QFrame.NoFrame)
    view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    scene=QtWidgets.QGraphicsScene()
    scene.setSceneRect(0,0,300,300)
    view.setScene(scene)
    item=moBaseIcon()
    scene.addItem(item)
    item.setPos(20,20)
    view.resize(300,300)
    view.move(100,100)
    view.show()
    sys.exit(app.exec_())
