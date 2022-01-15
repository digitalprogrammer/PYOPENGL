from OpenGL.GL import *

from core.attribute import Attribute
from core.base import Base
from core.openGLUtils import OpenGLUtils


#render two shapes. See we use two vaos and they are storesd in class variables
class Test(Base):
    def initialize(self):
        #return super().initialize()
        print("Initializing...")

        #initialize program
        vsCode = """
        in vec3 position;
        void main()
        {
            gl_Position = vec4(position, 1.0);
        }"""

        fsCode = """
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }"""

        self.programRef = OpenGLUtils.initializeProgram(
            vsCode, fsCode)
        
        #render settings
        glLineWidth(4)

        #set up vertex array object - triangle
        self.vaoTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoTri)
        positionDataTri = [
            [-0.5, 0.8, 0.0],
            [-0.2, 0.2, 0.0],
            [-0.8, 0.2, 0.0]
        ]
        self.vertexCountTri = len(positionDataTri)
        positionAttributeTri = Attribute(
            "vec3", positionDataTri)
        positionAttributeTri.associateVariable(
            self.programRef, "position")
        
        #set up vertex array object - square
        self.vaoSquare = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSquare)
        positionDataSquare = [
            [0.8, 0.8, 0.0],
            [0.8, 0.2, 0.0],
            [0.2, 0.2, 0.2],
            [0.2, 0.8, 0.0]
        ]
        self.vertexCountSquare = len(positionDataSquare)
        positionAttributeSquare = Attribute(
            "vec3", positionDataSquare)
        positionAttributeSquare.associateVariable(
            self.programRef, "position")
    

    def update(self):
        #return super().update()
        #using same program to render both shapes
        glUseProgram(self.programRef)

        #draw the triangle 
        glBindVertexArray(self.vaoTri)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountTri)

        #draw the square 
        glBindVertexArray(self.vaoSquare)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountSquare)


Test().run()
