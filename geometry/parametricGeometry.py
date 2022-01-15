from geometry.geometry import Geometry


class ParametricGeometry(Geometry):
    def __init__(self, uStart, uEnd, uResolution, 
    vStart, vEnd, vResolution, surfaceFunction):
        super().__init__()

        #generate set of points on function
        deltaU = (uEnd - uStart) / uResolution
        deltaV = (vEnd - vStart) / vResolution

        positions = []
        uvs = []

        for uIndex in range(uResolution+1):
            vArray = []
            for vIndex in range(vResolution+1):
                u = uStart + uIndex * deltaU
                v = vStart + vIndex * deltaV
                vArray.append(surfaceFunction(u, v))
            positions.append(vArray)

        
        for uIndex in range(uResolution+1):
            vArray = []
            for vIndex in range(vResolution+1):
                u = uIndex/uResolution
                v = vIndex/vResolution
                vArray.append([u,v])
            uvs.append(vArray)
        
        #store vertex data 
        positionData = []
        colorData = []
        uvData = []

        #default verex colors
        c1, c2, c3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        c4, c5, c6 = [0, 1, 1], [1, 0, 1], [1, 1, 0]

        #group vertex data into triangles
        #note: .copy[] is necessary to avoid storing references
        for xIndex in range(uResolution):
            for yIndex in range(vResolution):
                #position data
                pa = positions[xIndex+0][yIndex+0]
                pb = positions[xIndex+1][yIndex+0]
                pc = positions[xIndex+1][yIndex+1]
                pd = positions[xIndex+0][yIndex+1]
                positionData += [
                    pa.copy(), pb.copy(),
                    pc.copy(), pa.copy(),
                    pc.copy(), pd.copy()
                ]
                #color data
                colorData += [c1,c2,c3, c4,c5,c6]

                #uv coordinates
                uvA = uvs[xIndex+0][yIndex+0]
                uvB = uvs[xIndex+1][yIndex+0]
                uvC = uvs[xIndex+1][yIndex+1]
                uvD = uvs[xIndex+0][yIndex+1]
                uvData += [uvA,uvB,uvC, uvA,uvC,uvD]
                       
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.addAttribute("vec2", "vertexUV", uvData)
        self.countVertices()
