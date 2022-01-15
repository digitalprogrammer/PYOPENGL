from geometry.parametricGeometry import ParametricGeometry


class PlaneGeometry(ParametricGeometry):
    def __init__(self, width=1, height=1, widthSegments=8, heightSegments=8):
        def S(u, v):
            return [u, v, 0]
        super().__init__(
            -width*0.5, width*0.5, widthSegments, 
            -height*0.5, height*0.5, heightSegments, S)
