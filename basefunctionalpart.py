#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-

from PyQt5 import QtCore,QtGui,QtWidgets
from dynamiccolor import *
from colorconvertc import rgb2jch,jch2rgb,rgb2xyz,xyz2rgb
from npcolorconvert import npjch2rgb
import colorindex
import numpy as np

class moDockDot(QtWidgets.QGraphicsObject):
    DockDrag=QtCore.pyqtSignal(object)
    def __init__(self,parent=None):
        super(moDockDot,self).__init__(parent)

        self.__isdragging=False
        self.setAcceptHoverEvents(True)
    def boundingRect(self):
        '''the overloading process'''
        return QtCore.QRectF(-8,-8,16,16)

    def shape(self):
        path=QtGui.QPainterPath()
        path.addRect(-8,-8,12,12)
        return path

    def paint(self,painter,option,widget):
        painter.setPen(QtCore.Qt.NoPen)
        if self.isUnderMouse():
            color=iconGetSelect('enabled')
        else:
            color=iconGetFgBase('enabled')
        painter.setBrush(QtGui.QBrush(color))
        path=QtGui.QPainterPath()
        path.moveTo(0,-4)
        path.lineTo(-4,0)
        path.lineTo(0,4)
        path.lineTo(4,0)
        path.closeSubpath()
        painter.drawPath(path)

    def mousePressEvent(self,event):
        if event.button() & QtCore.Qt.LeftButton:
            self.__isdragging=True

    def mouseReleaseEvent(self,event):
        if event.button() & QtCore.Qt.LeftButton:
            self.__isdragging=False

    def mouseMoveEvent(self,event):
        if self.__isdragging:
            self.DockDrag.emit(event)

class moDockLine(QtWidgets.QGraphicsObject):
    Left,Top,Right,Bottom=range(4)
    DockValue=QtCore.pyqtSignal([int],[float])
    def __init__(self,parent=None,\
                 dpos=2,limit=[0.0,1.0],defaultvalue=0.5,limittype=float,sidedist=0,headdist=0):
        super(moDockLine,self).__init__(parent)
        self.__width=50
        self.__height=50
        self.__dpos=dpos

        self.__limit=limit
        self.__limittype=limittype
        self.__nowervalue=0
        self.__dockdot=moDockDot(self)
        self.__sidedist = sidedist
        self.__headdist = headdist
        self.setCompoPos()
        self.__dockdot.DockDrag.connect(self.dotMover)
        self.resetValue(defaultvalue,init=True)

    def boundingRect(self):
        if self.__dpos == moDockLine.Left or self.__dpos == moDockLine.Right:
            return QtCore.QRectF(0,0,1,self.__height-2*self.__headdist)
        else:
            return QtCore.QRectF(0,0,self.__width-2*self.__headdist,1)
    def paint(self,painter,option,widget):
        pass
    def setCompoPos(self):
        if self.parentItem():
            size=self.parentItem().boundingRect().size()
            if self.__dpos == moDockLine.Left or\
               self.__dpos == moDockLine.Right:
                self.__width=size.width()
                self.__height=size.height()-2*self.__headdist
            elif self.__dpos == moDockLine.Top or\
                 self.__dpos == moDockLine.Bottom:
                self.__width=size.width()-2*self.__headdist
                self.__height=size.height()
            if self.__dpos == moDockLine.Left :
                self.setPos(self.__sidedist,self.__headdist)
            elif self.__dpos == moDockLine.Top:
                self.setPos(self.__headdist,self.__sidedist)
            elif self.__dpos==moDockLine.Right:
                self.setPos(self.__width-self.__sidedist,self.__headdist)
            elif self.__dpos==moDockLine.Bottom:
                self.setPos(self.__headdist,self.__height-self.__sidedist)

    def resetValue(self,value, init=False):
        if value > self.__limit[1]:
            value = self.__limit[1]
        elif value < self.__limit[0]:
            value = self.__limit[0]
        if value != self.__nowervalue or init:
            self.__nowervalue=value
            if self.__dpos == moDockLine.Left or self.__dpos == moDockLine.Right:
                posy=\
                    self.__limittype.__call__(\
                    (self.__limit[1]-value)*1.0*\
                    self.__height/(self.__limit[1]-self.__limit[0]))
                self.__dockdot.setPos(0,posy)
            elif self.__dpos == moDockLine.Top or self.__dpos == moDockLine.Bottom:
                posx=\
                    self.__limittype.__call__(\
                    (value-self.__limit[0])*1.0*\
                    self.__width/(self.__limit[1]-self.__limit[0]))
                self.__dockdot.setPos(posx,0)

    @QtCore.pyqtSlot(object)
    def dotMover(self,event):
        value=0
        if self.__dpos == moDockLine.Left or self.__dpos == moDockLine.Right:
            move=event.pos().y()-event.lastPos().y()
            self.__dockdot.moveBy(0,move)
            if self.__dockdot.pos().y()>self.__height:
                self.__dockdot.setPos(0,self.__height)
            elif self.__dockdot.pos().y()<0:
                self.__dockdot.setPos(0,0)
            value=\
                self.__limittype.__call__\
                ((self.__height-self.__dockdot.pos().y())*\
                 (self.__limit[1]-self.__limit[0])*\
                 1.0/self.__height+self.__limit[0])
        elif self.__dpos == moDockLine.Top or self.__dpos == moDockLine.Bottom:
            move=event.pos().x()-event.lastPos().x()
            self.__dockdot.moveBy(move,0)
            if self.__dockdot.pos().x()>self.__width:
                self.__dockdot.setPos(self.__width,0)
            elif self.__dockdot.pos().x()<0:
                self.__dockdot.setPos(0,0)
            value=\
                self.__limittype.__call__\
                (self.__dockdot.pos().x()*\
                 (self.__limit[1]-self.__limit[0])*1.0/self.__width+\
                 self.__limit[0])
        if value != self.__nowervalue:
            self.__nowervalue=self.__limittype.__call__(value)
            self.DockValue.emit(self.__nowervalue)


