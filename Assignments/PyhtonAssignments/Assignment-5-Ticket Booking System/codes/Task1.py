
class Task1:
    def __init__(self):
        print("First 3 tasks")

    def checkTicketAvailability(self):
        print("Please enter the available tickets and Number of required tickets")
        availableTickets = int(input())
        noOfTickets = int(input())
        if availableTickets > noOfTickets:
            print("Yes! The required number of tickets are available")
        else:
            print("Sorry! The tickets are not available as of now. Try again later.")

    def calculateTotalCost(self):
        ticketType = input("Please enter ticket type : ")
        noOfTickets = int(input("Please enter no of tickets : "))
        base = 0
        if ticketType == "Silver":
            base = 50
        elif ticketType == "Gold":
            base = 100
        elif ticketType == "Diamond":
            base = 150
        print(f"Total cost of tickets will be {base * noOfTickets}")

    def looping(self):
        ticketType = input("Please enter ticket type : ")
        while ticketType != "Exit":
            noOfTickets = int(input("Please enter no of tickets : "))
            base = 0
            if ticketType == "Silver":
                base = 50
            elif ticketType == "Gold":
                base = 100
            elif ticketType == "Diamond":
                base = 150
            print(f"Total cost of tickets will be {base * noOfTickets}")
            ticketType = input("Please enter ticket type : ")
