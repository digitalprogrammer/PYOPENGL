from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform
from OpenGL.GL import *


class Material(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.programRef = OpenGLUtils.initializeProgram(
            vertexShaderCode, fragmentShaderCode)
        #store uniform objects, indexed by name of associated variable in shader
        self.uniforms = {}
        #each shader typically constains these uniforms
        #values will be set during render process from Mesh/Camera
        #additinal uniforms added by extending classes
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)
        
        #store opengl render settings indexed by variable name
        #Additional settingd added by extending classes 
        self.settings = {}
        self.settings["drawStyle"] = GL_TRIANGLES
    
    def addUniform(self, dataType, variableName, data):
        self.uniforms[variableName] = Uniform(dataType, data)
        
    
    #initialize all uniform variable references
    def locateUniforms(self):
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locateVariable(
                self.programRef, variableName)
    

    #configure opengl with render settings
    def updateRenderSettings(self):
        pass
    
    #convenience method for setting multiple material "properties"
    #uniform and render settings values - from a dictionary
    def setProperties(self, properties={}):
        for name, data in properties.items():
            #update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            #update render settings
            elif name in self.settings.keys():
                self.settings[name] = data
            #unknown property type
            else:
                raise Exception("Material has no property named: "+ name)
