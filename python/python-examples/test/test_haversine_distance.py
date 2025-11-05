"""
Test for haversine distance.
"""
import logging as log
from math import radians
import pytest
from sklearn.metrics.pairwise import haversine_distances
from python_examples.math.haversine_distance import calculate_haversine_distince, RADIUS_OF_EARTH

@pytest.mark.parametrize("lat_long_origin,lat_long_destination", [
    # Scikit Learn example Ezeiza Airport -> Charles de Gaulle Airport
    pytest.param(
        [-34.83333, -58.5166646], 
        [49.0083899664, 2.53844117956]
    )
])
def test_calculate_haversince_distance(lat_long_origin:list, lat_long_destination:list):
    """Test haversine_distance against """
    # log.info(f"origin:{lat_long_origin} destination:{lat_long_destination}")
    log.info(f"{lat_long_origin} - {lat_long_destination}")
    origin_in_radians = [radians(_) for _ in lat_long_origin]
    destination_in_radians = [radians(_) for _ in lat_long_destination]
    distance_matrix_result = haversine_distances([origin_in_radians, destination_in_radians])
    km_distance_matrix_result = distance_matrix_result * RADIUS_OF_EARTH / 1000

    haversine_distance = calculate_haversine_distince(lat_long_origin, lat_long_destination)
    km_haversine_distance = round(haversine_distance / 1000, 8)
    sklearn_distance = km_distance_matrix_result[0][1]
    log.info(f"Raw Calc={km_haversine_distance}, Sklearn Calc={sklearn_distance}")
    # Rounding both to 8 digits of accuracy...
    assert km_haversine_distance == round(km_distance_matrix_result[0][1], 8)