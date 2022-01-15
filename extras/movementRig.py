from core.object3D import Object3D


class MovementRig(Object3D):
    def __init__(self, unitsPerSecond=1, degreesPerSecond=60):
        #initilize base object3d; controls movement and turn left/right
        super().__init__()
        #initialize attached object3d; controls look up/down
        self.lookAttachment = Object3D()
        self.children = [self.lookAttachment]
        self.lookAttachment.parent = self

        #control rate of movement
        self.unitsPerSecond = unitsPerSecond
        self.degreesPerSecond = degreesPerSecond

        #custumizable key mappings
        # defaults: WASDRF (move), QE (turn), TG (look)
        self.KEY_MOVE_FORWARDS = "w"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_LEFT = "a"
        self.KEY_MOVE_RIGHT = "d"
        self.KEY_MOVE_UP = "r"
        self.KEY_MOVE_DOWN = "f"
        self.KEY_TURN_LEFT = "q"
        self.KEY_TURN_RIGHT = "e"
        self.KEY_LOOK_UP = "t"
        self.KEY_LOOK_DOWN = "g"

    #adding and removing objects applies to look attachment;
    #override funtions from object3d class
    def add(self, child):
        self.lookAttachment.add(child)

    def remove(self, child):
        self.lookAttachment.remove(child)

    def update(self, inputObejct, deltaTime):
        moveAmount = self.unitsPerSecond * deltaTime
        rotateAmount = self.degreesPerSecond * 3.1415926 * 0.0055555 * deltaTime

        if inputObejct.isKeyPressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -moveAmount)
        if inputObejct.isKeyPressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, moveAmount)
        if inputObejct.isKeyPressed(self.KEY_MOVE_LEFT):
            self.translate(-moveAmount, 0, 0)
        if inputObejct.isKeyPressed(self.KEY_MOVE_RIGHT):
            self.translate(moveAmount, 0, 0)
        if inputObejct.isKeyPressed(self.KEY_MOVE_UP):
            self.translate(0, moveAmount, 0)
        if inputObejct.isKeyPressed(self.KEY_MOVE_DOWN):
            self.translate(0, -moveAmount, 0)

        if inputObejct.isKeyPressed(self.KEY_TURN_LEFT):
            self.rotateY(rotateAmount)
        if inputObejct.isKeyPressed(self.KEY_TURN_RIGHT):
            self.rotateY(-rotateAmount)

        if inputObejct.isKeyPressed(self.KEY_LOOK_UP):
            self.lookAttachment.rotateX(rotateAmount)
        if inputObejct.isKeyPressed(self.KEY_LOOK_DOWN):
            self.lookAttachment.rotateX(-rotateAmount)

        
        
