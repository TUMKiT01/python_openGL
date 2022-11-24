from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = b'ball_glut'

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)
    init()
  
    glutDisplayFunc(display)
    glutMainLoop()
    return

def init():  
    glClearColor(0.,0.,0.,1.)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-4,4,-4,4,-4,4)
    #gluPerspective(60.,1.,1.,120.)
    #glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,3, 0,0,2, 0,1,0)  # 
  
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    ##glTranslatef(0.0,0.0,0.5)

    glPushMatrix()
    glColor4f(1.,0.,0.,0.5)
    glTranslatef(0,0,-3)
    glutSolidCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glColor4f(0.,1.,0.,0.5)
    glTranslatef(-3,0,0)
    glutSolidCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glColor4f(0.,0.,1.,0.5)
    glTranslatef(3,0,0)
    glutSolidCube(2.0)
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
