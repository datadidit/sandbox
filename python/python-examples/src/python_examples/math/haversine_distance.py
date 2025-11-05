"""
Utility class to use python to calculate the haversine distance between two longitude
and latitude points.
"""
import logging as log

from math import radians, sin, cos, atan2, sqrt

log.basicConfig(level=log.INFO)

# Radius of earth in meters
RADIUS_OF_EARTH = 6371000

def calculate_haversine_distince(lat_long_start:list, lat_long_end:list):
    """Calculate the haversine distance."""
    # Taken from here 
    # https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128

    # Direct Unpack the 
    # Minor correction to code unpack should 
    lat1, lon1 = lat_long_start
    lat2, lon2 = lat_long_end

    # Radians???
    phi_1 = radians(lat1)
    phi_2 = radians(lat2)

    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)

    a = sin(delta_phi / 2.0) ** 2 + cos(phi_1) * cos(phi_2) * sin(delta_lambda / 2.0) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Output distance in meters
    meters = RADIUS_OF_EARTH * c

    return meters
