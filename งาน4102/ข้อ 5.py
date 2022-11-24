from turtle import window_height
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
view = '1'
name = b'HW5'
width =500
height =500
shine =100
theta, sign = 0,1
lightPosition0 = [50.0, 10.0, 0.0, 10.0]
lightPosition1 = [-50.0, -20.0, 50.0, 10.0]
lightPosition2 = [50.0, 50.0, -20.0, 10.0]
lightPosition3 = [-50.0, 50.0, -20.0, 10.0]



diffuse = [1.0,1.0,1.0,1.0]
specular = [1.0,1.0,1.0,1.0]
ambient = [1.0,1.0,1.0,1.0]
specularOFmaterial = [1.0,1.0,1.0,1.0]
diffuseOFmaterial = [1.0,1.0,1.0,1.0]
ambientOFmaterial = [0.0,1.0,0.5,1.0]



def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    light()

def light():
    glMaterialfv(GL_FRONT , GL_DIFFUSE,diffuseOFmaterial)
    glMaterialfv(GL_FRONT , GL_AMBIENT,ambientOFmaterial)
    glMaterialfv(GL_FRONT , GL_SPECULAR,specularOFmaterial)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, diffuse)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, diffuse)
    
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(100.0,1.0,0.5,100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,15,0,1,0,0,1,0)
    if view == '1':
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition0)
    if view == '2':
        glLightfv(GL_LIGHT1, GL_POSITION, lightPosition1)
    if view == '3':
        glLightfv(GL_LIGHT2, GL_POSITION, lightPosition2)
    if view == '4':
        glLightfv(GL_LIGHT3, GL_POSITION, lightPosition3)
      
    glMaterialfv(GL_FRONT,GL_SHININESS, shine)
    rec = 10
    glPushMatrix()
    glRotatef(-50, 1, 0, 0)
    glRotatef(50, 0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-rec, rec)
    glVertex2f(-rec, -rec)
    glVertex2f(rec, -rec)
    glVertex2f(rec, rec)
    glEnd()
    
    glMaterialfv(GL_FRONT,GL_SHININESS, shine)
    rec = 10
    glPushMatrix()
    glRotatef(0, 1, 0, -50)
    glRotatef(0, 0, 1, 50)
    glBegin(GL_POLYGON)
    glVertex2f(-rec, rec)
    glVertex2f(-rec, -rec)
    glVertex2f(rec, -rec)
    glVertex2f(rec, rec)
    glEnd()

    glPopMatrix()
    glutSwapBuffers()
    return 
    
    
    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB| GLUT_DEPTH)
    glutInitWindowSize(width,height)
    glutInitWindowPosition(width,height)
    glutInitWindowPosition(width,height)
    glutCreateWindow(name)
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(on_keyboard)
    glutMainLoop()
    return
    
    
    
    
def on_keyboard(key, x, y):
    global view
    while True:
        if key == b'1':
            view = '1'
            glEnable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT2)
            glDisable(GL_LIGHT3)
            break

        if key == b'2':
            view = '2'
            glDisable(GL_LIGHT0)
            glEnable(GL_LIGHT1)
            glDisable(GL_LIGHT2)
            glDisable(GL_LIGHT3)
            break
        
        if key == b'3':
            view = '3'
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glEnable(GL_LIGHT2)
            glDisable(GL_LIGHT3)
            break

        if key == b'4':
            view = '4'
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT2)
            glEnable(GL_LIGHT3)
            break

        if key == b'5':
            view = '5'
            glEnable(GL_LIGHT0)
            glEnable(GL_LIGHT1)
            glEnable(GL_LIGHT2)
            glEnable(GL_LIGHT3)
            break
        if key == b'6':
            view = '6'
            glDisable(GL_LIGHT0)
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT2)
            glDisable(GL_LIGHT3)
            break
        break
    print(view)
    glutPostRedisplay()

  
if __name__ == '__main__': main()
    
    
    
    
    
    
    