class moInput(QtWidgets.QGraphicsTextItem):
    InputFinish = QtCore.pyqtSignal(str)
    HasFocus,NoFocus=['hasfocus','nofocus']
    FocusOut = QtCore.pyqtSignal(object)
    Type = QtWidgets.QGraphicsTextItem.UserType+10000
    def __init__(self,parent=None,width=120,maxletter=15):
        super(moInput,self).__init__(parent)

        self.__maxletter=maxletter
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable)
        self.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.setTabChangesFocus(True)
        if self.parentItem():
            self.setZValue(self.parentItem().zValue()+1)
        self.setTextWidth(width)
        u=QtGui.QTextOption()
        u.setWrapMode(QtGui.QTextOption.NoWrap)
        self.document().setDefaultTextOption(u)
        self.setDefaultTextColor(QtGui.QColor(255,255,255,128))
        self.setFont(QtGui.QFont("sansserif",pointSize=10))
        self.document().setMaximumBlockCount(1)

    def boundingRect(self):
        return QtCore.QRectF(0,0,self.textWidth(),20)

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(0,0,self.textWidth(),20)
        return path

    def paint(self,painter,option,widget):
        if self.hasFocus():
            state=moInput.HasFocus
        else:
            state=moInput.NoFocus
        painter.setPen(inputGetFrameBorder(state))
        painter.setBrush(inputGetFrameBg(state))
        painter.drawRoundedRect(0,3,self.textWidth(),17,3,3)
        d=self.document().documentLayout().PaintContext()
        d.palette=QtGui.QPalette(\
                                 QtGui.QBrush(QtGui.QColor(255,0,20,35)),\
                                 QtGui.QBrush(QtGui.QColor(255,0,20,35)),\
                                 QtGui.QBrush(QtGui.QColor(255,0,20,35)),\
                                 QtGui.QBrush(QtGui.QColor(255,0,20,35)),\
                                 QtGui.QBrush(QtGui.QColor(0,255,255,50)),\
                                 inputGetTextColor(state),\
                                 QtGui.QBrush(QtGui.QColor(255,255,0,50)),\
                                 QtGui.QBrush(QtGui.QColor(255,255,255,150)),\
                                 QtGui.QBrush(QtGui.QColor(255,145,255,50)))
        if int(option.state & (QtWidgets.QStyle.State_Selected |\
                                           QtWidgets.QStyle.State_HasFocus)):
            d.cursorPosition=self.textCursor().position()
            if self.textCursor().hasSelection():
                a= QtWidgets.QAbstractTextDocumentLayout.Selection()
                a.cursor=self.textCursor()
                b=QtWidgets.QTextCharFormat()
                pen=inputGetTextOutline(state)
                b.setTextOutline(pen)
                a.format=b
                d.selections=[a]
        self.document().documentLayout().draw(painter,d)

    def keyPressEvent(self,event):
        if event.key()==QtCore.Qt.Key_Return:
            self.clearFocus()
        elif event.key()==QtCore.Qt.Key_Backspace:
            super(moInput,self).keyPressEvent(event)
        elif event.key()==QtCore.Qt.Key_Escape:
            self.clearFocus()
        elif self.document().characterCount()>self.__maxletter and\
             event.text()!='':
            if self.textCursor().position()==self.__maxletter:
                self.textCursor().deletePreviousChar()
                super(moInput,self).keyPressEvent(event)
            else:
                super(moInput,self).keyPressEvent(event)
                self.textCursor().deletePreviousChar()
        else:
            super(moInput,self).keyPressEvent(event)
    def sceneEvent(self,event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key()==QtCore.Qt.Key_Tab:
                self.clearFocus()
                self.FocusOut.emit(self)
                return False
            else:
                super(moInput,self).sceneEvent(event)
                return True
        else:
            super(moInput,self).sceneEvent(event)
            return True

    def focusOutEvent(self,event):
        self.setSelected(False)
        text = self.document().toPlainText()
        self.InputFinish.emit(text)

    def type(self):
        return moInput.Type

class moDragLine(QtWidgets.QGraphicsObject):
    LineDrag=QtCore.pyqtSignal(int,object)
    Left,Top,Right,Bottom= [1,2,4,8]
    def __init__(self,parent=None,dpos=2):
        super(moDragLine,self).__init__(parent)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsFocusable)
        self.setAcceptHoverEvents(True)
        self.__dpos=dpos
        self.__isdragging=False
        self.setAcceptHoverEvents(True)
        self.__width=0
        self.__height=0
        self.__length=10
        self.__affect=4
        self.__border=1
        self.update()
    def update(self):
        if self.parentItem():
            size=self.parentItem().boundingRect().size()
            self.__width=size.width()
            self.__height=size.height()
            if self.__dpos == moDragLine.Left:
                self.setPos(0,0)
                self.__length=self.__height-30
            elif self.__dpos==moDragLine.Right:
                self.setPos(self.__width-4,0)
                self.__length=self.__height-30
            elif self.__dpos==moDragLine.Bottom:
                self.setPos(0,self.__height-4)
                self.__length=self.__width-30
            elif self.__dpos==moDragLine.Top:
                self.setPos(0,0)
                self.__length=self.__width-30
        super(moDragLine,self).update()

    def boundingRect(self):
        if self.__dpos == moDragLine.Left or self.__dpos==moDragLine.Right:
            return QtCore.QRectF(0,0,4,self.__height)
        elif self.__dpos == moDragLine.Top or self.__dpos==moDragLine.Bottom:
            return QtCore.QRectF(0,0,self.__width,4)

    def shape(self):
        path=QtGui.QPainterPath()
        if self.__dpos == moDragLine.Left or self.__dpos==moDragLine.Right:
            path.addRect(0,0,4,self.__height)
        elif self.__dpos == moDragLine.Top or self.__dpos==moDragLine.Bottom:
            path.addRect(0,0,self.__width,4)
        return path

    def paint(self,painter,option,widget):
        painter.setPen(QtCore.Qt.NoPen)
        if self.isUnderMouse():
            color=iconGetSelect('enabled')
        else:
            color=panelGetBorder().color()
        painter.setBrush(QtGui.QBrush(color))
        path=QtGui.QPainterPath()
        if self.__dpos == moDragLine.Left:
            path.addRect(2,self.__height/2-20,1,40)
        elif self.__dpos == moDragLine.Top:
            path.addRect(self.__width/2-20,2,40,1)
        elif self.__dpos==moDragLine.Right:
            path.addRect(0,self.__height/2-20,1,40)
        elif self.__dpos==moDragLine.Bottom:
            path.addRect(self.__width/2-20,0,40,1)
        painter.drawPath(path)

    def mousePressEvent(self,event):
        if event.button() & QtCore.Qt.LeftButton:
            self.__isdragging=True

    def hoverEnterEvent(self,event):
        if self.__dpos == moDragLine.Left or self.__dpos==moDragLine.Right:
            self.setCursor(QtCore.Qt.SplitHCursor)
        elif self.__dpos == moDragLine.Top or self.__dpos==moDragLine.Bottom:
            self.setCursor(QtCore.Qt.SplitVCursor)

    def mouseReleaseEvent(self,event):
        if event.button() & QtCore.Qt.LeftButton:
            self.__isdragging=False
            self.clearFocus()

    def mouseMoveEvent(self,event):
        if self.__isdragging:
            self.LineDrag.emit(self.__dpos,event)

