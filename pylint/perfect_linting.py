"""This is a test of a docstring module"""
from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    """This is my class docstring"""
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        """
        Calculate the distance between one position and another, along the Earth’s surface.
        using the haversine formula:
        """
        radius = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        height = (sin((phi_2 - phi_1) / 2)**2
                  + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * radius * asin(sqrt(height))
