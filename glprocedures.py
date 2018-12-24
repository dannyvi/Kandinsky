#! /usr/local/bin/python3.4
# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from basefunctionalpart import *

def eyePoint2xyz(point,r):
    longt = 2*np.pi*point[0]/360.0
    lat  = 2*np.pi*point[1]/360.0
    x=r*np.cos(longt)*np.cos(lat)
    y=r*np.sin(lat)
    z=r*np.cos(lat)*np.sin(longt)
    return [x,y,z]


def initGL(color):
    glClearColor(color[0],color[1],color[2],1.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_FLAT)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_POLYGON_SMOOTH)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_ALPHA_TEST)
    glEnable(GL_CULL_FACE)
    glShadeModel(GL_FLAT)
    glHint(GL_POINT_SMOOTH_HINT,GL_NICEST)
    glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)
    #glAlphaFunc(GL_ALWAYS,0)
    #glEnable(GL_NORMALIZE)

    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)

def disableGL():
    glDisable(GL_MULTISAMPLE)
    glDisable(GL_POINT_SMOOTH)
    glDisable(GL_POLYGON_SMOOTH)
    glDisable(GL_LINE_SMOOTH)
    glDisable(GL_DEPTH_TEST)
    #glDisable(GL_ALPHA_TEST)
    glDisable(GL_CULL_FACE)
    #glDisable(GL_NORMALIZE)

def gltSolidCone(rad):
    #glVertex3f(x/2.0,-x/(2.0*(3**0.5)),-x/(2.0*(3**0.5)))
    #glVertex3f(0,x*2/(3**0.5),-x/(2.0*(3**0.5)))
    #glVertex3f(-x/2.0,-x/(2.0*(3**0.5)),-x/(2.0*(3**0.5)))

    #glVertex3f(x/2.0,-x/(2.0*(3**0.5)),-x/(2.0*(3**0.5)))
    #glVertex3f(-x/2.0,-x/(2.0*(3**0.5)),-x/(2.0*(3**0.5)))
    #glVertex3f(0,0,x*2.0/(3**0.5))

    #glVertex3f(-x/2.0,-x/(2.0*(3**0.5)),-x/(2.0*(3**0.5)))
    #glVertex3f(0,x*2/(3**0.5),-x/(2.0*(3**0.5)))
    #glVertex3f(0,0,x*2.0/(3**0.5))

    #glVertex3f(0,x*2/(3**0.5),-x/(2.0*(3**0.5)))
    #glVertex3f(x/2.0,-x/(2.0*(3**0.5)),-x/(2.0*(3**0.5)))
    #glVertex3f(0,0,x*2.0/(3**0.5))


    step_z   = np.pi/15
    step_xy  = 2 * np.pi / 15

    angle_z  = 0.0
    angle_xy = 0.0
    x = [0,0,0,0]
    y = [0,0,0,0]
    z = [0,0,0,0]
    glBegin(GL_QUADS)

    for i in range(15):
        angle_z = i * step_z

        for j in range(15):
            angle_xy = j * step_xy

            x[0] = rad * np.sin(angle_z) * np.cos(angle_xy)
            y[0] = rad * np.sin(angle_z) * np.sin(angle_xy)
            z[0] = rad * np.cos(angle_z)

            x[1] = rad * np.sin(angle_z + step_z) * np.cos(angle_xy)
            y[1] = rad * np.sin(angle_z + step_z) * np.sin(angle_xy)
            z[1] = rad * np.cos(angle_z + step_z)

            x[2] = rad * np.sin(angle_z + step_z) * np.cos(angle_xy + step_xy)
            y[2] = rad * np.sin(angle_z + step_z) * np.sin(angle_xy + step_xy)
            z[2] = rad * np.cos(angle_z + step_z)

            x[3] = rad * np.sin(angle_z) * np.cos(angle_xy + step_xy)
            y[3] = rad * np.sin(angle_z) * np.sin(angle_xy + step_xy)
            z[3] = rad * np.cos(angle_z)

            for k in range(4):
                glVertex3f(x[k],y[k],z[k])

    glEnd()


def gltSolidCube(x):
    u = x/2.0
    #glShadeModel(GL_FLAT)
    glBegin(GL_QUADS)
    #glNormal3f(0.0,0.0,1.0)
    glVertex3f(u,u,u)
    glVertex3f(-u,u,u)
    glVertex3f(-u,-u,u)
    glVertex3f(u,-u,u)

    #glNormal3f(0.0,0.0,-1.0)
    glVertex3f(u,-u,-u)
    glVertex3f(-u,-u,-u)
    glVertex3f(-u,u,-u)
    glVertex3f(u,u,-u)

    #glNormal3f(0.0,1.0,0.0)
    glVertex3f(u,u,-u)
    glVertex3f(-u,u,-u)
    glVertex3f(-u,u,u)
    glVertex3f(u,u,u)

    #glNormal3f(0.0,-1.0,0.0)
    glVertex3f(u,-u,u)
    glVertex3f(-u,-u,u)
    glVertex3f(-u,-u,-u)
    glVertex3f(u,-u,-u)

    #glNormal3f(-1.0,0.0,0.0)
    glVertex3f(u,u,-u)
    glVertex3f(u,u,u)
    glVertex3f(u,-u,u)
    glVertex3f(u,-u,-u)

    #glNormal3f(1.0,0.0,0.0)
    glVertex3f(-u,-u,-u)
    glVertex3f(-u,-u,u)
    glVertex3f(-u,u,u)
    glVertex3f(-u,u,-u)
    glEnd()

