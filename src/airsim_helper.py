import airsim
import waypoint
import math

# GLOBAL VARIABLES
CRUISE_VELOCITY = 10     # 10 m/s
CRUISE_ALTITUDE = -50    # 50 m
BASE_POSITION = waypoint.Waypoint(lat=30.35294, long=76.36183, name="BASE")


def connect(client):
    """
    establishes connection to `airsim.MultirotorClient`
    """
    client.confirmConnection()
    client.enableApiControl(True)
    client.armDisarm(True)


def gps2ned(waypoint):
    bearing = BASE_POSITION.get_bearing(waypoint)
    distance = BASE_POSITION.distance(waypoint)
    y = math.sin(math.radians(bearing)) * distance
    x = math.cos(math.radians(bearing)) * distance
    return [x, y]


def traversePath(waypoints, client):
    for point in waypoints:
        ned = gps2ned(point)
        print(ned, point.name)
        client.moveToPositionAsync(
            ned[0], ned[1], CRUISE_ALTITUDE, CRUISE_VELOCITY).join()


def takeoffAndLandWithPath(waypoints, client):
    # takeoff
    client.takeoffAsync().join()
    client.moveToZAsync(CRUISE_ALTITUDE, CRUISE_VELOCITY).join()

    # traverse
    traversePath(waypoints, client)

    # land
    client.moveToZAsync(-3, CRUISE_VELOCITY).join()
    print("Landing")
    client.landAsync().join()
    print("Landed")
