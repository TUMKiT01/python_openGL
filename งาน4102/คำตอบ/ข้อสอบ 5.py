from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys


width, height = 500, 500
pos = 8
xe,ye,ze = 0., 0., pos
view, blend = True, True
space = 13
theta, sign = 0.0, 1.0
def main():
    glutInit(sys.argv)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow(b'cube')
    InitGL()
    glutDisplayFunc(DrawGL)
    glutKeyboardFunc(On_keyboard)
    glutReshapeFunc(On_reshape)
    glutIdleFunc(MyIdle)
    glutMainLoop()

def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def DrawGL():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    SetView()
    SetBlend()
    #SetFrame()
    
    glColor4f(1,0,0,0)
    glPushMatrix()
    glutSolidSphere(2.0, 60, 60)
    glPopMatrix()
 
    glColor4f(0,1,0,0)
    glPushMatrix()
    glTranslatef(0.0, 0.0, -6.0)
    glutSolidSphere(3.2, 60, 60)
    glPopMatrix()
    
    glColor4f(0.,0.0,1,0)       
    glPushMatrix()
    glTranslatef(0.0, 0.0, 5.0)
    glutSolidSphere(0.5, 60, 60)
    glPopMatrix()
    glutSwapBuffers()

def SetView():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if view:
        glFrustum(-5, 5, -5, 5, 3.0, 30)
        #gluPerspective(90., 1., 0.5, 80.)
    else:
        gluPerspective(90., 1., 3, 30.)
        #glOrtho(-space, space, -space, space, -space, space)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Q = (theta * math.pi)/180
    gluLookAt(xe*math.cos(Q) + ze*math.sin(Q), ye,  -xe*math.sin(Q) + ze*math.cos(Q), 0, 0, 0, 0, 1, 0)
    #gluLookAt(1, 0, 0, 0, 0, 1, 0)

def SetFrame():
    glPushMatrix()
    glColor4f(0.5, 0.5, 0.5, 0.5)
    glBegin(GL_LINES)
    glVertex3f(-space,0., 0.)
    glVertex3f( space, 0., 0.)
    glVertex3f( 0., -space, 0.)
    glVertex3f( 0.,  space, 0.)
    glEnd()
    glPopMatrix()

def SetBlend():
    if blend:
        glDisable(GL_BLEND)
        
    else:
        glEnable(GL_BLEND)

def On_reshape(w, h):
    global width, height
    width, height = w, h

def On_keyboard(key, x, y):
    global view 
    global blend
       
    while True:
        if key == b'\x1b':
            sys.exit()
        if key == b'v':
            view = not view
            break
        if key == b'b':
            blend = not blend
        break            
    glutPostRedisplay()

def On_reshape(w, h):
    global width, height
    width, height = w, h

def MyIdle():
    global theta, sign
    theta = theta + (0.02*sign)
    glutPostRedisplay()

if __name__ == "__main__":
    main()
