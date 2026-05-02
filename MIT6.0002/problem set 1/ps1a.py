###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Sasa Lakic
# Collaborators: Only me
# Time: 17:05 4/11/2025

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_dict = {}
    with open("ps1_cow_data.txt", "r") as file:
        while True:
            file_line = file.readline()
            if not file_line:
                break
            [name,weight] = file_line.split(',')
            weight = int(weight)
            
            cow_dict[name] = weight
    
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_dict = sorted(cows.items(), key = lambda item: item[1], reverse = True)
    cows_dict = dict(cows_dict)

    limit_when_empty = limit
    trips = []

    while cows_dict:
        current_limit = limit_when_empty
        trip = []
        for cow in list(cows_dict.keys()):
            cow_weight = cows_dict[cow]
            if(cow_weight <= current_limit):
                trip.append(cow)
                current_limit -= cow_weight
                del cows_dict[cow]
        trips.append(trip)

    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    min_trips_count = float('inf')
    best_allocation = None

    for partition in get_partitions(cows):
        
        is_valid = True
        for trip in partition:
            trip_weight = 0
            for cow in trip:
                trip_weight += cows[cow]
            if trip_weight > limit:
                is_valid = False
                break
        
        if is_valid:
            current_trips_count = len(partition)

            if current_trips_count < min_trips_count:
                min_trips_count = current_trips_count
                best_allocation = partition

    return best_allocation

    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    
    start = time.time()
    cow_trips = greedy_cow_transport(cows, 10)
    end = time.time()
    elapsed_time = end - start
    print("Time for calculating greedy: " + str(elapsed_time))

    start = time.time()
    best_partition = brute_force_cow_transport(cows, 10)
    end = time.time()
    elapsed_time = end - start
    print("Time for calculating brute_force: " + str(elapsed_time))

    pass

compare_cow_transport_algorithms()

# MOJE
# def main():
#     cows = load_cows("ps1_cow_data.txt")
#     cow_trips = greedy_cow_transport(cows, 10)
#     print(cow_trips)

#     best_partition = brute_force_cow_transport(cows, 10)
#     print(best_partition)


# main()