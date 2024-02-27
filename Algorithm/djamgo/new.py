# Import the module containing the get_vehicle_counts function
import module  # Replace 'module_name' with the actual name of your module

def main():
    # Input: Number of lanes
    num_lanes = int(input("Enter the number of lanes: "))

    # Loop through each lane
    for lane in range(1, num_lanes + 1):
        # Call the get_vehicle_counts function for each lane
        counts = module.get_vehicle_counts(lane)  # Adjust module_name accordingly
        print(counts)

if __name__ == "__main__":
    main()
