#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-

from PyQt5 import QtCore,QtWidgets,QtGui
import icons
from dynamiccolor import *
from basefunctionalpart import *
from colorconvertc import jch2rgb,rgb2jch

class moBaseFrame(QtWidgets.QGraphicsObject):
    Type=QtWidgets.QGraphicsItem.UserType+10
    Horizontal,Vertical=range(2)

    def __init__(self,parent=None,\
                 direction = 0):
        super(moBaseFrame,self).__init__(parent)
        self.__direction=direction


    def boundingRect(self):
        units=self.childItems()
        count=len(units)
        if count==0:
            count=1
        if units:
            unit=units[0].boundingRect()
        else:
            unit=QtCore.QRect(0,0,10,10)
        if self.__direction==moBaseFrame.Horizontal:
            width=unit.size().width()*count+4
            height=unit.size().height()+4
        else:
            width=unit.size().width()+4
            height=unit.size().height()*count+4
        return QtCore.QRectF(0,0,width,height)

    def shape(self):
        path=QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        p=containerBorderGetColor()
        painter.setPen(p)
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawRect(self.boundingRect())

class moRadioFrame(moBaseFrame):
    ModeExchange = QtCore.pyqtSignal(str)
    def __init__(self,parent=None,size=24):
        super(moRadioFrame,self).__init__(parent,direction=moBaseFrame.Horizontal)
        self.__selectedicon=None

    @QtCore.pyqtSlot(object,str)
    def modeChange(self,icon,info):
        if self.__selectedicon==None:
            self.__selectedicon=icon
        else:
            self.__selectedicon.clearSelecting()
            self.__selectedicon=icon
        self.ModeExchange.emit(info)

    def setSelectedIcon(self,icon):
        icon.setSelecting(True)
        self.__selectedicon=icon

class moModeFrame(moRadioFrame):
    def __init__(self,parent=None,size=24):
        super(moModeFrame,self).__init__(parent,moBaseFrame.Horizontal)
        self.__overall = icons.moIconModeOverall(self,size)
        self.__overall.setPos(2,2)
        self.__panel   = icons.moIconModePanel(self,size)
        self.__panel.setPos(size+2,2)
        self.__plate   = icons.moIconModePlate(self,size)
        self.__plate.setPos(size*2+2,2)
        self.setSelectedIcon(self.__overall)
        self.__overall.Onclicked.connect(self.modeChange)
        self.__panel.Onclicked.connect(self.modeChange)
        self.__plate.Onclicked.connect(self.modeChange)

    def setSelection(self,info):
        for icon in [self.__overall,self.__panel,self.__plate]:
            if info != icon.Info:
                icon.clearSelecting()
            else:
                self.setSelectedIcon(icon)

class moColorFrame(QtWidgets.QGraphicsObject):
    ColorSender=QtCore.pyqtSignal(object,str,list)
    def __init__(self,parent=None):
        super(moColorFrame,self).__init__(parent)

        self._r=0
        self._g=0
        self._b=0
        self._j=0
        self._c=0
        self._h=0
        self.setCacheMode(QtWidgets.QGraphicsItem.DeviceCoordinateCache)
        if self.parentItem():
            self.setZValue(self.parentItem().zValue()+2)
        self._dockright=moDockLine(self,moDockLine.Left,[0,99],0,int)
        self._docktop=moDockLine(self,moDockLine.Top,[0,359],0,int)
        self._dockbottom=moDockLine(self,moDockLine.Bottom,[0,120],0,int)
        self._dockright.DockValue.connect(self._respondJ)
        self._docktop.DockValue.connect(self._respondH)
        self._dockbottom.DockValue.connect(self._respondC)

    @QtCore.pyqtSlot(int)
    def _respondJ(self,j):
        self._j=j
        self._r,self._g,self._b=jch2rgb([self._j,self._c,self._h])
        while(self._r<0 or self._r>255 or\
              self._g<0 or self._g>255 or\
              self._b<0 or self._b>255):
            if self._c>0:
                self._c-=1
            elif self._c<0:
                self._c +=1
            else:
                break
