import datetime

from Service.IEventServiceProvider import IEventServiceProvider


class EventServiceProviderImpl(IEventServiceProvider):
    def __init__(self, dbUtil):
        self.dbUtil = dbUtil

    def create_event(self):
        event_name = input("Enter event name : ")
        date = input("Enter event Date : ")
        event_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        time = input("Enter event time in format HH:MM:SS : ")
        event_time = datetime.datetime.strptime(time, "%H:%M:%S").time()
        venue = input("Enter venue name : ")
        total_seats = int(input("Enter total seats : "))
        available_seats = int(input("Enter available seats : "))
        ticket_price = float(input("Enter ticket price : "))
        event_type = input("Enter event type : ")
        cursor = self.dbUtil.getDBConnection()
        query = "insert into venue (venue_name) values (%s)"
        cursor.execute(query, (venue, ))
        self.dbUtil.con.commit()
        cursor.execute("select venue_id from venue where venue_name=%s", (venue, ))
        venue_id = cursor.fetchone()
        createEvent = ("insert into events (event_name,event_date,event_time,venue_id,total_seats,available_seats,ticket_price,event_type) values (%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(createEvent, (event_name, event_date, event_time, venue_id[0], total_seats, available_seats, ticket_price, event_type, ))
        self.dbUtil.con.commit()
        cursor.execute("select * from events")
        rows = cursor.fetchall()
        for row in rows:
            print(row[-1])
        print(f"Event id for this event is {rows[-1][0]}")
        print("Event created successfully you can see the details above.")

    def getEventDetails(self):
        cursor = self.dbUtil.getDBConnection()
        cursor.execute("select * from events")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def getAvailableNoOfTickets(self):
        cursor = self.dbUtil.getDBConnection()
        query = "select event_name from events"
        cursor.execute(query)
        event_names = cursor.fetchall()
        print("Please select one events from below : ")
        for event in event_names:
            print(event)
        take_event = input("Please type your event name here correctly : ")
        query = "select available_seats from events where event_name=%s"
        cursor.execute(query, (take_event, ))
        seats = cursor.fetchall()
        print(seats)

