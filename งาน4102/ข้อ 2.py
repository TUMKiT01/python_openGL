from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import sys

flag = True


def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-0.5,6,-0.5,6)
    
def setView():
    glPushMatrix()
    glBegin(GL_LINES)
    glColor4f(0, 1, 0,1)
    glVertex2f(0,0)
    glVertex2f(0,6)

    glColor4f(1, 0, 0,1)
    glVertex2f(0,0)
    glVertex2f(0,-0.5)

    glColor4f(0, 0, 1,1)
    glVertex2f(0,0)
    glVertex2f(6,0)

    glColor4f(0, 1, 1,1)
    glVertex2f(0,0)
    glVertex2f(-0.5,0)

    glEnd()
    glPopMatrix()

    glPushMatrix()
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex(1,1)
    glVertex(2,1)
    glVertex(3,1)
    glVertex(4,1)
    glVertex(5,1)
    glVertex(6,1)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex(1,1)
    glVertex(1,2)
    glVertex(1,3)
    glVertex(1,4)
    glVertex(1,5)
    glVertex(1,6)
    glEnd()
    glPopMatrix()
    glFlush()
    return

def DrawGL():
    glClear(GL_COLOR_BUFFER_BIT)
    setView()
    if flag == True:
        glPushMatrix()
        glBegin(GL_TRIANGLES)
        glColor4f(0, 1, 0,1)
        glVertex2f( 4, 3 )
        glVertex2f( 4, 1 )
        glVertex2f( 6, 1 )
        glEnd()
        glPopMatrix()
    else:
        glPushMatrix()
        glScalef(1.5,1,0)
        glTranslatef(-3.33,5,0)
        glScalef(1,-1,0)
        glBegin(GL_TRIANGLES)
        glColor4f(1, 0, 0,1)
        glVertex2f( 4, 3 )
        glVertex2f( 4, 1 )
        glVertex2f( 6, 1 )
        glEnd()
        glPopMatrix()
    
    glFlush()
    return 

def onKeyboard(key , x ,y):
	global flag 
	print(key)
	glutPostRedisplay()
	if flag == True:
		flag = False
	else:
		flag = True
    



def main():
    glutInit(sys.argv)
    glutCreateWindow(b'Homework1/7')
    InitGL()
    glutInitWindowSize(900,800)
    glutDisplayFunc(DrawGL)
    glutKeyboardFunc(onKeyboard)
    glutMainLoop()


if __name__ == "__main__":
    main()