#        self._j,self._c,self._h =map(lambda x:int(x),\
#                                     rgb2jch([self._r,self._g,self._b]))
            self._r,self._g,self._b=jch2rgb([self._j,self._c,self._h])
        self._dockright.resetValue(self._j)
        self._docktop.resetValue(self._h)
        self._dockbottom.resetValue(self._c)
        self.update()
        self.ColorSender.emit(self,"JCH",[self._j,self._c,self._h])

    @QtCore.pyqtSlot(int)
    def _respondH(self,h):
        while h>=360:
            h-=360
        while h<0:
            h+=360
        self._h=h
        self._r,self._g,self._b=jch2rgb([self._j,self._c,self._h])
        while(self._r<0 or self._r>255 or\
              self._g<0 or self._g>255 or\
              self._b<0 or self._b>255):
            if self._c>0:
                self._c-=1
            elif self._c<0:
                self._c +=1
            else:
                break
            self._r,self._g,self._b=jch2rgb([self._j,self._c,self._h])
        self._dockright.resetValue(self._j)
        self._docktop.resetValue(self._h)
        self._dockbottom.resetValue(self._c)
        self.update()
        self.ColorSender.emit(self,"JCH",[self._j,self._c,self._h])
        #self.ColorSender.emit([self._r,self._g,self._b,\
        #                       self._j,self._c,self._h])

    @QtCore.pyqtSlot(int)
    def _respondC(self,c):
        self._c=c
        self._r,self._g,self._b=jch2rgb([self._j,self._c,self._h])
        while(self._r<0 or self._r>255 or\
              self._g<0 or self._g>255 or\
              self._b<0 or self._b>255):
            if self._c>0:
                self._c-=1
            elif self._c<1:
                self._c +=1
            else:
                break
            self._r,self._g,self._b=jch2rgb([self._j,self._c,self._h])
        self._dockright.resetValue(self._j)
        self._docktop.resetValue(self._h)
        self._dockbottom.resetValue(self._c)
        self.update()
        self.ColorSender.emit(self,"JCH",[self._j,self._c,self._h])


    def setRGB(self,rgb):
        r,g,b = rgb
        if r>255:
            r=255
        if r<0:
            r=0
        self._r=r
        if g>255:
            g=255
        if g<0:
            g=0
        self._g=g
        if b>255:
            b=255
        if b<0:
            b=0
        self._b=b
        self._j,self._c,self._h =map(lambda x:int(x),\
                                     rgb2jch([self._r,self._g,self._b]))
        self._dockbottom.resetValue(self._c)
        self._docktop.resetValue(self._h)
        self._dockright.resetValue(self._j)
        self.update()

    def responseInfo(self,value):
        self.setRGB(value[:3])



    def getRGB(self):
        return [self._r,self._g,self._b]

    def boundingRect(self):
        return QtCore.QRectF(0,0,57,57)

    def shape(self):
        path=QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        painter.setPen(panelGetBorder())
        painter.setBrush(QtGui.QBrush(QtGui.QColor(self._r,self._g,self._b)))
        painter.drawPath(self.shape())


class moInputFrame(QtWidgets.QGraphicsObject):
    InputSender=QtCore.pyqtSignal([int],[float],[str])
    R,G,B,J,C,H = range(6)
    def __init__(self,parent=None,width=24,maxletter=3,\
                 label='',labelwidth=80,labelheight=20,valuetype=0,limittype=int):
        super(moInputFrame,self).__init__(parent)
        self.__limittype=limittype
        self.__width=width+labelwidth
        self.__labelwidth=labelwidth
        self.__height=labelheight
        self.__valuetype = valuetype

        self._input=moInput(self,width,maxletter)
        self.__label=label
        self._input.setPos(labelwidth,0)
        self._input.InputFinish.connect(self.InputRespond)


    def boundingRect(self):
        return QtCore.QRectF(0,0,self.__width,self.__height)

    def paint(self,painter,option,widget):
        pen=QtGui.QPen(labelGetColor())
        painter.setPen(pen)
        painter.setFont(QtGui.QFont("sansserif",8))
        painter.drawText(0,0,self.__labelwidth,self.__height-1,\
                         QtCore.Qt.AlignBottom,self.__label)

    def setValue(self,value):
        self._input.setPlainText(str(value))

    @QtCore.pyqtSlot(str)
    def InputRespond(self,value):
        try:
            self.InputSender.emit(self.__limittype.__call__(value))
        except ValueError:
            self.InputSender.emit(0)
            #pass

    def responseInfo(self,value):
        #print value
        self.setValue(value[self.__valuetype])

