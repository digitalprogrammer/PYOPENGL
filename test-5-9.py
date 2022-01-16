from math import floor

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
from material.spriteMaterial import SpriteMaterial
from material.surfaceMaterial import SurfaceMaterial
from material.textureMaterial import TextureMaterial


#render a basic scene
class Test(Base):
    def initialize(self):
        print("Initializing...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 4])
        
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0, 0.5, 3])
        self.scene.add(self.rig)

        geometry = RectangleGeometry()
        tileSet = Texture("images/rolling-ball.png")
        spriteMaterial = SpriteMaterial(tileSet, {
            "billboard":1,
            "tileCount":[8,4],
            "tileNumber":0
        })
        self.tilesPerSecond = 8
        self.sprite = Mesh(geometry, spriteMaterial)
        self.scene.add(self.sprite)

        grid = GridHelper()
        grid.rotateX(-3.14 * 0.5)
        self.scene.add(grid)

    
    def update(self):
        tileNumber = floor(self.time * self.tilesPerSecond)
        self.sprite.material.uniforms["tileNumber"].data = tileNumber
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.camera)

    
#inistantiate this class and run the program
Test(screenSize=[800, 600]).run()
