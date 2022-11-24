from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import sys
import math

width, height = 500, 500
xe,ye,ze = 0., 0., 5.
theta = 0
def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5, 5, -5, 5, -5, 5)
    glEnable(GL_DEPTH_TEST)


def DrawGL():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Q = -(theta * math.pi)/180
    gluLookAt(xe*math.cos(Q) + ze*math.sin(Q), ye,  -xe*math.sin(Q) + ze*math.cos(Q), 0, 0, 0, 0, 1, 0)
   
    
    glColor4f(0.3,0.8,0.0,0.9)
    glPushMatrix()
    glutSolidSphere(2.0, 60, 60)
    glPopMatrix()
 
    glColor4f(0.8,0.6,0.1,0.7)
    glPushMatrix()
    glTranslatef(0.0, 0.0, -4.0)
    glutSolidSphere(3.2, 60, 60)
    glPopMatrix()
    
    glColor4f(0.,0.3,0.6,0.7)       
    glPushMatrix()
    glTranslatef(0.0, 0.0, 2.0)
    glutSolidSphere(1.0, 60, 60)
    glPopMatrix()
    
 
    
    glutSwapBuffers()

def On_reshape(w, h):
    global width, height
    width, height = w, h

def MyIdle():
    global theta
    theta = theta + 0.5
    if (theta >= 360.0) :
        theta = 0
    glutPostRedisplay()



def main():
    glutInit(sys.argv)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow(b'cube')
    InitGL()
    glutDisplayFunc(DrawGL)
    glutIdleFunc(MyIdle)
    glutReshapeFunc(On_reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()