class moExtensibleDragFrame(QtWidgets.QGraphicsObject):
    MinWidth,MinHeight=[168,300]
    def __init__(self,parent=None,scene=None,width=168,height=300,\
                 defaulttype =
                 moDragLine.Right|moDragLine.Bottom):
        super(moExtensibleDragFrame,self).__init__(parent)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges)
        self.__minwidth=self.MinWidth
        self.__minheight=self.MinHeight
        self.__width=width
        self.__height=height
        self.__draglines = []
        for i in [moDragLine.Left,moDragLine.Top,moDragLine.Right,moDragLine.Bottom]:
            if defaulttype&i:
                a=moDragLine(self,i)
                self.__draglines.append(a)
                a.LineDrag.connect(self.extendEvents)
        if scene:
            scene.addItem(self)

    def boundingRect(self):
        return QtCore.QRectF(0,0,self.__width,self.__height)

    def shape(self):
        path=QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        p=containerBorderGetColor()
        painter.setPen(p)
        painter.setBrush(panelGetColor())
        painter.drawRoundedRect(self.boundingRect(),4,4)
        #print 'painted extendee'

    @QtCore.pyqtSlot(int,object)
    def extendEvents(self,dpos,event):
        if dpos == moDragLine.Bottom:
            if self.scene():
                if event.scenePos().y()<self.scene().sceneRect().bottom():
                    self.__height +=event.scenePos().y()-event.lastScenePos().y()
            else:
                self.__height +=event.scenePos().y()-event.lastScenePos().y()
            if self.__height < self.__minheight:
                self.__height= self.__minheight
            elif self.scene() and self.pos().y()+\
                 self.__height>self.scene().sceneRect().bottom():
                self.__height= self.scene().sceneRect().bottom()-self.pos().y()
        elif dpos == moDragLine.Right:
            if self.scene():
                if event.scenePos().x()<self.scene().sceneRect().right():
                    self.__width += event.scenePos().x()-event.lastScenePos().x()
            else:
                self.__width += event.scenePos().x()-event.lastScenePos().x()
            if self.__width < self.__minwidth:
                self.__width=self.__minwidth
            elif self.scene() and self.pos().x()+\
                 self.__width>self.scene().sceneRect().right():
                self.__width= self.scene().sceneRect().right()-self.pos().x()
        for i in self.childItems():
            i.update()
        self.update()

    def itemChange(self,change,value):
        #print 'CHANGE EVENT OCCURED'
        if change == self.ItemPositionChange and self.scene():
            rect = self.boundingRect()
            newpos = value#.toPointF()
            scenerect = self.scene().sceneRect()
            if newpos.x()+rect.left() < scenerect.left():
                newpos.setX(scenerect.left()-rect.left())
            elif newpos.x()+rect.right()>=scenerect.right():
                newpos.setX(scenerect.right()-rect.right())
            if newpos.y()+rect.top()<scenerect.top():
                newpos.setY(scenerect.top()-rect.top())
            elif newpos.y()+rect.bottom()>=scenerect.bottom():
                newpos.setY(scenerect.bottom()-rect.bottom())
            if self.__width>scenerect.width():
                self.__width=scenerect.width()
            if self.__height>scenerect.height():
                self.__height=scenerect.height()
            for i in self.childItems():
                i.update()
            super(moExtensibleDragFrame,self).itemChange(change,value)
            return newpos
        return super(moExtensibleDragFrame,self).itemChange(change,value)

    def mousePressEvent(self,event):
        #print "FRAME PRESSED"
        super(moExtensibleDragFrame,self).mousePressEvent(event)


class autoTransformFrame(QtWidgets.QGraphicsObject):
    def __init__(self,parent=None,bindtop=6,bindleft=6,bindright=6,bindbottom=6,minwidth=30,minheight=30):
        super(autoTransformFrame,self).__init__(parent)
        self.__bindtop=bindtop
        self.__bindright=bindright
        self.__bindleft=bindleft
        self.__bindbottom=bindbottom
        self.__minwidth=minwidth
        self.__minheight=minheight
        self.drag = moDockLine(self,moDockLine.Right,[0,100],100,int,8,20)
        if self.parentItem():
            size=self.parentItem().boundingRect().size()
            self.__width=size.width()
            self.__height=size.height()
            self.setPos(self.__bindleft,self.__bindtop)
        self.setFlag(QtWidgets.QGraphicsItem.ItemClipsChildrenToShape)
        self.drag.DockValue.connect(self.dragFrame)
    def boundingRect(self):
        if self.parentItem():
            size=self.parentItem().boundingRect().size()
            width=size.width()-self.__bindleft-self.__bindright
            height=size.height()-self.__bindtop-self.__bindbottom
            return QtCore.QRectF(0,0,width,height)
        else:
            return QtCore.QRectF(0,0,self.__minwidth,self.__minheight)

    def shape(self):
        path = QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        self.drag.setCompoPos()
        painter.setPen(inputGetFrameBorder('hasfocus'))
        painter.setBrush(inputGetFrameBg('nofocus'))
        painter.drawRoundedRect(self.boundingRect(),2,2)

    @QtCore.pyqtSlot(int)
    def dragFrame(self,number):
        for i in self.childItems():
            if i.type()==moColorPieceGroupFrame.Type:
                length=i.boundingRect().size().height()-\
                        self.boundingRect().size().height()
                if length>0:
                    i.setPos(30,-((length+30)*(100-number)/100)+10)

