from math import atan, cos, radians, sin, tan

from .haversine_distance import haversine_distance


def lamberts_ellipsoidal_distance(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:

    

    
    
    AXIS_A = 6378137.0
    AXIS_B = 6356752.314245
    EQUATORIAL_RADIUS = 6378137

    
    
    flattening = (AXIS_A - AXIS_B) / AXIS_A
    
    
    b_lat1 = atan((1 - flattening) * tan(radians(lat1)))
    b_lat2 = atan((1 - flattening) * tan(radians(lat2)))

    
    
    sigma = haversine_distance(lat1, lon1, lat2, lon2) / EQUATORIAL_RADIUS

    
    P_value = (b_lat1 + b_lat2) / 2
    Q_value = (b_lat2 - b_lat1) / 2

    
    
    X_numerator = (sin(P_value) ** 2) * (cos(Q_value) ** 2)
    X_demonimator = cos(sigma / 2) ** 2
    X_value = (sigma - sin(sigma)) * (X_numerator / X_demonimator)

    
    
    Y_numerator = (cos(P_value) ** 2) * (sin(Q_value) ** 2)
    Y_denominator = sin(sigma / 2) ** 2
    Y_value = (sigma + sin(sigma)) * (Y_numerator / Y_denominator)

    return EQUATORIAL_RADIUS * (sigma - ((flattening / 2) * (X_value + Y_value)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
