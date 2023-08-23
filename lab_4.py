

class Fly_det:
    def __init__(self, flights):
        self.flights = flights
    
    def search_by_loc(self, loc):
        matching_flights = [flight for flight in self.flights if loc in (flight.origin, flight.dest)]
        return matching_flights
    
    def search_from_loc(self, loc):
        matching_flights = [flight for flight in self.flights if flight.origin == loc]
        return matching_flights
    
    def search_between_cities(self, origin, dest):
        matching_flights = [flight for flight in self.flights if flight.origin == origin and flight.dest == dest]
        return matching_flights

class Flight:
    def __init__(self, flight_id, origin, dest, price):
        self.flight_id = flight_id
        self.origin = origin
        self.dest = dest
        self.price = price


def main():
    flights_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]
    
    flights = [Flight(*data) for data in flights_data]
    flight_table = Fly_det(flights)
    
    print("Choose Number corresponding:\n1. Flights for a particular city\n2. Flights From a city\n3. Flights between two given cities")
    
    ch = int(input("Enter your choice: \n"))
    
    if ch == 1:
        loc = input("Enter the city: \n")
        result = flight_table.search_by_loc(loc)
    elif ch == 2:
        loc = input("Enter the city: \n")
        result = flight_table.search_from_loc(loc)
    elif ch == 3:
        origin = input("Enter the source city: \n")
        dest = input("Enter the dest city: \n")
        result = flight_table.search_between_cities(origin, dest)
    else:
        print("Invalid choice!")
        return
    
    if not result:
        print("No flights found.")
    else:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.origin}\t{flight.dest}\t{flight.price}")

if __name__ == "__main__":
    main()