def buildLists():
    #u = x/2.0
    bx = glGenLists(1)
    #glShadeModel(GL_FLAT)
    glNewList(bx,GL_COMPILE)
    glBegin(GL_QUADS)
    #glNormal3f(0.0,0.0,1.0)
    glVertex3f(0.5,0.5,0.5)
    glVertex3f(-0.5,0.5,0.5)
    glVertex3f(-0.5,-0.5,0.5)
    glVertex3f(0.5,-0.5,0.5)

    #glNormal3f(0.0,0.0,-1.0)
    glVertex3f(0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5,0.5,-0.5)
    glVertex3f(0.5,0.5,-0.5)

    #glNormal3f(0.0,1.0,0.0)
    glVertex3f(0.5,0.5,-0.5)
    glVertex3f(-0.5,0.5,-0.5)
    glVertex3f(-0.5,0.5,0.5)
    glVertex3f(0.5,0.5,0.5)

    #glNormal3f(0.0,-1.0,0.0)
    glVertex3f(0.5,-0.5,0.5)
    glVertex3f(-0.5,-0.5,0.5)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(0.5,-0.5,-0.5)

    #glNormal3f(-1.0,0.0,0.0)
    glVertex3f(0.5,0.5,-0.5)
    glVertex3f(0.5,0.5,0.5)
    glVertex3f(0.5,-0.5,0.5)
    glVertex3f(0.5,-0.5,-0.5)

    #glNormal3f(1.0,0.0,0.0)
    glVertex3f(-0.5,-0.5,-0.5)
    glVertex3f(-0.5,-0.5,0.5)
    glVertex3f(-0.5,0.5,0.5)
    glVertex3f(-0.5,0.5,-0.5)
    glEnd()
    glEndList()
    return bx
#box = buildLists()

def listRender(colorlists,unitsize,unitdistance,degree):
    box = buildLists()
    def render1cube1(m0,m1,m2,m3,m4,m5,m6):
        glLoadIdentity()
        glRotatef(m0*1.0,0.0,1.0,0.0)
        if m3==0 and m4==0 and m5==0:
            m1=0
            m2=0
        glTranslatef(unitdistance*m2*degree/100.0,-0.8+unitdistance*m1*degree/100.0,0.0)
        glColor3ub(m3,m4,m5)
        glScalef(unitsize*m6,unitsize*m6,unitsize*m6)
        glCallList(box)
        #gltSolidCube(unitsize*m6)
        return True
    ufunc_render = np.frompyfunc(render1cube1,7,1)
    if not colorlists:
        return
    for i in colorlists:
        if i.type()==moColorGroupPiece.Type:
            if i.getColorDisplay() and (not i.getPieceColor()==[0,0,0]):
                glLoadIdentity()
                glTranslatef(0.0,-0.8,0.0)
                position = i.getRenderPos()
                color = i.getPieceColor()
                glColor3ub(color[0],color[1],color[2])
                glRotatef(position[0],0,1,0)
                glTranslatef(unitdistance*position[2]*degree/100.0,unitdistance*position[1]*degree/100.0,0)
                gltSolidCone(unitsize * i.getScaleSize())
                listRender(i.getChild(),unitsize,unitdistance,degree)
        elif i.type()==moColorListPiece.Type:
            if i.getColorDisplay():
                RGB = i.getPieceColor()
                HJCS = i.getHjcs()
                R = RGB[:,0]
                G = RGB[:,1]
                B = RGB[:,2]
                H = HJCS[:,0]
                J = HJCS[:,1]
                C = HJCS[:,2]
                S = HJCS[:,3]
                ufunc_render(H,J,C,R,G,B,S)

        else:  #i is colorpiece
            if i.getColorDisplay() and (not i.getPieceColor()==[0,0,0]):
                glLoadIdentity()
                glTranslatef(0.0,-0.8,0.0)
                position = i.getRenderPos()
                color = i.getPieceColor()
                #print color[0]
                glColor3ub(int(color[0])  ,int(color[1]),int(color[2]))
                glRotatef(position[0],0,1,0)
                glTranslatef(unitdistance*position[2]*degree/100.0,unitdistance*position[1]*degree/100.0,0)
                temp = i.getScaleSize() * unitsize
                glScalef(temp,temp,temp)
                glCallList(box)
                #gltSolidCube(unitsize * i.getScaleSize())
