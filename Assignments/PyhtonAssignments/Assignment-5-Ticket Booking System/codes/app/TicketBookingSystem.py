from bean.BookingSystemServiceProviderImpl import BookingSystemServiceProviderImpl
from bean.EventServiceProviderImpl import EventServiceProviderImpl
from DBUtil import DBUtil


class TicketBookingSystem(EventServiceProviderImpl, BookingSystemServiceProviderImpl):
    def __init__(self, dbUtil):
        super().__init__(dbUtil)

    def main(self):
        while True:
            print("Select one options from the options given below : ")
            print("1. Type create_event to Create a new event.")
            print("2. Type book_tickets to book tickets.")
            print("3. Type cancel_tickets Cancel Tickets.")
            print("4. Type get_available_seats to Know how many seats are Available.")
            print("5. Type get_event_details to see every event and it's details.")
            print("6. Type exit to Exit from the application.")
            choice = input("Enter your choice here : ")
            match choice:
                case "create_event":
                    self.create_event()
                    print()
                case "get_event_details":
                    self.getEventDetails()
                    print()
                case "get_available_seats":
                    self.getAvailableNoOfTickets()
                    print()
                case "book_tickets":
                    num_tickets = int(input("Please enter the number of tickets you want to book : "))
                    self.book_tickets(num_tickets)
                    print()
                case "cancel_tickets":
                    booking_id = int(input("Please enter your booking id here : "))
                    self.cancel_booking(booking_id)
                    print()
                case "exit":
                    break
                case _:
                    print("Invalid input! Please Try Again.")
                    print("We're heading you to main menu.")
        print("Thanks for visiting our platform to book tickets. Hope to see you soon.")


dbutil = DBUtil()
events = TicketBookingSystem(dbutil)
events.main()
