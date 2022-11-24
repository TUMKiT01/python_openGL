from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
name = b'Transformation_chapter'
import numpy as np
import math
xmin, ymin = 0.5, 0.5
xmax, ymax = 1.5, 1.5
left, right, bottom, top = -5., 5., -5., 5.
tx, ty = 0., 0.
cx, cy = 0., 0.
sc, theta, step = 1., 0., 0.1
o = np.array([[xmin, ymin, 1], [xmin, ymax, 1], [xmax, ymax, 1], [xmax, ymin, 1]], dtype=float)
T = np.zeros([3,3],  dtype = float) 

def init():
    global cx,cy
    sx, sy = 0., 0.
    for p in o:
        sx =sx + p[0]
        sy =sy + p[1]
    cx = sx/len(o)
    cy = sy/len(o)

def myPushMatrix():
    global T
    T =  np.identity(3, dtype = float)

def myRotatef(theta):
    global T
    R =  np.identity(3, dtype = float)
    ang = (theta*np.pi)/180
    R[0,0] = math.cos(ang)
    R[0,1] = math.sin(ang)
    R[1,0] = -math.sin(ang)
    R[1,1] = math.cos(ang)
    T = np.matmul(R, T)
    
def myTranslatef(tx,ty):
    global T
    Ts =  np.identity(3, dtype = float)
    Ts[2,0] = tx
    Ts[2,1] = ty
    T = np.matmul(Ts, T)
    
def myScalef(sx,sy):
    global T
    Ts =  np.identity(3, dtype = float)
    Ts[0,0] = sx
    Ts[1,1] = sy
    T = np.matmul(Ts, T)    

def myPopMatrix():
    global T
    T = np.zeros([3,3],  dtype = float) 

def InitGL():
    glClearColor(1.,1.,1.,0.)
    glColor3f(0.0, 0.0, 0.0)
    glPolygonMode( GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    myPushMatrix()
    myTranslatef(cx, cy)
    myRotatef(theta)
    myScalef(sc,sc)
    myTranslatef(-cx, -cy)
    obj = np.matmul(o, T)
    glBegin(GL_QUADS)
    for p in obj:
        glVertex2f(p[0], p[1])
    glEnd()
    myPopMatrix()

    glFlush()
    return

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)
    init()
    InitGL()
    glutDisplayFunc(display)
    glutKeyboardFunc(On_keyboard)

    glutMainLoop()
    return

def On_keyboard(key, x, y):
    global tx, ty, sc, theta
    while True:
        if key == b'\x1b':
            sys.exit()
        if key == b'l':
            tx = tx - 0.1       
            break
        if key == b'r':
            tx = tx + 0.1       
            break
        if key == b'b':
            ty = ty - 0.1         
            break
        if key == b't':
            ty = ty + 0.1            
            break
        if key == b'i':
            sc = sc + 0.1            
            break
        if key == b'd':
            sc = sc - 0.1            
            break
        if key == b'R':        
            theta = theta + 1.0
            break

        break
    glutPostRedisplay()



if __name__ == '__main__': main()
