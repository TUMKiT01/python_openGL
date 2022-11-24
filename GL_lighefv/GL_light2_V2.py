from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math
r, g, b = 1.0, 1.0, 1.0
x0,y0,z0 = 10, 0, 0
x1,y1,z1 = -10, 0, 0
w = 0.8
name = b'Lighting'
theta, sign = 0, 1


def setCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10, 0,0,0, 0,1,0)

def setLight():
    glEnable(GL_LIGHTING)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [r, g, 0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [r*0.7, g*0.7, 0, 1.0])    

    glLightfv(GL_LIGHT1, GL_DIFFUSE, [r, 0, b, 1.0])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [r*0.7, 0, b*0.7, 1.0])  


    #glMaterialfv(GL_FRONT,GL_DIFFUSE,[0, g, 0, 1.0])    
    #glMaterialfv(GL_FRONT,GL_AMBIENT,[0, g*0.25, 0, 0.0])
    


def init():
    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    setCamera()
    setLight()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(On_keyboard)
    glutIdleFunc(MyIdle)
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Q = (theta * math.pi)/180
    glLightfv(GL_LIGHT0, GL_POSITION, [x0*math.cos(Q) + z0*math.sin(Q), y0, -x0*math.sin(Q) + z0*math.cos(Q),0])
    glLightfv(GL_LIGHT1, GL_POSITION, [x1*math.cos(Q) + z1*math.sin(Q), y1, -x1*math.sin(Q) + z1*math.cos(Q),0])
    glColor3f(1.,1., 0.)
    glPushMatrix()
    glutSolidSphere(2,80,80)
    glPopMatrix()
    glutSwapBuffers()
    return

def On_keyboard(key, x, y):
    while True:
        if key == b'\x1b':
            sys.exit() 
        if key == b'l':
            glEnable(GL_LIGHT0)
            glDisable(GL_LIGHT1)                   
            break
        if key == b'r':
            glEnable(GL_LIGHT1)
            glDisable(GL_LIGHT0)                   
            break
        if key == b'b':
            glEnable(GL_LIGHT0)
            glEnable(GL_LIGHT1)
            break
        if key == b't':
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            break
        break
    glutPostRedisplay()

def MyIdle():
    global theta, sign
    theta = theta + (0.5*sign)
    if ((theta >= 360.0) | (theta <= 0.0)):
        sign = sign*(-1)
    glutPostRedisplay()

if __name__ == '__main__': main()
