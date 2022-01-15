from math import cos, pi, sin

from geometry.ellipsoidGemetry import EllipsoidGeometry


class SphereGeometry(EllipsoidGeometry):
    def __init__(self, radius=1, radiusSegments=32, heightSements=16):
        super().__init__(2*radius, 2*radius, 2*radius, radiusSegments, heightSements)