class moColorPieceGroupFrame(QtWidgets.QGraphicsObject):
    Type = QtWidgets.QGraphicsItem.UserType + 515
    SelectedColor = QtCore.pyqtSignal(object,str,list)
    def __init__(self,parent=None):
        super(moColorPieceGroupFrame,self).__init__(parent)
        self.setPos(30,10)
        self.children = []
        self.selecteditem=[]
        self.eyelist = []
        self.__lastrotpos = 0
        self.__lastscapos = 0
        self.__lastx = 0
        self.__lasty = 0
        self.__lastz = 0
    def update(self):
        self.calculateAll()
        super(moColorPieceGroupFrame,self).update()

    def boundingRect(self):
        return self.childrenBoundingRect()

    def paint(self,painter,option,widget):
        #print 'jjj'
        pass
    def type(self):
        return moColorPieceGroupFrame.Type
    def calculateAll(self):
        for i in self.childItems():
            if i.type()==moLookEye.Type:
                self.scene().removeItem(i)
        pos=[0,0]
        if self.children:
            for u in self.children:
                #print u
                if u.type()==moColorPiece.Type or \
                   u.type()==moColorListPiece.Type:
                    v= moLookEye(self)
                    v.setPos(-24,pos[1]+1)
                    v.setState(u.getColorDisplay())
                    v.Clicked.connect(u.setColorDisplay)
                    self.eyelist.append(v)
                    u.setPos(pos[0],pos[1])
                    #u.update()
                    pos = [0,pos[1]+20]
                else:
                    abpos,pos = self.calculateEveryChild(pos,pos,True,u)

    def calculateEveryChild(self,abpos,nowerpos,heading,piece,bounding=None):
        x,y=0,0
        ax,ay = abpos
        childalign = 8
        piece.iconShow(False)
        piece.setPos(nowerpos[0],nowerpos[1])
        if not heading:
            x += 20
            if bounding:
                bounding.Clicked.connect(piece.setColorDisplay)
            if piece.type()==moColorGroupPiece.Type and piece._child:
                for i in piece._child:
                    bounding.Clicked.connect(i.setColorDisplay)
                    i.setVisible(False)

            return [[abpos[0]+x,abpos[1]],[nowerpos[0]+x,nowerpos[1]]]
        else:   #heading
            w = moLookEye(self)
            w.setPos(-24,abpos[1]+1)
            w.setState(piece.getColorDisplay())
            w.Clicked.connect(piece.setColorDisplay)
            if bounding:
                bounding.Clicked.connect(w.updateState)
            self.eyelist.append(w)
            piece.iconShow(True)
            if piece.getFold() == moColorGroupPiece.Fold:
                heading = heading & (not piece.getFold())
                if piece._child:
                    for j in piece._child:
                        j.setVisible(True)
                        if j.type()==moColorPiece.Type:
                            w.Clicked.connect(j.setColorDisplay)
                            x +=20
                            j.setPos(x,y)
                        else:
                            x += 20
                            ax =abpos[0]+x
                            ay =abpos[1]+y
                            abp,repos=self.calculateEveryChild([ax,ay],[x,y],heading,j,w)
                            x = repos[0]
                            y = repos[1]
                            x -=20
                return [[abpos[0],abpos[1]+20],[nowerpos[0],nowerpos[1]+20]]
            else:
                x = x+childalign
                heading = heading & (not piece.getFold())
                if piece._child:
                    for k in piece._child:

                        k.setVisible(True)
                        if k.type()==moColorPiece.Type:
                            y += 20
                            r = moLookEye(self)
                            r.setPos(-24,abpos[1]+1+y)
                            r.setState(k.getColorDisplay())
                            r.Clicked.connect(k.setColorDisplay)
                            w.Clicked.connect(r.updateState)
                            self.eyelist.append(r)
                            k.setPos(x,y)
                        else:
                            y+=20
                            ax =abpos[0]+x
                            ay =abpos[1]+y
                            abp,repos=self.calculateEveryChild([ax,ay],[x,y],heading,k,w)
                            x = repos[0]
                            y = repos[1]
                            y -= 20
                    ax,ay = abpos[0],abpos[1]+y+20
                return [[ax,ay],[nowerpos[0],nowerpos[1]+y+20]]

    def addChild(self,child):
        #print 'child added'
        if child.type()==moColorListPiece.Type:
            self.children.append(child)
            if child.parentItem() != self:
                child.setParentItem(self)
            child.Update.connect(self.update)
            child.Selected.connect(self.dealSelection)
        elif self.selecteditem and len(self.selecteditem)==1:
            if self.selecteditem[0] in self.children:
                if self.selecteditem[0].type()==moColorPiece.Type:
                    pos = self.children.index(self.selecteditem[0])
                    self.children.insert(pos,child)
                    child.setParentItem(self)
                    child.Update.connect(self.update)
                    child.Selected.connect(self.dealSelection)
                else:
                    try:
                        assert(self.selecteditem[0].type()==moColorGroupPiece.Type)
                        self.selecteditem[0].addChild(0,child)
                    except AssertionError:
                        print('errror')
                        return
            else:
                parent,pos = self.searchItemPos(self.selecteditem[0],self.children)
                if parent!=None :
                    parent.addChild(pos,child)
        else:
            #print child
            self.children.append(child)
            if child.parentItem() != self:
                child.setParentItem(self)
            child.update()
            child.Update.connect(self.update)
            child.Selected.connect(self.dealSelection)
        self.update()

  #  def ppp(self):
  #      print 'ppp'
    def searchItemPos(self,item,lists):
        if item in lists:
            if item.type()==moColorPiece.Type:
                pos = lists.index(item)+1
                parent = item.parentItem()
            else:
                try:
                    assert(item.type()==moColorGroupPiece.Type)
                    pos = 1
                    parent = item
                except AssertionError:
                    print('assertionerror')
                    return None,None
            return [parent,pos]
        else:
            g = [i for i in lists if i.type()==moColorGroupPiece.Type]
            if not g:
                return None,None
            else:
                for j in g:
                    parent,pos = self.searchItemPos(item,j.getChild())
                    if parent and pos:
                        return [parent,pos]
                    else:
                        pass
                return None,None

    def removeChild(self,child):
        if child in self.selecteditem:
            self.selecteditem.remove(child)
        if child in self.children:
            self.children.remove(child)
            if self.scene():
                self.scene().removeItem(child)
        else:
            child.parentItem().removeChild(child)
        self.update()

    def clearChild(self):
        while(self.children):
            self.removeChild(self.children[0])
    @QtCore.pyqtSlot(object,bool,bool)
    def dealSelection(self,selection,value,shifted):
        if self.selecteditem:
            if not shifted:
                for i in self.selecteditem:
                    i.setSelected(False)
                self.selecteditem=[]
            else:
                pass
        if value == True and selection:
            selection.setSelected(True)
            self.selecteditem.append(selection)
            if selection.type()!=moColorListPiece.Type:
                self.SelectedColor.emit(selection,"RGB",selection.getPieceColor())
        self.update()

    def dealSelectionChild(self,owner,selection):
        if owner._child:
            for i in owner._child:
                if i != selection:
                    i.setSelected(False)
                if i.type()==moColorGroupPiece.Type:
                    self.dealSelectionChild(i,selection)

    def changeSelectionColor(self,color):
        if len(self.selecteditem) == 1:
            #for i in self.selecteditem:
            i = self.selecteditem[0]
            if i.type() == moColorPiece.Type:
                i.setPieceColor(color[:3])
                i.setRenderPos(color[-3:])

    def setSelectionScale(self,scale):
        if self.selecteditem:
            for i in self.selecteditem:
                i.setScaleSize(scale)

    def addSelectionScale(self):
        if self.selecteditem:
            for i in self.selecteditem:
                scale = i.getScaleSize()
                if scale<50:
                    i.setScaleSize(scale+1)
            #if scale <10:
                #self.setSelectionScale(1+scale)

    def subSelectionScale(self):
        if self.selecteditem:
            for i in self.selecteditem:
                scale = i.getScaleSize()
                if scale>1:
                    self.setSelectionScale(-1+scale)

    def setSelectionRotate(self,rotation):
        rotvalue = rotation-self.__lastrotpos
        self.__lastrotpos=rotation
        if self.selecteditem:
            for i in self.selecteditem:
                i.posRotateBy(rotvalue)

    def addSelectionRotate(self):
        rotvalue = 5+self.__lastrotpos
        self.setSelectionRotate(rotvalue)

    def subSelectionRotate(self):
        rotvalue = -5+self.__lastrotpos
        self.setSelectionRotate(rotvalue)

    def setSelectionPosScale(self,size):
        #print 'size',size
        scasize = size-self.__lastscapos
        self.__lastscapos=size
        if self.selecteditem:
            for i in self.selecteditem:
                i.posScaleBy(scasize)

    def addSelectionPosScale(self):
        pos = 5+self.__lastscapos
        self.setSelectionPosScale(pos)
    def subSelectionPosScale(self):
        pos = -5+self.__lastscapos
        self.setSelectionPosScale(pos)

    def setSelectionMoveX(self,pos):
        length = pos - self.__lastx
        self.__lastx = pos
        if self.selecteditem:
            for i in self.selecteditem:
                i.posMoveByX(length)

    def addSelectionMoveX(self):
        length = 5 + self.__lastx
        self.setSelectionMoveX(length)

    def subSelectionMoveX(self):
        length = -5 + self.__lastx
        self.setSelectionMoveX(length)

    def setSelectionMoveY(self,pos):
        length = pos - self.__lasty
        self.__lasty = pos
        if self.selecteditem:
            for i in self.selecteditem:
                i.posMoveByY(length)

    def addSelectionMoveY(self):
        length = 5 + self.__lasty
        self.setSelectionMoveY(length)
    def subSelectionMoveY(self):
        length = -5 + self.__lasty
        self.setSelectionMoveY(length)

    def setSelectionMoveZ(self,pos):
        length = pos - self.__lastz
        self.__lastz = pos
        if self.selecteditem:
            for i in self.selecteditem:
                i.posMoveByZ(length)

    def addSelectionMoveZ(self):
        length = 5 + self.__lastz
        self.setSelectionMoveZ(length)

    def subSelectionMoveZ(self):
        length = -5 + self.__lastz
        self.setSelectionMoveZ(length)

    def mousePressEvent(self,event):
        self.dealSelection(None,False,False)
        super(moColorPieceGroupFrame,self).mousePressEvent(event)