#class moCC(QtWidgets.QGraphicsObject):
#    def __init__(self,parent=None,color=[200,100,30],scale=1,jch=None):
#        super(moCC,self).__init__(parent)
#        self.__color = color
#        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)#

#    def boundingRect(self):
#        return QtCore.QRectF(0,0,18,18)
#    def paint(self,painter,option,widget):
        #print 'ppppp called'
#        pass

class moColorPiece(QtWidgets.QGraphicsObject):
    Update = QtCore.pyqtSignal(int)
    Type=QtWidgets.QGraphicsObject.UserType + 1000
    Selected=QtCore.pyqtSignal(object,bool,bool)
    def __init__(self,parent=None,color=[100,100,150],scale=1,jch=None):
        super(moColorPiece,self).__init__(parent)
        if color[0]<0:
            color[0]=0
        if color[1]<0:
            color[1]=0
        if color[2]<0:
            color[2]=0
        if color[0]>255:
            color[0]=255
        if color[1]>255:
            color[1]=255
        if color[2]>255:
            color[2]=255
        self._color=color
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.__displayinscene = True
        self._scale = scale
        if jch==None:
            jch = rgb2jch(self._color)
            self._renderpos = [jch[2],jch[0],jch[1]]
        else:
            self._renderpos = jch
    def __getstate__(self):
        return (self._color,self.__displayinscene,self._scale,self._renderpos)

    def __setstate__(self,state):
        self.__init__()
        self._color,self.__displayinscene,self._scale,self._renderpos=state



    def boundingRect(self):
        return QtCore.QRectF(0,0,18,18)

    def type(self):
        return moColorPiece.Type

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(2,2,14,14)
        return path

    def paint(self,painter,option,widget):
        #print 'paint called'
        if self.isSelected():
            color=[self._color[0]-20,self._color[1]-20,self._color[2]-20]
            if color[0]<0:color[0]=0
            if color[1]<0:color[1]=0
            if color[2]<0:color[2]=0
            pen=QtGui.QPen(QtGui.QColor(color[0],color[1],color[2],255))
            pen.setWidth(2)
            painter.setPen(pen)
        else:
            painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(self._color[0],\
                                                   self._color[1],\
                                                   self._color[2],255)))
        painter.drawRoundedRect(2,2,14,14,0,0)
        #print 'ffff'

    def mousePressEvent(self,event):
        shifted = False
        if event.button() & QtCore.Qt.LeftButton:
            self.setSelected(not self.isSelected())
        if event.modifiers() & QtCore.Qt.ShiftModifier:
            shifted = True
        self.Selected.emit(self,self.isSelected(),shifted)

    def mouseReleaseEvent(self,event):
        pass
