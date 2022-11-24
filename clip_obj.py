from platform import java_ver
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import numpy as np


# Window
width, height = 500, 500
SizeWindowMax = (width + height) / 2

# Size
Xaxis = 200.0
Yaxis = 100.0

XMin = -Xaxis
XMax = Xaxis
YMin = -Yaxis
YMax = Yaxis
Center_XY = (XMax - XMin) / 2.0

# Side
Side = ['Botton','Top','Left','Right']

# Use to Encode function
CodeWinLeft    = 0x01;
CodeWinRight   = 0x02;
CodeWinBottom  = 0x04;
CodeWinTop     = 0x08;

# Show Line
Show = True

# Move Step Window
Step = 2.0

# mouse
MouseX, MouseY = 0.0, 0.0
MouseState = True

# Obj
p = []
p_tmp = []

def main():
    #glut support GL
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b'Clip Object| Buttom(b) Top(t) Right(r) Left(l) ')
    init()

    glutDisplayFunc(DrawObject)
    glutKeyboardFunc(KeyBoardKey)
    glutSpecialFunc(SpecialKey)
    glutMouseFunc(MouseAssign)
    # glutPassiveMotionFunc(PassiveMouseMotion)
    glutMainLoop()

def init():
    glClearColor(0.0,0.0,0.2,1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-SizeWindowMax,SizeWindowMax,-SizeWindowMax,SizeWindowMax)
    SetPoint()

def SetPoint():
    global p
    p = [
            [-110.,-150.], 
            [-200.,150.],
            [200.,150.],
            [110.,-150.],
            [0.,80.]
        ]

def DrawObject():
    glClear(GL_COLOR_BUFFER_BIT)  #
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Window
    glPushMatrix()
    glColor3f(0.0, 0.8, 0.0)
    glBegin(GL_POLYGON)   # glbegin สร้างเมตริกขึ้นมา  (วาดได้หลายเหลียม)  
    glVertex2f(XMin,YMin)
    glVertex2f(XMin,YMax)
    glVertex2f(XMax,YMax)
    glVertex2f(XMax,YMin)
    glEnd()# rbพอจบการทำงานให้เอา  obj * T 
    glPopMatrix()

    # Draw ObjectLine to cliping
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for i in p:
        glVertex2f(i[0],i[1])
    glEnd()
    glPopMatrix()

    # Force update of screen
    glFlush()

def KeyBoardKey(Key,X,Y):
    global XMin,XMax,YMin,YMax,Center_XY
    print(Key)
    step = 2.0

    # Enter
    if(Key.lower() == b'\r'): 
        ClipObj()

    # Buttom
    if(Key.lower() == b'b') or (Key == b'\xd4'):
        ClipObj(0)

    # Top
    if(Key.lower() == b't') or (Key == b'\xd0'):
        ClipObj(1)

    # Left
    if(Key.lower() == b'l') or (Key == b'\xca'):
        ClipObj(3)

    # Right
    if(Key.lower() == b'r') or (Key == b'\xbe'):
        ClipObj(2)

    # +
    if(Key.lower() == b'+'):
        if((XMax - XMin) < (SizeWindowMax * 2)):
            XMin -= step
            XMax += step
            YMin -= step
            YMax += step
            Center_XY = (XMax - XMin) / 2.0
    # +
    if(Key.lower() == b'-'):
        if((XMax - XMin) > (5.0)):
            XMin += step
            XMax -= step
            YMin += step
            YMax -= step
            Center_XY = (XMax - XMin) / 2.0

    #print('     [{}]\n[{}]  [{}]\n    [{}]\n'.format(YMax,XMin,XMax,YMin))

    # Post Redisplay
    glutPostRedisplay()

def SpecialKey(Key, X, Y):
    global XMin,XMax,YMin,YMax, Step

    # Down
    if(Key == GLUT_KEY_DOWN):
        if(YMin > -SizeWindowMax):
            YMin -= Step
            YMax -= Step

    # Up
    if(Key == GLUT_KEY_UP):
        if(YMax < SizeWindowMax):
            YMin += Step
            YMax += Step

    # Left
    if(Key == GLUT_KEY_LEFT):
        if(XMin > -SizeWindowMax):
            XMin -= Step
            XMax -= Step

    # Right
    if(Key == GLUT_KEY_RIGHT):
        if(XMax < SizeWindowMax):
            XMin += Step
            XMax += Step


    #print('     [{}]\n[{}]  [{}]\n    [{}]\n'.format(YMax,XMin,XMax,YMin))

    # Post Redisplay
    glutPostRedisplay()

