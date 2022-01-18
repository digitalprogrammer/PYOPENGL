import numpy

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
        
        def calculateNormal(p0, p1, p2):
            v1 = numpy.array(p1) - numpy.array(p0)
            v2 = numpy.array(p2) - numpy.array(p0)

            normal = numpy.cross(v1, v2)
            normal = normal / numpy.linalg.norm(normal)
            return normal
        
        vertexNormals = []
        for uIndex in range(uResolution+1):
            vArray = []
            for vIndex in range(vResolution+1):
                u = uStart = uIndex * deltaU
                v = vStart + vIndex * deltaV
                h = 0.0001
                p0 = surfaceFunction(u,v)
                p1 = surfaceFunction(u+h,v)
                p2 = surfaceFunction(u,v+h)
                normalVector = calculateNormal(p0, p1, p2)
                vArray.append(normalVector)
            vertexNormals.append(vArray)

        #store vertex data 
        positionData = []
        colorData = []
        uvData = []

        #default verex colors
        c1, c2, c3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        c4, c5, c6 = [0, 1, 1], [1, 0, 1], [1, 1, 0]

        vertexNormalData = []
        faceNormalData = []

        #group vertex data into triangles
        #note: .copy[] is necessary to avoid storing references
        for xIndex in range(uResolution):
            for yIndex in range(vResolution):
                #position data
                pA = positions[xIndex+0][yIndex+0]
                pB = positions[xIndex+1][yIndex+0]
                pC = positions[xIndex+1][yIndex+1]
                pD = positions[xIndex+0][yIndex+1]
                positionData += [
                    pA.copy(), pB.copy(),
                    pC.copy(), pA.copy(),
                    pC.copy(), pD.copy()
                ]
                #color data
                colorData += [c1,c2,c3, c4,c5,c6]

                #uv coordinates
                uvA = uvs[xIndex+0][yIndex+0]
                uvB = uvs[xIndex+1][yIndex+0]
                uvC = uvs[xIndex+1][yIndex+1]
                uvD = uvs[xIndex+0][yIndex+1]
                uvData += [uvA,uvB,uvC, uvA,uvC,uvD]

                #vertex normal vectors
                nA = vertexNormals[xIndex+0][yIndex+0]
                nB = vertexNormals[xIndex+1][yIndex+0]
                nD = vertexNormals[xIndex+0][yIndex+1]
                nC = vertexNormals[xIndex+1][yIndex+1]
                vertexNormalData += [nA,nB,nC, nA,nC,nD]

                #face normal vectors
                fn0 = calculateNormal(pA,pB,pC)
                fn1 = calculateNormal(pA, pC, pD)
                faceNormalData += [fn0,fn0,fn0, fn1,fn1,fn1]
                       
        self.addAttribute("vec3", "vertexNormal", vertexNormalData)
        self.addAttribute("vec3", "faceNormal", faceNormalData)
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.addAttribute("vec2", "vertexUV", uvData)
        self.countVertices()

   