#
    def setPieceColor(self,color):
        if color[0]<0:
            color[0]=0
        if color[1]<0:
            color[1]=0
        if color[2]<0:
            color[2]=0
        if color[0]>255:
            color[0]=255
        if color[1]>255:
            color[1]=255
        if color[2]>255:
            color[2]=255
        self._color=color
#
        self.update()
#
    def getPieceColor(self):
        return self._color
#
    def getScaleSize(self):
        return self._scale
#
    def setScaleSize(self,scale):
        self._scale = scale
#
    def setColorDisplay(self,show):
        self.__displayinscene=show

    def getColorDisplay(self):
        return self.__displayinscene
#
#    def itemChange(self,change,value):
#        pass
#        print "change",change,"value", value
#        if change == self.ItemSelectedHasChanged:
#            self.Selected.emit(self,value==True)
            #return value==True
#        else:
#            return super(moColorPiece,self).itemChange(change,value)
#        return super(moColorPiece,self).itemChange(change,value)
#
    def setRenderPos(self,jch):
        self._renderpos = [jch[2],jch[0],jch[1]]

    def getRenderPos(self):
        return self._renderpos

    def posRotateBy(self,hue):
        h,j,c = self.getRenderPos()
        h+=hue
        while h>=360:
            h -=360
        while h<0:
            h += 360
        r,g,b = jch2rgb([j,c,h])
        if  r>255 or g>255 or b>255:
            return
        if r<=255 and r>=0 and g<=255 and g>=0 and b<=255 and b>=0:
            self.setRenderPos([j,c,h])
            self.setPieceColor([r,g,b])
    def posScaleBy(self,size):
        h,j,c = self.getRenderPos()

        jbc = j-50
        l = (jbc**2+c**2)**0.5
        proj = jbc/l
        proc = c/l
        l += size
        if l<=0:
            l=0.5
        jbc = l*proj
        c   = l*proc
        j = jbc+50

        r,g,b = jch2rgb([j,c,h])
        if  r>255 or g>255 or b>255:
            return
        if r<=255 and r>=0 and g<=255 and g>=0 and b<=255 and b>=0:
            self.setRenderPos([j,c,h])
            self.setPieceColor([r,g,b])

    def posMoveByX(self,movelength):
        h,j,c = self.getRenderPos()
        height = c * np.sin(h*np.pi/180)
        width = c * np.cos(h*np.pi/180)
        c = ((width + movelength)**2 + height**2)**0.5
        h = np.arctan2(height,width+movelength)*180/np.pi
        while h>=360:
            h -=360
        while h<0:
            h += 360
        r,g,b = jch2rgb([j,c,h])
        if  r>255 or g>255 or b>255:
            return
        if r<=255 and r>=0 and g<=255 and g>=0 and b<=255 and b>=0:
            self.setRenderPos([j,c,h])
            self.setPieceColor([r,g,b])

    def posMoveByZ(self,movelength):
        h,j,c = self.getRenderPos()
        height = c * np.sin(h*np.pi/180)
        width = c * np.cos(h*np.pi/180)
        c = (width**2 + (height+movelength)**2)**0.5
        h = np.arctan2(height+movelength,width)*180/np.pi
        while h>=360:
            h -=360
        while h<0:
            h += 360
        r,g,b = jch2rgb([j,c,h])
        if  r>255 or g>255 or b>255:
            return
        if r<=255 and r>=0 and g<=255 and g>=0 and b<=255 and b>=0:
            self.setRenderPos([j,c,h])
            self.setPieceColor([r,g,b])

    def posMoveByY(self,movelength):
        h,j,c = self.getRenderPos()
        j+=movelength
        r,g,b = jch2rgb([j,c,h])
        if  r>255 or g>255 or b>255:
            return
        if r<=255 and r>=0 and g<=255 and g>=0 and b<=255 and b>=0:
            self.setRenderPos([j,c,h])
            self.setPieceColor([r,g,b])

