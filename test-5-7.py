from typing import Text

from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from core.texture import Texture
from extras.textTexture import TextTexture
from geometry.boxGeometry import BoxGeometry
from geometry.rectangleGeometry import RectangleGeometry
from material.surfaceMaterial import SurfaceMaterial
from material.textureMaterial import TextureMaterial


#render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 1.5])
        
        geometry = RectangleGeometry()
        message = TextTexture(text="Caipora Graphics", systemFontName="Impact", 
                            fontSize=32, fontColor=[0,0,200], imageWidth=256,
                            imageHeight=256, alignHorizontal=0.5, alignVertical=0.5,
                            imageBorderWidth=4, imageBorderColor=[255,0,0])

        material = TextureMaterial(message)
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)
    
    def update(self):
        #self.mesh.rotateY(0.0514)
        #self.mesh.rotateX(0.0337)
        self.renderer.render(self.scene, self.camera)

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
