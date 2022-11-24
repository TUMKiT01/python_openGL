from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
name = b'Transformation_chapter'
import numpy as np

xmin, ymin = 2, -1
xmax, ymax = 4, 1
left, right, bottom, top = -5., 5., -5., 5.
tx, ty = 0., 0.
sc = 1.
obj = np.array([[xmin, ymin, 1], [xmin, ymax, 1], [xmax, ymax, 1], [xmax, ymin, 1]], dtype=float)
flag = True
def InitGL():
    glClearColor(1.,1.,1.,1.)
    glColor4f(0.0, 0.0, 1.0,0.0)
    #glPolygonMode( GL_FRONT_AND_BACK, GL_LINE)
    #glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    gluOrtho2D(left, right, bottom, top)
    #############################################################################
def SetFrame():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor4f(0.0, 0.0, 1.0,0.0)
    
    glPointSize(5.0)
    glBegin(GL_LINES)
    glColor4f(0.0, 0.0,0.0,0.0)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
       
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    SetFrame()
    
    glPushMatrix()
    glTranslatef(tx, ty, 0)
    glScalef(sc,sc,0)
    
    glBegin(GL_QUADS)
    glColor4f(0.0, 0.5,  0.8,0.0)
    for p in obj:
        glVertex2f(p[0], p[1])
    glEnd()
     
    ###############################

    if(flag==True):
             glBegin(GL_TRIANGLES)
             glColor4f(1.0, 0.0, 0.0,1.0)
             glVertex2f( 1.0,0.0 )
             glVertex2f( 2.0,1.0  )
             glVertex2f( 2, -1.0 )
             glEnd()

    else:             
            glBegin(GL_TRIANGLES)
            glColor4f(1.0, 0.0, 0.0,1.0)
            glVertex2f( 3.0,-2.0 )
            glVertex2f( 2, -1.0  )
            glVertex2f( 4, -1.0 )
            glEnd()
 

    glFlush()
    return

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutCreateWindow(b'HW1')
    InitGL()
    glutDisplayFunc(display)
    glutKeyboardFunc(On_keyboard)   
    glutMainLoop()
    return




def On_keyboard(key, x, y):
    global tx, ty, sc
    global flag
    while True:
        if key == b' ':
            sc = sc -0.5 
            tx = tx -1.5
            ty = ty -1.5 
            flag = not flag
            break 
    print(flag)
    glutPostRedisplay()

if __name__ == '__main__': main()
