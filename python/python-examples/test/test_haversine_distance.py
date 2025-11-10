"""
Test for haversine distance.
"""
import logging as log
import numpy as np
from math import radians
import pytest
from sklearn.metrics.pairwise import haversine_distances
from python_examples.math.haversine_distance import calculate_haversine_distince, RADIUS_OF_EARTH

@pytest.mark.parametrize("lat_long_origin,lat_long_destination", [
    # Scikit Learn example Ezeiza Airport -> Charles de Gaulle Airport
    pytest.param(
        [-34.83333, -58.5166646], 
        [49.0083899664, 2.53844117956]
    ),
    # Google location vs USDA Location
    pytest.param(
        [39.0168311, -76.92883499999999],
        [39.01644, -76.928925]
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


def test_shortest_distance():
    # Lincoln Memorial Latlong
    lincoln_memorial = [38.889248, -77.050636]
    
    # Ducinni's off U St
    ducinnis_pizza = [38.91706701509112, -77.04118715785616]
    
    # Admo Jumbo Slice
    jumbo_slice_pizza = [38.92105748065034, -77.04170211776945]
    
    # Manny Olgas Near U 
    manny_olgas = [38.91543818061708, -77.03174726038766]

    # Based off Haversine which is closest to Lincoln Memorial
    dataset = [
        {'name': 'Lincoln Memorial', 'geocode': lincoln_memorial},
        {'name': "Ducinni's Pizza", 'geocode': ducinnis_pizza},
        {'name': 'Jumbo Slice Pizza', 'geocode': jumbo_slice_pizza},
        {'name': "Manny Olga's", 'geocode': manny_olgas}
    ]

    # Put all these in radians
    radian_distances = list(map(lambda x: [radians(_) for _ in x['geocode']], dataset))

    # Calculate the Haversine Distances
    distance_matrix_result = haversine_distances(radian_distances)

    # Pull out the first Entry in the 2D array
    km_distance_matrix_result = distance_matrix_result * RADIUS_OF_EARTH / 1000
    log.info(f"\nDistance Matrix in Kilometers:\n {km_distance_matrix_result}")

    # Get the index of the minimum distance for the lincoln memorial
    np_array = np.array(km_distance_matrix_result[0][1:])
    idx_min = np.argmin(np_array)
    # Closest Should be Ducinnis
    assert idx_min + 1 == 1 
    log.info(f"\nClosest Jumbo Slice spot to Lincoln Memorial by Haversine Distance is {dataset[idx_min + 1]['name']}")
