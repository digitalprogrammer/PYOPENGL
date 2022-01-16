from pydoc import cram
from typing import Text

from core.base import Base
from core.camera import Camera
from core.mesh import Mesh
from core.renderer import Renderer
from core.scene import Scene
from core.texture import Texture
from extras.gridHelper import GridHelper
from extras.movementRig import MovementRig
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
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0, 0.5, 3])
        self.scene.add(self.rig)
        
        crateGeometry = BoxGeometry()
        crateTexture = Texture("images/crate.png")
        crateMateril = TextureMaterial(crateTexture)
        crate = Mesh(crateGeometry, crateMateril)
        self.scene.add(crate)

        grid = GridHelper(gridColor=[1,1,1], centerColor=[1,1,0])
        grid.rotateX(-3.14 * 0.5)
        self.scene.add(grid)

        self.hudScene = Scene()
        self.hudCamera = Camera()
        self.hudCamera.setOrthographic(0, 800, 0, 600, 1, -1)
        labelGeo1 = RectangleGeometry(width=600, height=80, position=[0,600], alignment=[0,1])

        labelText1 = Texture("images/cafe.png")
        labelMat1 = TextureMaterial(labelText1)
        label1 = Mesh(labelGeo1, labelMat1)
        self.hudScene.add(label1)

        labelGeo2 = RectangleGeometry(width=400, height=80, position=[800,0], alignment=[1,0])
        labelText2 = Texture("images/cafe.png")
        labelMat2 = TextureMaterial(labelText2)
        label2 = Mesh(labelGeo2, labelMat2)
        self.hudScene.add(label2)
    
    def update(self):
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hudScene, self.hudCamera, clearColor=False)

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
