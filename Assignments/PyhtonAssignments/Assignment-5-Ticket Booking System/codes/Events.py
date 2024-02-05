from datetime import datetime
from Venue import Venue


class Event(Venue):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, available_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = datetime.strptime(event_date, "%Y-%m-%d").date()
        self.event_time = datetime.strptime(event_time, "%H:%M").time()
        self.venue_name = venue.venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def calculate_total_revenue(self):
        return self.ticket_price * (self.total_seats - self.available_seats)

    def getBookedNoOfTickets(self):
        return self.total_seats-self.available_seats

    def book_tickets(self, num_tickets):
        self.available_seats = self.available_seats - num_tickets

    def cancel_booking(self, num_tickets):
        self.available_seats = self.available_seats + num_tickets

    def display_event_details(self):
        print(f"Event name = {self.event_name}")
        print(f"Date of event = {self.event_date}")
        print(f"Time of event = {self.event_time}")
        print(f"Venue name = {self.venue_name}")
        print(f"Available Seats = {self.available_seats}")