class moColorManagerListOp(QtWidgets.QGraphicsObject):
    def __init__(self,parent=None,width=160):
        super(moColorManagerListOp,self).__init__(parent)
        self.addcolor = icons.moIconColorManagerAddColor(self)
        self.addlist  = icons.moIconColorManagerAddColorGroup(self)
        self.removeitem = icons.moIconColorManagerRemoveColor(self)
        self.explodeitem  = icons.moIconColorManagerExplode(self)
        self.reduceitems = icons.moIconColorManagerReduce(self)
        self.symmetry = icons.moIconColorManagerSymmetry(self)
        self._width = width
        self.addcolor.setPos(6,4)
        self.addlist.setPos(30,4)
        self.removeitem.setPos(54,4)
        self.explodeitem.setPos(78,4)
        self.reduceitems.setPos(102,4)
        self.symmetry.setPos(126,4)
    def boundingRect(self):
        return QtCore.QRectF(0,0,160,32)

    def paint(self,painter,option,widget):
        pass

    def mousePressEvent(self,event):          ##########test
        #print 'ListOp frame prd'
        super(moColorManagerListOp,self).mousePressEvent(event)

class moTwoDirectionDragFrame(QtWidgets.QGraphicsObject):
    def __init__(self,parent=None):
        super(moTwoDirectionDragFrame,self).__init__(parent)

    def boundingRect(self):
        return QtCore.QRectF(0,0,48,30)
    def paint(self,painter,option,widget):
        painter.setPen(panelGetBorder())
        painter.drawRect(self.boundingRect())

