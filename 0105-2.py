class Luggage:
    def __init__(self, luggage_id, weight, departure_time, destination_airport, passenger_name):
        # 行李類別的建構子
        self.luggage_id = luggage_id
        self.weight = weight
        self.departure_time = departure_time
        self.destination_airport = destination_airport
        self.passenger_name = passenger_name

    def display_info(self):
        # 顯示有關行李的資訊
        print(f"Luggage ID: {self.luggage_id}, Weight: {self.weight} kg, Departure Time: {self.departure_time}, Destination Airport: {self.destination_airport}, Passenger Name: {self.passenger_name}")

class BoardingPass:
    def __init__(self, passenger_name, boarding_pass_number, boarding_time, gate_number, seat_position, luggage_count, luggage_id):
        # 登機證類別的建構子
        self.passenger_name = passenger_name
        self.boarding_pass_number = boarding_pass_number
        self.boarding_time = boarding_time
        self.gate_number = gate_number
        self.seat_position = seat_position
        self.luggage_count = luggage_count
        self.luggage_id = luggage_id

    def display_info(self):
        # 顯示有關登機證的資訊
        print(f"Passenger Name: {self.passenger_name}, Boarding Pass Number: {self.boarding_pass_number}, Boarding Time: {self.boarding_time}, Gate Number: {self.gate_number}, Seat Position: {self.seat_position}, Luggage Count: {self.luggage_count}, Luggage ID: {self.luggage_id}")

class Passenger:
    def __init__(self, name, id_number, nationality, contact_number, email):
        # 乘客類別的建構子
        self.name = name
        self.id_number = id_number
        self.nationality = nationality
        self.contact_number = contact_number
        self.email = email

    def display_info(self):
        # 顯示有關乘客的資訊
        print(f"Name: {self.name}, ID Number: {self.id_number}, Nationality: {self.nationality}, Contact Number: {self.contact_number}, Email: {self.email}")

class Airport:
    def __init__(self, airport_name, location, operating_hours, contact_number, establishment_year):
        # 機場類別的建構子
        self.airport_name = airport_name
        self.location = location
        self.operating_hours = operating_hours
        self.contact_number = contact_number
        self.establishment_year = establishment_year

    def display_info(self):
        # 顯示有關機場的資訊
        print(f"Airport Name: {self.airport_name}, Location: {self.location}, Operating Hours: {self.operating_hours}, Contact Number: {self.contact_number}, Establishment Year: {self.establishment_year}")
