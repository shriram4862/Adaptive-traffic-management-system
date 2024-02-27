import time

class TrafficLight:
    def __init__(self):
        self.states = ['Red', 'Green', 'Yellow']
        self.delay = {'Red': 10, 'Green': 15, 'Yellow': 3}
        self.current_state = 'Red'

    def run(self):
        while True:
            print(f"The light is {self.current_state}")
            time.sleep(self.delay[self.current_state])
            self.change_state()

    def change_state(self):
        current_index = self.states.index(self.current_state)
        self.current_state = self.states[(current_index + 1) % len(self.states)]

# Create an instance of the TrafficLight class
traffic_light = TrafficLight()

# Run the traffic light simulation
traffic_light.run()