def MouseAssign(button, state, x, y):
    global MouseState, MouseX, MouseY

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            ClipObj()
    elif button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            p = []
            SetPoint()

    MouseState = GLUT_ENTERED if (state) == GLUT_ENTERED else GLUT_LEFT
    MouseX = (2.0 * x) - SizeWindowMax
    MouseY = SizeWindowMax - (2.0 * y)

def PassiveMouseMotion(x, y):
    global MouseState, MouseX, MouseY, Xaxis, Yaxis, XMin, XMax, YMin, YMax

    if MouseState:
        # X
        if (((MouseX - Center_XY) > -SizeWindowMax) and ((MouseX + Center_XY) < SizeWindowMax)):
            XMin = MouseX - Center_XY
            XMax = MouseX + Center_XY

        # Y
        if (((MouseY - Center_XY) > -SizeWindowMax) and ((MouseY + Center_XY) < SizeWindowMax)):
            YMin = MouseY - Center_XY
            YMax = MouseY + Center_XY
        
        MouseX = (2.0 * x) - SizeWindowMax
        MouseY = SizeWindowMax - (2.0 * y)
    glutPostRedisplay()

def ClipObj(pos = None):
    global p, p_tmp, XMin,XMax,YMin,YMax,Center_XY
    
    if pos == None:
        for s in range(len(Side)):
            p_tmp = []
            for i in range(len(p)):
                if i < (len(p)-1):
                    ClipSide(p[i],p[i + 1], s)
                else:
                    ClipSide(p[i],p[0], s)
            p = []
            p = p_tmp
    else:
        # for s in range(len(Side)):
        p_tmp = []
        for i in range(len(p)):
            if i < (len(p)-1):
                ClipSide(p[i],p[i + 1], pos)
            else:
                ClipSide(p[i],p[0], pos)
        p = []
        p = p_tmp

    print(p)

def ClipSide(s,p,side):#   
    global XMin,XMax,YMin,YMax, p_tmp
    x, y = 0.0, 0.0

    dy = p[1] - s[1]
    dx = p[0] - s[0] if p[0] != s[0] else 0.000000000001
    k = dy / dx

    # left
    if side == 3:
        if p[0] >= XMin: #เช็คว่า p inside?
            if s[0] < XMin:
                y = p[1] + (XMin - p[0]) * k
                x = XMin
                p_tmp.append([x,y])
            p_tmp.append(p)
        else:
            if s[0] > XMin:#เช็ค ห
                y = s[1] + (XMin - s[0]) * k
                x = XMin
                p_tmp.append([x,y])

    # right
    if side == 2:
        if p[0] <= XMax:
            if s[0] > XMax:
                y = p[1] + (XMax - p[0]) * k
                x = XMax
                p_tmp.append([x,y])
            p_tmp.append(p)
        else:
            if s[0] < XMax:
                y = s[1] + (XMax - s[0]) * k
                x = XMax
                p_tmp.append([x,y])

    # buttom
    if side == 0:
        if p[1] >= YMin:
            if s[1] < YMin:
                x = p[0] + (YMin - p[1]) / k
                y = YMin
                p_tmp.append([x,y])
            p_tmp.append(p)
        else:
            if s[1] > YMin:
                x = s[0] + (YMin - s[1]) / k
                y = YMin
                p_tmp.append([x,y])

    # top
    if side == 1:
        if p[1] <= YMax:
            if s[1] > YMax:
                x = p[0] + (YMax - p[1]) / k
                y = YMax
                p_tmp.append([x,y])
            p_tmp.append(p)
        else:
            if s[1] < YMax:
                x = s[0] + (YMax - s[1]) / k
                y = YMax
                p_tmp.append([x,y])

if __name__ == '__main__': 
    main()