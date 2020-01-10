# Simple program to illustrate using class

from Station import Station

# Main program entry point
if __name__ == '__main__':
    # Print a blank line
    print("")

    # Create a station with default data values
    station_a = Station()
    print("station_a=" + str(station_a))

    # Create a station with supplied data values
    id = "station_a"
    longitude = "45.00"
    latitude = "-106.00"
    station_b = Station("station_a",longitude,latitude)
    print("station_b=" + str(station_b))
