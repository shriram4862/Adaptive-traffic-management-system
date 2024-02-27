#declearation of priority
#comparision of priority
#abmulance of priority
# Define the priorities of vehicles
# Define the priorities of vehicles
vehicle_priorities = {
    'car': 3,
    'bus': 4,
    'motorcycle': 2,
    'bicycle': 1,
    'person': 1,
    'ambulance': 5
}

# Define the parts
parts = ['Part 1', 'Part 2', 'Part 3', 'Part 4']

# Initialize part counts
part_counts = {part: {} for part in parts}

# Input the number of vehicles in each part
for part in parts:
    print(f"Enter the number of vehicles in {part}:")
    part_counts[part]['car'] = int(input("Cars: "))
    part_counts[part]['bus'] = int(input("Buses: "))
    part_counts[part]['motorcycle'] = int(input("Motorcycles: "))
    part_counts[part]['bicycle'] = int(input("Bicycles: "))
    part_counts[part]['person'] = int(input("Persons: "))

# Calculate the priority score for each part
part_scores = {}
for part, counts in part_counts.items():
    score = sum(counts.get(vehicle, 0) * vehicle_priorities.get(vehicle, 0) for vehicle in counts.keys())
    part_scores[part] = score

# Find the part with the highest priority score
max_part = max(part_scores, key=part_scores.get)

# Print the results
print("\nVehicle Counts in Each Part:")
for part, counts in part_counts.items():
    print(f"{part}:")
    for vehicle, count in counts.items():
        print(f"{vehicle}: {count}")
print("\nPart with the Highest Priority Score:")
print(f"{max_part} with a priority score of {part_scores[max_part]}")


##############################