class moColorRotationFrame(moTwoDirectionDragFrame):
    RotateValue = QtCore.pyqtSignal(int)
    def __init__(self,parent=None):
        super(moColorRotationFrame,self).__init__(parent)
        self.rotatecw  = icons.moIconColorManagerCWRotate(self)
        self.rotateccw = icons.moIconColorManagerCCWRotate(self)
        self._dockbottom=moDockLine(self,moDockLine.Bottom,[0,360],180,int)
        self.rotatecw.setPos(0,0)
        self.rotateccw.setPos(24,0)
        self._dockbottom.DockValue.connect(self.RotateValue.emit)

class moColorScalePosFrame(moTwoDirectionDragFrame):
    ScaleValue = QtCore.pyqtSignal(int)
    def __init__(self,parent=None):
        super(moColorScalePosFrame,self).__init__(parent)
        self.scaleposup  = icons.moIconColorManagerScaleUpPos(self)
        self.scaleposdown = icons.moIconColorManagerScaleDownPos(self)
        self.scaleposup.setPos(0,0)
        self.scaleposdown.setPos(24,0)

        self._dockbottom=moDockLine(self,moDockLine.Bottom,[0,150],75,int)
        self._dockbottom.DockValue.connect(self.ScaleValue.emit)

class moColorScaleSizeFrame(moTwoDirectionDragFrame):
    ScaleSize = QtCore.pyqtSignal(int)
    def __init__(self,parent=None):
        super(moColorScaleSizeFrame,self).__init__(parent)
        self.scalesizeup  = icons.moIconColorManagerScaleUpSize(self)
        self.scalesizedown = icons.moIconColorManagerScaleDownSize(self)
        self._dockbottom=moDockLine(self,moDockLine.Bottom,[1,100],50,int)
        self._dockbottom.DockValue.connect(self.ScaleSize.emit)
        self.scalesizeup.setPos(0,0)
        self.scalesizedown.setPos(24,0)

