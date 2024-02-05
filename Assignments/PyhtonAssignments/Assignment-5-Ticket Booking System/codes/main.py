# task1 = Task1()
# task1.checkTicketAvailability()
# task1.calculateTotalCost()
# task1.looping()
import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Kevink25*",
    database="ticketbookingsystem"
)
venue = "Harmony Hall"
cur = con.cursor()
cur.execute("select venue_id from venue where venue_name= %s", (venue,))
venue_id = cur.fetchone()
print(venue_id[0])
"""
    event = {
        "event_name" : input("Enter the event name : "),
        "event_date" : input("Enter the date of the event : "),
        "event_time" : input("Enter Event timing : "),
        "venue_name" : input("Enter venue name : "),
        "total_seats" : int(input("Enter total seats")),
        "available_seats" : int(input("Enter available seats : ")),
        "ticket_price" : float(input("Enter the ticket price : ")),
        "event_type" : input("Enter event type : ")
    }
    
    booking = Booking(event)
    print(booking.getBookedNoOfTickets())
 #   first_event = Event(event)
  #  first_event.display_event_details()
"""
