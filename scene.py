#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-

from PyQt5 import QtGui
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from panels import *
from glprocedures import *
from basefunctionalpart import *
from colorconvertc import makeCam02Cube
from npcolorconvert import npjch2rgb
from icons import moIconSetBgColor
import numpy as np
import pickle #cPickle as pickle
import colorindex
from imageanal import imageAnalyze
from dynamiccolor import moColor
#import time

class moScene(QtWidgets.QGraphicsScene):

    def __init__(self,parent = None,degrees=10,angledeg=40):
        super(moScene,self).__init__(parent)
        self.setSceneRect(0,0,930,600)
        #self.setSortCacheEnabled(True)
        self.is_Dragging=False
        self._piximage=None
        self._piximagename=None

        #self.setBG=True

        self.degrees = degrees
        self.angledeg = angledeg
        self.colorcube = colorindex.colors
        self.camcube = makeCam02Cube(self.degrees,self.degrees,self.angledeg)
        self.colorsys = moColor
        self.eyepoint,self.eyeradius=[90,0],6.0
        self.baseunitsize = 0.06/self.degrees
        self.baseunitscale = 4
        self.unitdistance = 1.4/self.degrees

        self.listunitsize = 0.06/self.degrees
        self.listunitscale = 6

        self.colorplate = 5
        self.colorpan   = 0
        self.mode = 'overall'
        self.submode = True

        self.modepanel=moModePanel(self)
        self.scenefuncpanel=moSceneFuncPanel(self)
        self.filemanager = moFileManagerPanel(self)
        self.coloreditpanel=moColorGroupEditPanel(parent=None,scene=self)
        self.helpinfo = moPanelHelpInfo(self)
        self.setbgcolor = moIconSetBgColor()
        self.addItem(self.setbgcolor)
        #self.cc2 = moColorGroupEditPanel(scene=self)

        self.openfilename=''
        f = open('res/pathhistory','r')
        try:
            dirname = pickle.load(f)
        except:
            dirname = ''
        self.currentdir=dirname
        f2 = open('res/anahistory','r')
        try:
            anadirname = pickle.load(f2)
        except:
            anadirname = ''
        self.anadirname=anadirname
        self.modepanel.MainModeExchange.connect(self.setMode)
        self.modepanel.SubModeExchange.connect(self.setSubMode)

        #self.coloreditpanel.colorinfo.Broadcast.connect(self.modifyBackgroundColor)

        self.scenefuncpanel.icons[moSceneFuncPanel.SwitchUp].setEnabled(False)
        self.scenefuncpanel.icons[moSceneFuncPanel.SwitchDown].setEnabled(False)

        self.scenefuncpanel.icons[moSceneFuncPanel.MoreColor].Onclicked.connect(self.increaseModuleColor)
        self.scenefuncpanel.icons[moSceneFuncPanel.LessColor].Onclicked.connect(self.decreaseModuleColor)
        self.scenefuncpanel.icons[moSceneFuncPanel.BgLighter].Onclicked.connect(self.modifyBackgroundColor)
        self.scenefuncpanel.icons[moSceneFuncPanel.BgDarker].Onclicked.connect(self.modifyBackgroundColor)
        self.scenefuncpanel.icons[moSceneFuncPanel.TurnLeft].Onclicked.connect(self.turnHorizontalWrapper)
        self.scenefuncpanel.icons[moSceneFuncPanel.TurnRight].Onclicked.connect(self.turnHorizontalWrapper)
        self.scenefuncpanel.icons[moSceneFuncPanel.TurnUp].Onclicked.connect(self.turnVerticalWrapper)
        self.scenefuncpanel.icons[moSceneFuncPanel.TurnDown].Onclicked.connect(self.turnVerticalWrapper)
        self.scenefuncpanel.icons[moSceneFuncPanel.ScaleIncrease].Onclicked.connect(self.baseUnitSizeWrapper)
        self.scenefuncpanel.icons[moSceneFuncPanel.ScaleDecrease].Onclicked.connect(self.baseUnitSizeWrapper)
        self.scenefuncpanel.icons[moSceneFuncPanel.SwitchUp].Onclicked.connect(self.setPlateOrPanel)
        self.scenefuncpanel.icons[moSceneFuncPanel.SwitchDown].Onclicked.connect(self.setPlateOrPanel)
        self.scenefuncpanel.icons[moSceneFuncPanel.ViewNear].Onclicked.connect(self.setEyeRadius)
        self.scenefuncpanel.icons[moSceneFuncPanel.ViewFar].Onclicked.connect(self.setEyeRadius)

        self.filemanager.icons[moFileManagerPanel.New].Onclicked.connect(self.newFile)
        self.filemanager.icons[moFileManagerPanel.Open].Onclicked.connect(self.openFile)
        self.filemanager.icons[moFileManagerPanel.Save].Onclicked.connect(self.saveFile)
        self.filemanager.icons[moFileManagerPanel.SaveAs].Onclicked.connect(self.saveFileAs)
        self.filemanager.icons[moFileManagerPanel.Import].Onclicked.connect(self.importAnalPicture)



    def updateSize(self,event):
        size = self.sceneRect().size()
        pos = self.coloreditpanel.pos()
        colorpos =[self.sceneRect().size().width()-pos.x(),self.sceneRect().size().height()-pos.y()]
        self.setSceneRect(0,0,event.size().width(),event.size().height())
        self.modepanel.setPos(8+32+32,(self.sceneRect().size().height()-40))
        self.scenefuncpanel.setPos(self.modepanel.boundingRect().size().width()+20+32+32,(self.sceneRect().size().height()-40))
        self.filemanager.setPos(self.modepanel.boundingRect().size().width()+self.scenefuncpanel.boundingRect().size().width()+32+32+32,self.sceneRect().size().height()-40)
        self.coloreditpanel.setPos(event.size().width()-colorpos[0],\
                                   event.size().height()-colorpos[1])
        self.helpinfo.setPos(8,(self.sceneRect().size().height()-32))
        self.setbgcolor.setPos(40,(self.sceneRect().size().height()-32))
        resizeGL(size.width(),size.height())
        self.update()

    def drawBackground(self,painter,rect):
        #f True:#not self.setBG:
        color = self.colorsys.getBaseColorF()
        #else:
        #    color = self.coloreditpanel.colorinfo.getRGB()
        #    color = map(lambda x:float(x/255.0),color)
        #self.colorsys.resetColor(map(lambda x:x+int(n),self.colorsys.getBaseColor()))
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.beginNativePainting()
        initGL(color)
        reLook(self.sceneRect().size(),33,self.eyepoint,self.eyeradius)
        if self.baseunitscale>0 and not self.submode:
            perspectiveRender(self.mode,10,\
                          self.baseunitsize*self.baseunitscale,\
                          0.14,self.colorcube,\
                          self.colorpan,self.angledeg,self.colorplate)
        elif self.submode:
            perspectiveRender(self.mode,self.degrees,\
                          self.baseunitsize*self.baseunitscale,\
                          self.unitdistance,self.camcube,\
                          self.colorpan,self.angledeg,self.colorplate)
            if self.coloreditpanel.colorlists.children:
                listRender(self.coloreditpanel.colorlists.children,\
                           self.listunitsize*self.listunitscale,self.unitdistance,self.degrees)
        disableGL()
        painter.endNativePainting()

    def keyPressEvent(self,event):
        if not self.focusItem() or self.focusItem().type() != moInput.Type:
            self.dispatchKey(event)
        super(moScene,self).keyPressEvent(event)

    def dispatchKey(self,event):
        if event.key()==QtCore.Qt.Key_A:
            self.modifyBackgroundColor(None,25)
        elif event.key()==QtCore.Qt.Key_Z:
            self.modifyBackgroundColor(None,-25)
        elif event.key()==QtCore.Qt.Key_Left:
            self.turnHorizontalWrapper(None,-10)
        elif event.key()==QtCore.Qt.Key_Right:
            self.turnHorizontalWrapper(None,10)
        elif event.key()==QtCore.Qt.Key_Up:
            self.turnVerticalWrapper(None,15)
        elif event.key()==QtCore.Qt.Key_Down:
            self.turnVerticalWrapper(None,-15)
        elif event.key()==QtCore.Qt.Key_Comma:
            self.baseUnitSizeWrapper(None,-1)
        elif event.key()==QtCore.Qt.Key_Period:
            self.baseUnitSizeWrapper(None,1)
        elif event.key()==QtCore.Qt.Key_PageUp:
            self.setPlateOrPanel(None,1)
        elif event.key()==QtCore.Qt.Key_PageDown:
            self.setPlateOrPanel(None,-1)
        elif event.key()==QtCore.Qt.Key_X:
            self.setMode('overall')
        elif event.key()==QtCore.Qt.Key_C:
            self.setMode('panel')
        elif event.key()==QtCore.Qt.Key_V:
            self.setMode('plate')
        elif event.key()==QtCore.Qt.Key_BracketLeft:
            self.setEyeRadius(None,0.5)
        elif event.key()==QtCore.Qt.Key_BracketRight:
            self.setEyeRadius(None,-0.5)
        elif event.key()==QtCore.Qt.Key_K:
            self.coloreditpanel.colorlists.addSelectionScale()
        elif event.key()==QtCore.Qt.Key_L:
            self.coloreditpanel.colorlists.subSelectionScale()
        elif event.key()==QtCore.Qt.Key_Semicolon:
            self.setPlateOrPanel(0,-1)

        elif event.key()==QtCore.Qt.Key_Apostrophe:
            self.setPlateOrPanel(0,1)
        elif event.key()==QtCore.Qt.Key_S:
            self.decreaseModuleColor()
        elif event.key()==QtCore.Qt.Key_D:
            self.increaseModuleColor()

        self.update()


    def modifyBackgroundColor(self,wrap,n):
        self.colorsys.resetColor(list(map(lambda x:x+int(n),self.colorsys.getBaseColor())))
        self.update()

    def resetBackgroundColor(self,color):
        self.colorsys.resetColor(color)
        self.update()

    def turnHorizontalWrapper(self,wrap,info):
        self.eyepoint[0]=CoerceNum(self.eyepoint[0],int(info),0,360)

    def turnVerticalWrapper(self,wrap,info):
        self.eyepoint[1]=StayLimit(self.eyepoint[1],int(info),-90,90)

    def baseUnitSizeWrapper(self,wrap,info):
        self.baseunitscale=StayLimit(self.baseunitscale,int(info),0,20)

    def setMode(self,info):
        self.mode = info
        if self.mode == 'overall':
            self.scenefuncpanel.icons[moSceneFuncPanel.SwitchUp].setEnabled(False)
            self.scenefuncpanel.icons[moSceneFuncPanel.SwitchDown].setEnabled(False)
        else:
            self.scenefuncpanel.icons[moSceneFuncPanel.SwitchUp].setEnabled(True)
            self.scenefuncpanel.icons[moSceneFuncPanel.SwitchDown].setEnabled(True)
        self.modepanel.mainmodeframe.setSelection(info)

    def setSubMode(self):
        self.submode = not self.submode

    def setPlateOrPanel(self,wrap,info):
        if self.mode == 'plate':
            self.colorplate =StayLimit(self.colorplate,int(info),1,self.degrees-1)
        if self.mode == 'panel':
            self.colorpan = CoerceNum(self.colorpan,int(info),0,self.angledeg)

    def setEyeRadius(self,wrap,info):
        self.eyeradius = StayLimit(self.eyeradius,float(info),2,14)


    def mousePressEvent(self,event):
        self.is_Dragging=False
        a = QtGui.QTransform()
        if self.itemAt(event.scenePos(),a) is None and \
           event.button() & QtCore.Qt.LeftButton :
            self.is_Dragging=True
        else:
            super(moScene,self).mousePressEvent(event)

    def mouseMoveEvent(self,event):
        if self.is_Dragging==True:
            self.onDragPerspective(event)
            self.update()
        super(moScene,self).mouseMoveEvent(event)
