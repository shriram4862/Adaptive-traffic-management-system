def get_vehicle_priorities():
    return {
        'bicycle': 1,
        'person': 1,
        'bike': 2,
        'car': 4,
        'auto': 3,
        'bus': 8,
        'Truck': 6,
        'emergency_vehicle': 10
    }

def get_vehicle_weights():
    return {
        'bicycle': 1,
        'person': 1,
        'bike': 1,
        'car': 3,
        'auto': 2,
        'bus': 8,
        'Truck': 8,
        'emergency_vehicle': 10
    }

def get_vehicle_counts():
    print("Enter the number of vehicles:")
    car = int(input("Cars: "))
    bus = int(input("Buses: "))
    bike = int(input("bike: "))
    bicycle = int(input("Bicycles: "))
    truck = int(input("Truck: "))
    person = int(input("Persons: "))
    auto = int(input("Auto: "))
    emergency_vehicle = int(input("emergency_vehicle: "))

    return {
        'person': person,
        'bicycle': bicycle,
        'bike': bike,
        'auto': auto,
        'car': car,
        'bus': bus,
        'truck': truck,
        'emergency_vehicle': emergency_vehicle
    }

def calculate_total_score(vehicles, priorities, weights):
    total_score = 0
    for vehicle, count in vehicles.items():
        score = count * priorities.get(vehicle, 0) * weights.get(vehicle, 0)
        total_score += score
    return total_score

def main():
    vehicle_priorities = get_vehicle_priorities()
    vehicle_weights = get_vehicle_weights()
    vehicles = get_vehicle_counts()
    total_score = calculate_total_score(vehicles, vehicle_priorities, vehicle_weights)
    print("Total Score:", total_score)

if __name__ == "__main__":
    main()