class moColorListPiece(QtWidgets.QGraphicsObject):
    Update = QtCore.pyqtSignal(int)
    Type=QtWidgets.QGraphicsItem.UserType + 1002
    Selected=QtCore.pyqtSignal(object,bool,bool)
    def __init__(self,parent=None,color=np.array([[0,0,0]]),hjcs=np.array([[1,1,1,1]])):
        super(moColorListPiece,self).__init__(parent)
        self._color = color
        self._hjcs = hjcs
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self.__displayinscene = True
    def __getstate__(self):
        return [self._color,self.__displayinscene,self._hjcs]

    def __setstate__(self,state):
        self.__init__()
        self._color,self.__displayinscene,self._hjcs=state

    def boundingRect(self):
        return QtCore.QRectF(0,0,18,18)

    def type(self):
        return moColorListPiece.Type

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(0,0,18,18)

    def paint(self,painter,option,widget):

        if self.isSelected():
            pen=QtGui.QPen(QtGui.QColor(230,230,230,255))
            pen.setWidth(2)
            painter.setPen(pen)
        else:
            painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(250,250,250,255)))
        painter.drawRoundedRect(-1,-1,19,19,8,8)

    def mousePressEvent(self,event):
        shifted = False
        if event.button() & QtCore.Qt.LeftButton:
            self.setSelected(not self.isSelected())
        if event.modifiers() & QtCore.Qt.ShiftModifier:
            shifted = True
        self.Selected.emit(self,self.isSelected(),shifted)

#    def mousePressEvent(self,event):
#        if event.button() & QtCore.Qt.LeftButton:
#            self.setSelected(not self.isSelected())
#        self.Selected.emit(self,self.isSelected())

    def mouseReleaseEvent(self,event):
        pass

    def setPieceColor(self,color):
        pass

    def getPieceColor(self):
        return self._color

    def getScaleSize(self):
        return self._hjcs[:,3]

    def setScaleSize(self,scale):
        pass

    def setColorDisplay(self,show):
        self.__displayinscene=show

    def getColorDisplay(self):
        return self.__displayinscene

