import requests

class WazeTrafficCameraNotifier:
    def __init__(self, user_location, destination):
        self.user_location = user_location
        self.destination = destination
        self.base_url = "https://www.waze.com/"

    def get_route_data(self):
        """Retrieve route data from Waze API"""
        route_url = f"{self.base_url}row-RoutingManager/routingRequest?from=x%3A{self.user_location['latitude']}+y%3A{self.user_location['longitude']}&to=x%3A{self.destination['latitude']}+y%3A{self.destination['longitude']}&at=0&returnJSON=true&returnGeometries=false&returnInstructions=true&timeout=60000&nPaths=1&options=AVOID_TRAILS%3At%2CALLOW_UTURNS%3At"
        response = requests.get(route_url)
        data = response.json()
        return data

    def check_traffic_cameras(self):
        """Check for traffic cameras along the route"""
        route_data = self.get_route_data()
        if "cameras" in route_data["alerts"]:
            traffic_cameras = route_data["alerts"]["cameras"]
            if traffic_cameras:
                print("Traffic cameras ahead:")
                for camera in traffic_cameras:
                    print(f"- {camera['street']}")

    def notify_traffic_cameras(self):
        """Notify the user if there are traffic cameras"""
        self.check_traffic_cameras()

# Example usage:
user_location = {
    "latitude": 37.7749,
    "longitude": -122.4194
}
destination = {
    "latitude": 37.3352,
    "longitude": -121.8811
}

notifier = WazeTrafficCameraNotifier(user_location, destination)
notifier.notify_traffic_cameras()