class moColorManagerListTransform(QtWidgets.QGraphicsObject):
    def __init__(self,parent=None,width=180):
        super(moColorManagerListTransform,self).__init__(parent)
        self.rotate = moColorRotationFrame(self)
        self.scalepos = moColorScalePosFrame(self)
        self.scalesize= moColorScaleSizeFrame(self)
        self._width = width
        self.rotate.setPos(6,4)
        self.scalepos.setPos(60,4)
        self.scalesize.setPos(114,4)
        #self.setPos(0,0)
    def boundingRect(self):
        return QtCore.QRectF(0,0,180,32)

    def paint(self,painter,option,widget):
        pass

class moColorMoveXFrame(moTwoDirectionDragFrame):#QtWidgets.QGraphicsObject):
    MoveValue = QtCore.pyqtSignal(int)
    def __init__(self,parent=None):
        super(moColorMoveXFrame,self).__init__(parent)
        self.movexadd  = icons.moIconColorManagerMoveXAdd(self)
        self.movexsub = icons.moIconColorManagerMoveXSub(self)
        self._dockbottom=moDockLine(self,moDockLine.Bottom,[0,300],150,int)
        self.movexadd.setPos(0,0)
        self.movexsub.setPos(24,0)
        self._dockbottom.DockValue.connect(self.MoveValue.emit)

class moColorMoveYFrame(moTwoDirectionDragFrame):
    MoveValue = QtCore.pyqtSignal(int)
    def __init__(self,parent=None):
        super(moColorMoveYFrame,self).__init__(parent)
        self.moveyadd  = icons.moIconColorManagerMoveYAdd(self)
        self.moveysub = icons.moIconColorManagerMoveYSub(self)
        self._dockbottom=moDockLine(self,moDockLine.Bottom,[0,300],150,int)
        self.moveyadd.setPos(0,0)
        self.moveysub.setPos(24,0)
        self._dockbottom.DockValue.connect(self.MoveValue.emit)

class moColorMoveZFrame(moTwoDirectionDragFrame):
    MoveValue = QtCore.pyqtSignal(int)
    def __init__(self,parent=None):
        super(moColorMoveZFrame,self).__init__(parent)
        self.movezadd  = icons.moIconColorManagerMoveZAdd(self)
        self.movezsub = icons.moIconColorManagerMoveZSub(self)
        self._dockbottom=moDockLine(self,moDockLine.Bottom,[0,300],150,int)
        self.movezadd.setPos(0,0)
        self.movezsub.setPos(24,0)
        self._dockbottom.DockValue.connect(self.MoveValue.emit)

class moColorManagerListMove(QtWidgets.QGraphicsObject):
    def __init__(self,parent=None,width=180):
        super(moColorManagerListMove,self).__init__(parent)
        self.movex = moColorMoveXFrame(self)
        self.movey = moColorMoveYFrame(self)
        self.movez = moColorMoveZFrame(self)
        self.movex.setPos(6,4)
        self.movey.setPos(60,4)
        self.movez.setPos(114,4)
    def boundingRect(self):
        return QtCore.QRectF(0,0,180,32)

    def paint(self,painter,option,widget):
        pass


