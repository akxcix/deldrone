import airsim
import airsim_helper
import waypoint

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

path = [
    waypoint.Waypoint(30.35315, 76.36064, "A"),
    waypoint.Waypoint(30.35484, 76.36033, "B"),
]

airsim_helper.takeoffAndLandWithPath(path, client)