#
    def mouseReleaseEvent(self,event):
        super(moScene,self).mouseReleaseEvent(event)
        self.is_Dragging=False
        a = QtGui.QTransform()
        if ( (self.itemAt(event.scenePos(),a)==self._piximage) or \
             (self.itemAt(event.scenePos(),a) is None)) and \
           abs(event.scenePos().x()-event.buttonDownScenePos(QtCore.Qt.LeftButton).x())<5 and \
           abs(event.scenePos().y()-event.buttonDownScenePos(QtCore.Qt.LeftButton).y())<5:
            pos = event.scenePos()
            self.getColorAndLink(pos)

    def onDragPerspective(self,event):
        self.eyepoint[0] = CoerceNum(self.eyepoint[0],event.scenePos().x()-event.lastScenePos().x(),0,360)
        self.eyepoint[1] = StayLimit(self.eyepoint[1],event.scenePos().y()-event.lastScenePos().y(),-90,90)
    def getColorAndLink(self,pos):
            x,y = int(pos.x()),int(self.sceneRect().size().height()-pos.y())
            value = glReadPixels(x,y,1,1,GL_RGB,GL_UNSIGNED_BYTE,outputType=None)
            value =  value[0][0].tolist()
            bg = self.colorsys.getBaseColor()[:-1]
            if self.setbgcolor.testSelected():#False:
                self.resetBackgroundColor(value)
                #pass
            elif value != bg or (not (bg[0]==bg[1] and bg[1]==bg[2])):#self.colorsys.getBaseColor()[:-1] or ():
                self.coloreditpanel.colorinfo.colorInfoCenter(None,"RGB",value)

    def getRGBFromPanel(self):
        return self.coloreditpanel.colorinfo.getRGB()

    def setRGBToPanel(self,rgb):
        self.coloreditpanel.colorinfo.setRGB(rgb)

    def showTips(self,tips):
        self.helpinfo.assignText(tips)
        #print(tips)

    def cancelTips(self):
        self.helpinfo.cancelText()

    def increaseModuleColor(self):
        self.degrees+=2
        if self.degrees>40:
            self.degrees=40
        self.baseunitsize = 0.06/self.degrees
        self.unitdistance = 1.4/self.degrees
        self.listunitsize = 0.06/self.degrees
        self.camcube = makeCam02Cube(self.degrees,self.degrees,self.angledeg)

    def decreaseModuleColor(self):
        self.degrees-=2
        if self.degrees<10:
            self.degrees=10
        self.baseunitsize = 0.06/self.degrees
        self.unitdistance = 1.4/self.degrees
        self.listunitsize = 0.06/self.degrees
        self.camcube = makeCam02Cube(self.degrees,self.degrees,self.angledeg)

    def newFile(self):
        self.openfilename=''
        self.coloreditpanel.colorlists.clearChild()
        if self._piximage and self._piximage.scene()==self:
            self.removeItem(self._piximage)
            self._piximage=None
            self._piximagename=None
    def openFile(self):
        if self.currentdir:
            path = self.currentdir
        else:
            path = unicode(os.path.abspath(os.curdir))
        self.openingfile=QtWidgets.QFileDialog(directory = path)
        self.openingfile.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        self.openingfile.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        self.openingfile.accepted.connect(self.openFileAccepted)
        self.openingfile.show()

    def openFileAccepted(self):
        self.openfilename = self.openingfile.selectedFiles()[0]
        #print(self.openfilename)
        self.currentdir = self.openingfile.directory().absolutePath()
        f = open('res/pathhistory','wb')
        pickle.dump(self.currentdir,f)
        f.close()
        try:
            if self.openfilename.split('.')[-1] != 'cpn':
                raise ValueError(u'无效文件类型')
            inputdata = open(self.openfilename,'rb')
            ss = pickle.load(inputdata)
            s1 = ss[0]
            s  = ss[1]
            inputdata.close()
            self.coloreditpanel.colorlists.clearChild()
            if self._piximage and self._piximage.scene()==self:
                self.removeItem(self._piximage)
                self._piximage=None
                self._piximagename=None
            assert(type(s)==list)
            for i in s:
                assert(i.type()==moColorPiece.Type or i.type()==moColorGroupPiece.Type or i.type()==moColorListPiece.Type)
                args = i.__getstate__()
                i.__setstate__(args)
                self.coloreditpanel.colorlists.addChild(i)
            if s1:
                self._piximagename = s1
                self._piximage = moPicExtendFrame(self._piximagename) #QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(self._piximagename).scaledToWidth(200))#,scene=self)
                #self._piximage.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
                self._piximage.setPos(0,0)

        except AssertionError as e:
            a=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'',u'无效数据')
            a.exec_()
        except AttributeError as e:
            a=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'',u'无效文件')
            print(e)
            a.exec_()
        except ValueError as e:
            a=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'',u'无效文件类型')
            a.exec_()

    def saveFile(self):
        if self.openfilename:
            try:
                if self.openfilename.split('.')[-1] != 'cpn':
                    raise NameError
                output = open(self.openfilename,'wb')
                data = self.coloreditpanel.colorlists.children
                if not data:
                    raise ValueError
                data = [self._piximagename,data]
                pickle.dump(data,output,-1)
                output.close()
            except NameError:
                a=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'',u'无效文件')
                a.exec_()
            except ValueError:
                a=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'',u'没有色块')
                a.exec_()
        else:
            self.saveFileAs()

    def saveFileAs(self):
        if self.currentdir:
            path = self.currentdir
        else:
            path = unicode(os.path.abspath(os.curdir))
        self._savingfile = QtWidgets.QFileDialog(directory=path)
        #self._savingfile = QtWidgets.QFileDialog()
        self._savingfile.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        #self._savingfile.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self._savingfile.accepted.connect(self.saveFileAccepted)
        #self._savingfile.show()
        self._savingfile.exec_()

    def saveFileAccepted(self):
        self.openfilename = self._savingfile.selectedFiles()[0]
        self.currentdir = self._savingfile.directory().absolutePath()
        f = open('res/pathhistory','wb')
        pickle.dump(self.currentdir,f)
        f.close()
        try:
            if self.openfilename.split('.')[-1] != 'cpn':
                raise NameError
            output = open(self.openfilename,'wb')
            data = self.coloreditpanel.colorlists.children
            if not data:
                raise ValueError
            data = [self._piximagename,data]
            pickle.dump(data,output,-1)
            output.close()
        except NameError:
            a=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'',u'无效文件')
            a.exec_()
        except ValueError:
            a=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'',u'没有色块')
            a.exec_()


    def importAnalPicture(self):
        if self.anadirname:
            path = self.anadirname
        else:
            path = unicode(os.path.abspath(os.curdir))
        self.anafile=QtWidgets.QFileDialog(directory = path)
        self.anafile.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        self.anafile.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        self.anafile.accepted.connect(self.openAnaAccepted)
        self.anafile.show()

    def openAnaAccepted(self):
        self.anadirname = self.anafile.directory().absolutePath()
        f = open('res/anahistory','wb')
        pickle.dump(self.anadirname,f)
        f.close()
        if self._piximage and self._piximage.scene()==self:
            self.removeItem(self._piximage)
            self._piximage=None
            self._piximagename=None
        self._piximagename = unicode(self.anafile.selectedFiles()[0])
        self._pix = QtGui.QPixmap(self._piximagename)
        self._piximage = QtWidgets.QGraphicsPixmapItem(self._pix.scaledToWidth(200))#,scene=self)
        # moPicExtendFrame(self._piximagename) 
        #self._piximage = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap(self._piximagename).scaledToWidth(200) )
        self.addItem(self._piximage)
                #,scene=self)
        self._piximage.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self._piximage.setPos(0,0)

        colorjchnum= imageAnalyze(self._piximagename)
        #print(colorjchnum)
        H = colorjchnum[:,0]*9
        J = colorjchnum[:,1]*5
        C = colorjchnum[:,2]*5
        S = colorjchnum[:,3]
        self.coloreditpanel.colorlists.clearChild()

        colorrgbnum = npjch2rgb(np.array([J,C,H]).T)
        R = colorrgbnum[:,0]
        G = colorrgbnum[:,1]
        B = colorrgbnum[:,2]

        child = moColorListPiece(color=colorrgbnum,hjcs=np.array([H,J,C,S]).T)

        self.coloreditpanel.colorlists.addChild(child)