class moPicExtendFrame(QtWidgets.QGraphicsObject):
    MinWidth,MinHeight=[200,100]
    def __init__(self,pic,parent=None,scene=None,width=200,height=100,\
                 defaulttype =
                 moDragLine.Right|moDragLine.Bottom):
        super(moPicExtendFrame,self).__init__(parent)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges)
        self.__minwidth=self.MinWidth
        self.__minheight=self.MinHeight
        self.__width=width
        self.__height=height
        self.__draglines = []
        for i in [moDragLine.Left,moDragLine.Top,moDragLine.Right,moDragLine.Bottom]:
            if defaulttype&i:
                a=moDragLine(self,i)
                self.__draglines.append(a)
                a.LineDrag.connect(self.extendEvents)
        if scene:
            scene.addItem(self)

        self._pix = QtGui.QPixmap(pic).scaled(width,height,QtCore.Qt.KeepAspectRatio)
        #if self._pix.width()/self._pix.height() >= width/height:
        #    self._pix = self._pix.scaledToWidth(width)
        #else:
        #    self._pix = self._pix.scaledToHeight(height)
        self._piximage = QtWidgets.QGraphicsPixmapItem(self._pix,self)
        self._piximage.setPos(0,0)

    def boundingRect(self):
        return QtCore.QRectF(0,0,self.__width,self.__height)

    def shape(self):
        path=QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

    def paint(self,painter,option,widget):
        p=containerBorderGetColor()
        painter.setPen(p)
        painter.setBrush(panelGetColor())
        painter.drawRoundedRect(self.boundingRect(),4,4)
        #print 'painted extendee'

    @QtCore.pyqtSlot(int,object)
    def extendEvents(self,dpos,event):
        if dpos == moDragLine.Bottom:
            if self.scene():
                if event.scenePos().y()<self.scene().sceneRect().bottom():
                    self.__height +=event.scenePos().y()-event.lastScenePos().y()
            else:
                self.__height +=event.scenePos().y()-event.lastScenePos().y()
            if self.__height < self.__minheight:
                self.__height= self.__minheight
            elif self.scene() and self.pos().y()+\
                 self.__height>self.scene().sceneRect().bottom():
                self.__height= self.scene().sceneRect().bottom()-self.pos().y()
        elif dpos == moDragLine.Right:
            if self.scene():
                if event.scenePos().x()<self.scene().sceneRect().right():
                    self.__width += event.scenePos().x()-event.lastScenePos().x()
            else:
                self.__width += event.scenePos().x()-event.lastScenePos().x()
            if self.__width < self.__minwidth:
                self.__width=self.__minwidth
            elif self.scene() and self.pos().x()+\
                 self.__width>self.scene().sceneRect().right():
                self.__width= self.scene().sceneRect().right()-self.pos().x()
        for i in self.childItems():
            i.update()
        self.update()
        self._pix = self._pix.scaled(self.__width,self.__height,QtCore.Qt.KeepAspectRatio)
        #if self._pix.width()/self._pix.height() >= self.__width/self.__height:
        #    self._pix = self._pix.scaledToWidth(self.__width)
        #else:
        #    self._pix = self._pix.scaledToHeight(self.__height)
        self._piximage.setPixmap(self._pix) 

    def itemChange(self,change,value):
        #print 'CHANGE EVENT OCCURED'
        if change == self.ItemPositionChange and self.scene():
            rect = self.boundingRect()
            newpos = value#.toPointF()
            scenerect = self.scene().sceneRect()
            if newpos.x()+rect.left() < scenerect.left():
                newpos.setX(scenerect.left()-rect.left())
            elif newpos.x()+rect.right()>=scenerect.right():
                newpos.setX(scenerect.right()-rect.right())
            if newpos.y()+rect.top()<scenerect.top():
                newpos.setY(scenerect.top()-rect.top())
            elif newpos.y()+rect.bottom()>=scenerect.bottom():
                newpos.setY(scenerect.bottom()-rect.bottom())
            if self.__width>scenerect.width():
                self.__width=scenerect.width()
            if self.__height>scenerect.height():
                self.__height=scenerect.height()
            for i in self.childItems():
                i.update()
            super(moPicExtendFrame,self).itemChange(change,value)
            return newpos
        return super(moPicExtendFrame,self).itemChange(change,value)

    def mousePressEvent(self,event):
        #print "FRAME PRESSED"
        super(moPicExtendFrame,self).mousePressEvent(event)

