from math import radians, cos, sin, asin, sqrt

# Pune/Chennai coordinates for our sabotage test
CITY_MAP = {
    "CHENNAI": (13.0827, 80.2707),
    "PUNE": (18.5204, 73.8567),
    "BANGALORE": (12.9716, 77.5946),
    "MUMBAI": (19.0760, 72.8777)
}

def get_velocity(city1, city2, time_diff_hours):
    if city1 == city2 or time_diff_hours <= 0:
        return 0
    
    lat1, lon1 = CITY_MAP.get(city1, (0,0))
    lat2, lon2 = CITY_MAP.get(city2, (0,0))
    
    if (lat1, lon1) == (0,0) or (lat2, lon2) == (0,0):
        return 0

    # Distance calculation
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    km = 6371 * 2 * asin(sqrt(a))
    
    return km / time_diff_hours
def is_impossible_travel(velocity_kmh):
    """
    Rule: Flags if the travel speed exceeds commercial flight limits.
    Anything > 900 km/h triggers a geographical anomaly.
    """
    COMMERCIAL_FLIGHT_MAX_KMH = 900
    return velocity_kmh > COMMERCIAL_FLIGHT_MAX_KMH

# Optional: Add DELHI to your CITY_MAP if you want to expand the test net
# "DELHI": (28.7041, 77.1025),