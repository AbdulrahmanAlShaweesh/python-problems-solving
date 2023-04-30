

""" Distance Travel """

def distance_travel(times, speed, distances) :
     
    # the distance that will travel in 6, 10 and 15 hours.
    for timeTravel in times :
        distance = speed * timeTravel
        print(f'The car will trave {distance} is {timeTravel}')

times = [6, 10, 15]
speed = 70
distances = []
distance_travel(times, speed, distances)