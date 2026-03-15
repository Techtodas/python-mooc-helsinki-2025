# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str):
    stations = {}

    with open(filename) as new_file:
        first_line = True
        for line in new_file:
            if first_line:
                first_line = False
                continue
            line = line.split(";")
            station_name = line[3]
            longitude = float(line[0])
            latitude = float(line[1])
            stations[station_name] = (longitude, latitude)
 
    return stations

def distance(stations: dict, station1: str, station2: str):
    longitude1 = 0
    latitude1 = 0
    longitude2 = 0
    latitude2 = 0

    for station, coordinate in stations.items():
        if station1 == station:
            longitude1 = coordinate[0]
            latitude1 = coordinate[1]
        elif station2 == station:
            longitude2 = coordinate[0]
            latitude2 = coordinate[1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    names = list(stations.keys())
    best_distance = 0
    best_station1 = None
    best_station2 = None
    
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            station1 = names[i]
            station2 = names[j]

            distance_km = distance(stations, station1, station2)

            if distance_km > best_distance:
                best_distance = distance_km
                best_station1 = names[i]
                best_station2 = names[j]

    return (best_station1, best_station2, best_distance)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)