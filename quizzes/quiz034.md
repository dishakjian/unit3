## Paper Solution

![photo_2025-01-30_08-43-30](https://github.com/user-attachments/assets/018c28ce-d3fb-468e-bc91-354bc44e802e)


## Code
```.py

class Flight:
    def __init__(self, flight_number: str, origin: str, destination: str, 
                 departure_time: str, arrival_time: str):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passenger_list = set()  # Using a set to avoid duplicate names

    def add_passenger(self, passenger_name: str) -> str:
        if passenger_name in self.passenger_list:
            return f"{passenger_name} is already on the flight."
        self.passenger_list.add(passenger_name)
        return f"{passenger_name} has been added to the flight."

    def remove_passenger(self, passenger_name: str) -> str:
        if passenger_name in self.passenger_list:
            self.passenger_list.remove(passenger_name)
            return f"{passenger_name} has been removed from the flight."
        return f"{passenger_name} is not on the flight."

    def show_flight(self) -> str:
        return (
            f"\nFlight Details:\n"
            f"--------------------\n"
            f"Flight Number : {self.flight_number}\n"
            f"Origin        : {self.origin}\n"
            f"Destination   : {self.destination}\n"
            f"Departure     : {self.departure_time}\n"
            f"Arrival       : {self.arrival_time}\n"
            f"Passengers    : {', '.join(self.passenger_list) if self.passenger_list else 'No passengers yet.'}\n"
            f"--------------------"
        )

# Test Cases

# First Flight
flight1 = Flight("EAW520", "Johannesburg", "Seoul", "10:00 AM", "4:00 PM")
print(flight1.show_flight())
print(flight1.add_passenger("Esther Mawero"))
print(flight1.add_passenger("Lungile Phiri"))
print(flight1.add_passenger("Emily Banda"))
print(flight1.show_flight())
print(flight1.remove_passenger("Lungile Phiri"))
print(flight1.show_flight())

# Second Flight
flight2 = Flight("QR202", "Doha", "New York", "2:30 PM", "8:45 AM")
print(flight2.show_flight())
print(flight2.add_passenger("Aisha Khan"))
print(flight2.add_passenger("Michael Jones"))
print(flight2.add_passenger("Sarah Lee"))
print(flight2.show_flight())
print(flight2.remove_passenger("Michael Jones"))
print(flight2.show_flight())


```


## Proof Code Works

![image](https://github.com/user-attachments/assets/996714e3-d6bc-4814-b9d8-9b2867d43de0)

