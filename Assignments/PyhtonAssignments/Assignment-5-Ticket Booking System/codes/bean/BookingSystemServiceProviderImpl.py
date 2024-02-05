from Service.IBookingSystemServiceProvider import IBookingSystemServiceProvider
from datetime import date


class BookingSystemServiceProviderImpl(IBookingSystemServiceProvider):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def calculate_booking_cost(self, num_tickets):
        pass

    def book_tickets(self, num_tickets):
        print("Please enter customer details so we can assure booking : ")
        customer_name = input("First please enter your name : ")
        customer_email = input("Please enter you email : ")
        customer_phone = input("Please enter your phone number : ")
        cursor = self.dbUtil.getDBConnection()
        cursor.execute("insert into customer(customer_name,email,phone_number) values (%s,%s,%s)",
                       (customer_name, customer_email, customer_phone,))
        self.dbUtil.con.commit()
        cursor.execute("select customer_id from customer where customer_name=%s", (customer_name,))
        customer_row = cursor.fetchone()
        if customer_row:
            customer_id = customer_row[0]
        print("Please select one events from the events listed below : ")
        cursor.execute("select event_name from events")
        events = cursor.fetchall()
        for event in events:
            print(event[0])
        name_of_event = input("Enter your event here : ")
        cursor.execute("select event_id,ticket_price from events where event_name = %s", (name_of_event,))
        rows = cursor.fetchone()
        if rows:
            event_id, price = rows
        total_cost = price * num_tickets
        today = date.today()
        query = "insert into bookings (customer_id, event_id, num_tickets, total_cost, booking_date) values (%s,%s,%s,%s,%s)"
        cursor.execute(query, (customer_id, event_id, num_tickets, total_cost, today))
        self.dbUtil.con.commit()
        cursor.execute("select booking_id from bookings where customer_id = %s", (customer_id,))
        booking_id = cursor.fetchone()
        if booking_id:
            b_id = booking_id[0]
        print("Congratulations. Your booking is confirmed. Your booking id is ", b_id)

    def cancel_booking(self, booking_id):
        cursor = self.dbUtil.getDBConnection()
        query = "delete from bookings where booking_id = %s"
        cursor.execute(query, (booking_id,))
        self.dbUtil.con.commit()
        print("Your booking is cancelled successfully.")


    def get_booking_details(self, booking_id):
        pass
