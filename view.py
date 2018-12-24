#!/usr/local/bin/python3.4
#-*-coding:utf-8-*-


import sys
from PyQt5 import QtCore,QtWidgets,QtOpenGL
from scene import *


class moView(QtWidgets.QGraphicsView):
    def __init__(self):
        super(moView,self).__init__()
        self.move(20,20)
        self.resize(930,600)
        self.setMinimumSize(930,500)
        self.setWindowTitle("color manager")
        sc = moScene()
        self.setScene(sc)
        self.scene().setSceneRect(0,0,930,600)
        widget = QtOpenGL.QGLWidget(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers|QtOpenGL.QGL.Rgba))
        widget.makeCurrent()
        self.setViewport(widget)
        self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate);
        self.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.setViewportUpdateMode(QtWidgets.QGraphicsView.FullViewportUpdate)
        #self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        #self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)

    def resizeEvent(self,event):
        self.setSceneRect(QtCore.QRectF(0,0,event.size().width(),\
                                                    event.size().height()))
        self.scene().updateSize(event)
        super(moView,self).resizeEvent(event)

    def keyPressEvent(self,event):
        if self.scene().focusItem() is None:
            self.dispatchKey(event)
        super(moView,self).keyPressEvent(event)

    def dispatchKey(self,event):
        if event.key()==QtCore.Qt.Key_Q:
            sys.exit()
        elif event.key()==QtCore.Qt.Key_F:
            if self.isFullScreen():
                self.showNormal()
                self.setSceneRect(self.sceneRect())
            else:
                self.showFullScreen()
                self.setSceneRect(self.sceneRect())
        else:
            pass

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    v=moView()
    v.show()
    #import cProfile
    #cube = makeCam02Cube(20,20,40)
    #cProfile.run('perspectiveRender("overall",20,0.03,0.06,cube,5,40,5)')
    sys.exit(app.exec_())