#    def itemChange(self,change,value):
#        if change == self.ItemSelectedHasChanged:
#            self.Selected.emit(self,value==True)
#            return value==True
#        else:
#            return super(moColorListPiece,self).itemChange(change,value)

    def setRenderPos(self,jch):
        pass

    def getRenderPos(self):
        return self._hjcs[:,:3]

    def getHjcs(self):
        return self._hjcs

    def posRotateBy(self,hue):
        hjcs = self._hjcs
        h = self._hjcs[:,0]
        j = self._hjcs[:,1]
        c = self._hjcs[:,2]
        s = self._hjcs[:,3]
        h = h + hue
        h = np.where(h<0,h+360,h)
        h = np.where(h>=360,h-360,h)
        self._hjcs = np.array([h,j,c,s]).T
        self._color = npjch2rgb(np.array([j,c,h]).T)

    def posScaleBy(self,size):
        hjcs = self._hjcs
        h = self._hjcs[:,0]
        j = self._hjcs[:,1]
        c = self._hjcs[:,2]
        s = self._hjcs[:,3]

        jbc = j-50
        l = (jbc**2+c**2)**0.5
        proj = jbc/l
        proc = c/l
        l = l + size
        l = np.where(l<=0,0.1,l)
        jbc = l*proj
        c   = l*proc
        j = jbc+50

        rgb = npjch2rgb(np.array([j,c,h]).T)
        if np.any(rgb>255):
            return
        self._color = rgb
        self._hjcs = np.array([h,j,c,s]).T

    def posMoveByX(self,movelength):
        hjcs = self._hjcs
        h = self._hjcs[:,0]
        j = self._hjcs[:,1]
        c = self._hjcs[:,2]
        s = self._hjcs[:,3]

        height = c * np.sin(h*np.pi/180)
        width = c * np.cos(h*np.pi/180)

        c = ((width + movelength)**2 + height**2)**0.5
        h = np.arctan2(height,width+movelength)*180/np.pi
        h = np.where(h<0,h+360,h)
        h = np.where(h>=360,h-360,h)

        rgb = npjch2rgb(np.array([j,c,h]).T)
        if np.any(rgb>255):
            return

        self._color = rgb
        self._hjcs = np.array([h,j,c,s]).T

    def posMoveByZ(self,movelength):
        hjcs = self._hjcs
        h = self._hjcs[:,0]
        j = self._hjcs[:,1]
        c = self._hjcs[:,2]
        s = self._hjcs[:,3]

        height = c * np.sin(h*np.pi/180)
        width = c * np.cos(h*np.pi/180)

        c = (width**2 + (height+movelength)**2)**0.5
        h = np.arctan2(height+movelength,width)*180/np.pi
        h = np.where(h<0,h+360,h)
        h = np.where(h>=360,h-360,h)

        rgb = npjch2rgb(np.array([j,c,h]).T)
        if np.any(rgb>255):
            return

        self._color = rgb
        self._hjcs = np.array([h,j,c,s]).T

    def posMoveByY(self,movelength):
        hjcs = self._hjcs
        h = self._hjcs[:,0]
        j = self._hjcs[:,1]
        c = self._hjcs[:,2]
        s = self._hjcs[:,3]

        j=j+movelength
        rgb = npjch2rgb(np.array([j,c,h]).T)
        if np.any(rgb>255):
            return

        self._color = rgb
        self._hjcs = np.array([h,j,c,s]).T


