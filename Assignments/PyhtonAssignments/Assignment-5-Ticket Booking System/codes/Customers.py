

class Customer:
    def __init__(self, customer_name, email, phone):
        self.customer_name = customer_name
        self.email = email
        self.phone = phone

    def display_customer_details(self):
        print(f"Customer Name : {self.customer_name}")
        print(f"Email : {self.email}")
        print(f"Phone Number : {self.phone}")