#"""
def perspectiveRender(mode,degree,unitsize,unitdistance,\
                      cube,colorpan,angledeg,plate):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
    glColor4f(0.5,0.5,0.5,0.3)
    glDrawLine3f([1.5,-0.1,0],[-1.5,-0.1,0])
    glDrawLine3f([0,0.6,0],[0,-0.8,0])
    glDrawLine3f([0,-0.1,1.5],[0,-0.1,-1.5])
    glDisable(GL_BLEND)
    glTranslatef(0.0,-0.8,0.0)
    box = buildLists()
    def render1cube1(m0,m1,m2,m3,m4,m5):
        glLoadIdentity()
        glRotatef(m0*1.0,0.0,1.0,0.0)
        glTranslatef(unitdistance*m2*degree/100.0,-0.8+unitdistance*m1*degree/100.0,0.0)
        glScalef(unitsize,unitsize,unitsize)
        glColor3ub(int(m3),int(m4),int(m5))
        glCallList(box)
        #gltSolidCube(unitsize)
        return True
    ufunc_render = np.frompyfunc(render1cube1,6,1)
    if mode == 'overall':
        for i in range(degree+1):
            glColor3f(i*1.0/degree,\
                      i*1.0/degree,i*1.0/degree)
            gltSolidCube(unitsize)
            glTranslatef(0.0,unitdistance,0.0)
        ufunc_render(cube[:,0],cube[:,1],cube[:,2],cube[:,3].astype('uint8'),cube[:,4].astype('uint8'),cube[:,5].astype('uint8'))

    elif mode == 'panel':
        glRotatef(colorpan*360/angledeg,0,1,0)
        for i in range(degree+1):
            glColor3f(i*1.0/degree,\
                      i*1.0/degree,i*1.0/degree)
            gltSolidCube(unitsize)
            glTranslatef(0.0,unitdistance,0.0)
        glLoadIdentity()

        opsite = colorpan + angledeg/2
        if opsite>=angledeg:
            opsite -= angledeg
        panel = np.array(list(filter(lambda x: abs(x[0]-colorpan*360/angledeg)<0.1 or\
                       abs(x[0]-opsite*360/angledeg)<0.1,cube)))
        ufunc_render(panel[:,0],panel[:,1],panel[:,2],panel[:,3],panel[:,4],panel[:,5])

    elif mode == 'plate':
        glTranslatef(0.0,unitdistance*plate,0.0)
        glColor3f(plate*1.0/degree,plate*1.0/degree,plate*1.0/degree)
        gltSolidCube(unitsize)
        plate = np.array(list(filter(lambda x: abs(x[1]-plate*100.0/degree)<0.1 ,cube)))
        ufunc_render(plate[:,0],plate[:,1],plate[:,2],plate[:,3],plate[:,4],plate[:,5])

def glDrawLine3f(point1,point2):
    glLoadIdentity()
    glBegin(GL_LINES)
    a1,b1,c1=point1
    a2,b2,c2=point2
    glVertex3f(a1,b1,c1)
    glVertex3f(a2,b2,c2)
    glEnd()
#"""

def resizeGL(w,h):
    if h==0:h=1
    glViewport(0,0,int(w),int(h))
    #Relook(winproportion)

def reLook(siz,perspectiveangle,eyepoint,eyeradius):
    w = int(siz.width())
    h = int(siz.height())
    if h==0:
        h=1
    proportion=w*1.0/h
    X,Y,Z=eyePoint2xyz(eyepoint,eyeradius)
    glPushMatrix()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glTranslatef(-0.15,0.08,0)
    ######glOrtho(-0.8*perspectiveangle,1.2*perspectiveangle,-1.0,1.0,-3.0,3.0)
    #########glLoadIdentity()
    gluPerspective(perspectiveangle,\
                   proportion,0.3,10.0)
    gluLookAt(X,Y,Z, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    #######  print GL_MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

def CoerceNum(var,num,lower,higher):
    var+=num
    while var<lower or var>=higher:
        if var<lower:
            var+=higher-lower
        elif var>=higher:
            var-=higher-lower
    return var
def StayLimit(var,num,lower,higher):
    var+=num
    if var<=lower:
        var=lower
    elif var>=higher:
        var=higher
    return var


if __name__ == '__main__':
    import cProfile
    from colorconvert import makeCam02Cube
    from OpenGL.GLUT import *
    cube = makeCam02Cube(20,20,40)
    import sys
    #mode=
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow("Bounce")
    initGL([0,0,0])

    cProfile.run('perspectiveRender("overall",20,0.03,0.06,cube,5,40,5)')
    glutMainLoop()
    sys.exit()
