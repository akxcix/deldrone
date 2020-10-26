import math


class Waypoint:
    """
    waypoint is a class that describes a geographical point on the map
    """

    def __init__(self, lat=0, long=0, name=str()):
        self.lat = lat
        self.long = long
        self.name = name

    def distance(self, other):
        """
        get geographical distnace between A and B using haversine formula
        """

        delta_lat = math.radians(other.lat) - math.radians(self.lat)
        delta_long = math.radians(other.long) - math.radians(self.long)

        a = (math.sin((delta_lat) / 2)) ** 2 + math.cos(
            math.radians(self.lat)
        ) * math.cos(math.radians(other.lat)) * ((math.sin((delta_long) / 2)) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return c * 6371000

    def get_bearing(self, other):
        """
        get bearing in degrees from A -> B
        """

        theta_B = math.radians(other.lat)
        theta_A = math.radians(self.lat)

        l_B = math.radians(other.long)
        l_A = math.radians(self.long)

        x = math.cos(theta_B) * math.sin(l_B - l_A)
        y = math.cos(theta_A) * math.sin(theta_B) - math.sin(theta_A) * math.cos(
            theta_B
        ) * math.cos(l_B - l_A)

        beta = math.atan2(x, y)

        return math.degrees(beta)
