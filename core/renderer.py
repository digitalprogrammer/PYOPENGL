import pygame
from light.light import Light
from OpenGL.GL import *

from core.mesh import Mesh


class Renderer(object):
    def __init__(self, clearColor=[0, 0, 0]):
        glEnable(GL_DEPTH_TEST)
        #require for antialiasing
        glEnable(GL_MULTISAMPLE)
        glClearColor(clearColor[0], clearColor[1], clearColor[2], 1)
        #support transparent textures
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.windowSize = pygame.display.get_surface().get_size()

    

    def render(self, scene, camera, clearColor=True, clearDepth=True, renderTarget=None):
        #activate render target
        if renderTarget == None:
            #set render target to window
            glBindFramebuffer(GL_FRAMEBUFFER, 0)
            glViewport(0, 0, self.windowSize[0], self.windowSize[1])
        else:
            #set render target properties
            glBindFramebuffer(GL_FRAMEBUFFER, renderTarget.framebufferRef)
            glViewport(0, 0, renderTarget.width, renderTarget.height)
        
        #clear color and depth buffers
        if clearColor:
            glClear(GL_COLOR_BUFFER_BIT)
        if clearDepth:
            glClear(GL_DEPTH_BUFFER_BIT)

        #Update camera view (calculate inverse)
        camera.updateViewMatrix()

        #extract list of all Mesh objects in scene 
        descendantList = scene.getDescendantList()
        meshFilter = lambda x : isinstance(x, Mesh)
        meshList = list(filter(meshFilter, descendantList))

        lightFilter = lambda x : isinstance(x, Light)
        lightList = list(filter(lightFilter, descendantList))

        #scenes support 4 lights; precisely 4 must be present 
        while len(lightList) < 4:
            lightList.append(Light())

        for mesh in meshList:
            #if this object is not visible continue to next object in list
            if not mesh.visible:
                continue

            glUseProgram(mesh.material.programRef)

            #bind VAO
            glBindVertexArray(mesh.vaoRef)

            #update uniform values stored outside of material
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projectionMatrix

            #if material uses light data, add lights from list
            if "light0" in mesh.material.uniforms.keys():
                for lightNumber in range(4):
                    lightName = "light" + str(lightNumber)
                    lightObject = lightList[lightNumber]
                    mesh.material.uniforms[lightName].data = lightObject
            #add camera position if needed (specular lighting)
            if "viewPosition" in mesh.material.uniforms.keys():
                mesh.material.uniforms["viewPosition"].data = camera.getWorldPosition()

            #update uniforms stored in material 
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()
            #update render settings
            mesh.material.updateRenderSettings()
            glDrawArrays(mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)