class moColorGroupPiece(QtWidgets.QGraphicsObject):
    Type=QtWidgets.QGraphicsItem.UserType + 1001
    Selected=QtCore.pyqtSignal(object,bool,bool)
    Update = QtCore.pyqtSignal(int)
    Fold,UnFold=[True,False]
    def __init__(self,parent=None,color=[100,100,100]):
        super(moColorGroupPiece,self).__init__(parent)
        self._color=color
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
        self._child=[]
        self._fold=moColorGroupPiece.UnFold
        self.__iconshow=True
        self._foldicon=moFoldIcon(self)
        self._foldicon.Clicked.connect(self.turnFold)
        self.__displayinscene = True
        self._scale=1

    def __getstate__(self):
        return (self._color,self._child,self._fold,self.__iconshow,\
                self.__displayinscene,self._scale)

    def __setstate__(self,state):
        self.__init__()
        self._color,child,self._fold,self.__iconshow,self.__displayinscene,self._scale=state
        if child:
            for i in range(len(child)):
                if child[i].type()==moColorPiece.Type:
                    arg=child[i].__getstate__()
                    child[i].__init__()
                    child[i].__setstate__(arg)
                    self.addChild(i,child[i])
                else:
                    arg=child[i].__getstate__()
                    child[i].__init__()
                    child[i].__setstate__(arg)
                    self.addChild(i,child[i])


    def update(self):
        if self.__iconshow==True:
            self._foldicon.setVisible(True)

        super(moColorGroupPiece,self).update()

    def boundingRect(self):
        return QtCore.QRectF(0,0,18,18)

    def type(self):
        return moColorGroupPiece.Type

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(1,1,16,16)
        return path

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        color = self.getPieceColor()
        increase = getIncreaseColor()
        if self.isSelected():
            color1=[color[0]+increase,color[1]+increase,color[2]+increase]
            if color1[0]<0:color1[0]=0
            if color1[1]<0:color1[1]=0
            if color1[2]<0:color1[2]=0
            if color1[0]>255:color1[0]=255
            if color1[1]>255:color1[1]=255
            if color1[2]>255:color1[2]=255
            pen=QtGui.QPen(QtGui.QColor(color1[0],color1[1],color1[2],255))
            pen.setWidth(2)
            painter.setPen(pen)
        else:
            painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(color[0],\
                                                   color[1],\
                                                   color[2],255)))
        painter.drawRoundedRect(4,4,10,10,3,3)

    def mousePressEvent(self,event):
        shifted = False
        if event.button() & QtCore.Qt.LeftButton:
            self.setSelected(not self.isSelected())
        if event.modifiers() & QtCore.Qt.ShiftModifier:
            shifted = True
        self.Selected.emit(self,self.isSelected(),shifted)

#    def mousePressEvent(self,event):
#        if event.button() & QtCore.Qt.LeftButton:
#            self.setSelected(not self.isSelected())
#        self.Selected.emit(self,self.isSelected())

    def mouseReleaseEvent(self,event):
        pass


    def getPieceColor(self):
        if self._child:
            length = 0 #len(self._child)
            #r,g,b=[0,0,0]
            x,y,z=[0,0,0]
            for i in self._child:
                if i.type()==moColorPiece.Type:
                    c = rgb2xyz(i.getPieceColor())
                    ll = i.getScaleSize()**2
                    length += ll
                    x+=ll*c[0]
                    y+=ll*c[1]
                    z+=ll*c[2]
                else:
                    try:
                        assert(i.type()==moColorGroupPiece.Type)
                        #length -= 1
                        leng,color = i.getChildColor()
                        length += leng
                        x += color[0]
                        y += color[1]
                        z += color[2]
                    except AssertionError:
                        print('assertionerror')
                        pass
            if length==0:
                return [0,0,0]
            else:
                rgb = xyz2rgb([x/length,y/length,z/length])
                #r,g,b = rgb
                return rgb #[int(r/length),int(g/length),int(b/length)]

        else:
            return [0,0,0]

    def getChildColor(self):
        if self._child == []:
            return [0,[0,0,0]]
        else:
            length = 0#len(self._child)
            x,y,z=[0,0,0]
            for i in self._child:
                if i.type()==moColorPiece.Type:
                    c = rgb2xyz(i.getPieceColor())
                    ll = i.getScaleSize()**2
                    length += ll
                    x += ll*c[0]
                    y += ll*c[1]
                    z += ll*c[2]
                else:
                    try:
                        assert(i.type()==moColorGroupPiece.Type)
                        #length -= 1
                        leng,color= i.getChildColor()
                        length += leng
                        x += color[0]
                        y += color[1]
                        z += color[2]
                    except AssertionError:
                        print('assertion  error')
                        pass
            return [length,[x,y,z]]

    def getFold(self):
        return self._fold

    def getRenderPos(self):
        color = self.getPieceColor()
        j,c,h = rgb2jch(color)
        return [h,j,c]

    def getScaleSize(self):
        return self._scale

    def setScaleSize(self,scale):
        self._scale = scale

    def iconShow(self,show):
        self.__iconshow=show
        self._foldicon.setVisible(show)
        self.update()

    def addChild(self,pos,child):
        if child.parentItem() != self:
            child.setParentItem(self)
        self._child.insert(pos,child)
        child.Update.connect(self.Update.emit)
        child.Selected.connect(self.Selected.emit)
        self.refreshColor()

    def getChild(self):
        return self._child

    def removeChild(self,child):
        if child in self._child:
            self._child.remove(child)
            self.scene().removeItem(child)
        self.refreshColor()

    def refreshColor(self):
        if self._child:
            length = len(self._child)
            r,g,b=[0,0,0]
            for i in self._child:
                c =i.getPieceColor()
                r+=c[0]
                g+=c[1]
                b+=c[2]
            self._color = [r/length,g/length,b/length]

    @QtCore.pyqtSlot()
    def turnFold(self):
        self._foldicon.turnFold()
        self._fold = not self._fold
        self.Update.emit(1)

    def setColorDisplay(self,show):
        self.__displayinscene=show

    def getColorDisplay(self):
        return self.__displayinscene

