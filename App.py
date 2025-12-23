def print_timetable(route_name, hour, trips, gap):
    print()
    print("Route:", route_name)
    print("Timetable:")

    time = hour * 60 

    for i in range(trips):
        h = (time // 60) % 24
        print("Trip", i + 1, "=", str(h) + ":00")
        time = time + (gap * 60)


route_name = input("Enter route name: ")
start_hour = int(input("Start hour (0-23): "))
trips = int(input("How many trips? "))
gap = int(input("Gap between trips (hours): "))

print_timetable(route_name, start_hour, trips, gap)