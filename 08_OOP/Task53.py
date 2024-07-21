'''
Write a Class Train which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Pakistani Railways
'''
import random
class Train():

    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no. {self.trainNo} from {fro} to {to}")

    def status(self):
        print(f"Train no. {self.trainNo} is moving successfully.")

    def fare(self,fro,to):
        print(f"Ticket fare in train no. {self.trainNo} from {fro} to {to} is {random.randint(300,5000)}")

t=Train(7)
t.book("Lahore", "Islamabad")
t.fare("Lahore", "Islamabad")
t.status()