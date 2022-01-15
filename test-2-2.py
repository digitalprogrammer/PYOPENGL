from OpenGL.GL import *

from core.base import Base
from core.openGLUtils import OpenGLUtils


#Render a single point on the screen. The point can be scaled
class Test(Base):
    def initialize(self):
        #return super().initialize()
        print("Initializing...")
        #initialize program
        #vertex shader code
        vsCode = """
        void main()
        {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }"""

        #fragment shader code
        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }"""

        #Send code to GPU and compile; store program reference
        self.programRef = OpenGLUtils.initializeProgram(
            vsCode, fsCode)
        #set up vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        #render settings (optional)
        #set point width and height
        glPointSize(10)

    def update(self):
        #select program to use when rendering
        glUseProgram(self.programRef)

        #renders geometric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)
    #Instatiate this class and run the program
Test().run()