#    def itemChange(self,change,value):
#        arg = super(moColorGroupPiece,self).itemChange(change,value)
#        if change == self.ItemSelectedHasChanged:
#            self.Selected.emit(self,self.isSelected())
#        return arg

    def posRotateBy(self,hue):
        for i in self._child:
            i.posRotateBy(hue)

    def posScaleBy(self,size):
        for i in self._child:
            i.posScaleBy(size)

    def posMoveByX(self,movelength):
        for i in self._child:
            i.posMoveByX(movelength)

    def posMoveByY(self,movelength):
        for i in self._child:
            i.posMoveByY(movelength)

    def posMoveByZ(self,movelength):
        for i in self._child:
            i.posMoveByZ(movelength)
class moFoldIcon(QtWidgets.QGraphicsObject):
    Clicked = QtCore.pyqtSignal()
    def __init__(self,parent=None):
        super(moFoldIcon,self).__init__(parent)
        self.__fold = False
        self.setPos(-6,0)
        self.setVisible(False)

    def boundingRect(self):
        return QtCore.QRectF(0,0,6,18)
    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(-2,0,8,18)
        return path
        return QtCore.QRectF(0,0,6,18)
    def paint(self,painter,option,widget):
        path=QtGui.QPainterPath()
        if self.__fold==True:
            path.moveTo(0,6)
            path.lineTo(4,9)
            path.lineTo(0,12)
            path.closeSubpath()
        else:
            path.moveTo(0,9)
            path.lineTo(6,9)
            path.lineTo(3,12)
            path.closeSubpath()
        painter.setPen(QtCore.Qt.NoPen)
        color=inputGetFrameBorder('hasfocus').color()
        painter.setBrush(color)
        painter.drawPath(path)

    def turnFold(self):
        self.__fold=not self.__fold

    def mousePressEvent(self,event):
        if event.button() & QtCore.Qt.LeftButton:
            self.Clicked.emit()


class moLookEye(QtWidgets.QGraphicsObject):
    Type = QtWidgets.QGraphicsItem.UserType + 101
    Clicked= QtCore.pyqtSignal(bool)
    Show,Hide = [True,False]
    def __init__(self,parent=None):
        super(moLookEye,self).__init__(parent)
        self._state=moLookEye.Show

    def type(self):
        return moLookEye.Type

    def boundingRect(self):
        return QtCore.QRectF(0,0,14,18)

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing)
        path=QtGui.QPainterPath()
        path.moveTo(1,7)
        path.cubicTo(4,4,10,4,13,7)
        path.cubicTo(10,13,4,13,1,7)
        path.closeSubpath()
        path2=QtGui.QPainterPath()
        path2.addEllipse(5,6,4,4)
        if self._state == moLookEye.Show:
            state='undermouse'
        else:
            state = 'disabled'
        pen=QtGui.QPen(iconGetFgBase(state))
        painter.setPen(pen)
        painter.drawPath(path)
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtGui.QBrush(iconGetFgBase(state)))
        painter.drawPath(path2)

    def mousePressEvent(self,event):
        if event.button() & QtCore.Qt.LeftButton:
            self._state = not self._state
            self.Clicked.emit(self._state)
            self.update()

    def setState(self,state):
        self._state = state
        self.update()

    def updateState(self,state):
        self._state = state
        self.Clicked.emit(self._state)
        self.update()
