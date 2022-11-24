from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math
name = b'ball_glut'
sz = 5
xe, ye, ze = 0, 0, 6
theta, sign = 0., 1. 

diff = [1.,1.,1.,0.7]
f0_diff = [0.7, 0.,0.,0.7]
f1_diff = [0.,0.7,0.,0.7]
f2_diff = [0.,0.,0.7,0.7]


amb  = [0.9,0.9,0.9,1.0]
f0_amb = [0.3,0.,0.,0.7]
f1_amb = [0.,0.3,0.,0.7]
f2_amb = [0.,0.,0.3,0.8]


spec = [1., 1., 1., 1.]
f0_spec = [1.,0.,0.,0.7]
f1_spec = [0.,1.,0.,0.7]
f2_spec = [0.,0.,1.,0.7]

fsh = 16

pos  = [0., 0., 20., 0.]
flag = True
def init():
    glClearColor(0.,0.,0.,0.)
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70., 1., 5., 20.)
    #glOrtho(-5, 5,-5,5,-5 ,7)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0,GL_DIFFUSE,diff)
    glLightfv(GL_LIGHT0,GL_AMBIENT,amb)
    glLightfv(GL_LIGHT0,GL_SPECULAR,spec)
    
    return

def mytime():
    global theta, sign
    theta = theta + (0.1 * sign)
    if ((theta >= 360.0) | (theta <= 0.0)):
        sign = sign * (-1)
    glutPostRedisplay()

def On_keyboard(key, x, y):
    global flag
    while True:
        print('55')
        if key == b'\x1b':
            sys.exit()
        if key == b't':
            flag = not flag             
            break
        break
    glutPostRedisplay()
    return

def framework():
    
    if flag:      
        glEnable(GL_LIGHTING)
    else:
        glDisable(GL_LIGHTING)

    glMaterialf(GL_FRONT,GL_SHININESS, fsh)

    glPushMatrix()
    glRotatef(theta,0,1,0)
    glLightfv(GL_LIGHT0,GL_POSITION,pos)
    glPopMatrix()
  
    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_DIFFUSE, f0_diff)
    glMaterialfv(GL_FRONT, GL_AMBIENT, f0_amb)
    glMaterialfv(GL_FRONT, GL_SPECULAR, f0_spec)
    glColor3f(1.,0.,0.)
    glutSolidCube(2.0)
    glPopMatrix()

    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_DIFFUSE, f1_diff)
    glMaterialfv(GL_FRONT, GL_AMBIENT, f1_amb)
    glMaterialfv(GL_FRONT, GL_SPECULAR, f1_spec)
    glColor3f(0.,1.,0.)
    glTranslatef(-3,0,-3)
    glutSolidCube(2.0)
    glPopMatrix()

    
    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_DIFFUSE, f2_diff)
    glMaterialfv(GL_FRONT, GL_AMBIENT, f2_amb)
    glMaterialfv(GL_FRONT, GL_SPECULAR, f2_spec)
    glColor3f(0.,0.,1.)
    glTranslatef(3,0,3)
    glutSolidCube(2.0)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, 200, 200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
    framework()

    glViewport(0, 200, 200, 200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, -10, 0, 0, 0, 0, 1, 0)
    framework()

    glViewport(200, 200, 200, 200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10, 0, 0, 0, 0, 0, 0, 1, 0)
    framework()

    glViewport(200, 0, 200, 200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 10, 0, 0, 0, 0, 1, 0, 0)
    framework()



    glFlush()
    return

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)
    init()
    glutDisplayFunc(display)    
    glutKeyboardFunc(On_keyboard)
    glutIdleFunc(mytime)
    glutMainLoop()
    return



if __name__ == '__main__': 
    main()