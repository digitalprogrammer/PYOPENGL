from geometry.geometry import Geometry


class RectangleGeometry(Geometry):
    def __init__(self, width=1, height=1, position=[0, 0], alignment=[0.5, 0.5]):
        super().__init__()
        x, y = position
        a, b = alignment
        p0 = [x + (-a)*width, y + (-b)*height, 0]
        p1 = [x + (1-a)*width, y + (-b)*height, 0]
        p2 = [x + (-a)*width, y + (1-b)*height, 0]
        p3 = [x + (1-a)*width, y + (1-b)*height, 0]
        c0, c1, c2, c3 = [1,1,1], [1,0,0], [0,1,0], [0,0,1]
        positionData = [p0,p1,p3, p0,p3,p2]
        colorData = [c0,c1,c3, c0,c3,c2]
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)

        #textures coordinates
        t0, t1, t2, t3 = [0,0], [1,0], [0,1], [1,1]
        uvData = [t0,t1,t3, t0,t3,t2]        
        self.addAttribute("vec2", "vertexUV", uvData)

        #normal vectors
        normalVector = [0,0,1]
        normalData = [normalVector] * 6
        self.addAttribute("vec3", "vertexNormal", normalData)
        self.addAttribute("vec3", "faceNormal", normalData)
        
        self.countVertices()
