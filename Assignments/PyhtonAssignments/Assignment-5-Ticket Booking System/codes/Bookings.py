from bean.Events import Event
import random
from datetime import date


class Booking(Event):

    def __init__(self, event, customer):
        self.booking_id = random.randint(10000, 99999)
        self.customer = customer
        self.event = event
        self.num_tickets = len(customer)
        self.total_cost = 0
        self.booking_date = date.today()


    def calculate_booking_cost(self, num_tickets):
        pass

    def book_tickets(self, num_tickets):
        super().book_tickets(num_tickets)

    def cancel_booking(self, num_tickets):
        super().cancel_booking(num_tickets)

    def getAvailableNoOfTickets(self):
        return self.event.available_seats

    def getEventDetails(self):
        pass
