import time

class TrafficLight:
    def __init__(self, road_name, initial_state):
        self.road_name = road_name
        self.state = initial_state
        self.green_time = 60
        self.red_time = 60

    def switch_to_green(self):
        self.state = "green"
        time.sleep(self.green_time)

    def switch_to_red(self):
        self.state = "red"
        time.sleep(self.red_time)

    def __str__(self):
        return f"Traffic light for {self.road_name} is {self.state} for {self.green_time if self.state == 'green' else self.red_time} seconds"

class Intersection:
    def __init__(self):
        self.roads = {
            "lane1": TrafficLight("lane1", "red"),
            "lane2": TrafficLight("lane2", "red"),
            "lane3": TrafficLight("lane3", "red"),
            "lane4": TrafficLight("lane4", "red")
        }

    def simulate_traffic(self):
        while True:
            for road_name, traffic_light in self.roads.items():
                print("\nTraffic Status:")
                for road in self.roads.values():
                    print(road)
                print("\nTime Status:")
                for road in self.roads.values():
                    print(f"{road.road_name}: {road.green_time if road.state == 'green' else road.red_time} seconds")
                print("\n----------------------\n")
                
                print(f"Changing traffic light to green for {road_name}...")
                traffic_light.switch_to_green()

                # Switch all other lights to red
                for other_road in self.roads.values():
                    if other_road != traffic_light:
                        other_road.switch_to_red()

                print(f"{road_name} is now green. Waiting for {traffic_light.green_time} seconds...")
                time.sleep(1)

if __name__ == "__main__":
    intersection = Intersection()
    intersection.simulate_traffic()
