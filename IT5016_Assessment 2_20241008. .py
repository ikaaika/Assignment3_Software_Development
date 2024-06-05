  nimport random
import string

# these are the class tickets
class Ticket:
    ticketCounter = 2000
    openTickets = 0
    resolvedTickets = 0

    # ticket attributes
    def __init__(self, staffID, creatorName, contactEmail, desc):
        self.ticketNo = Ticket.ticketCounter
        Ticket.ticketCounter += 1
        self.staffID = staffID
        self.creatorName = creatorName
        self.contactEmail = contactEmail
        self.desc = desc
        self.response = "Not Yet Provided"
        self.status = "Open"
        self.openTickets += 1
        self.password = None

    # displaying ticket info
    def displayTicket(self):
        print(f"Ticket Number: {self.ticketNo}")
        print(f"Ticket Creator:{self.creatorName}")
        print(f"staff ID: {self.staffID}")
        print(f"Email Address: {self.contactEmail}")
        print(f"Description: {self.desc}")
        print(f"Response: {self.response}")
        if self.password:
            print(f"Password: {self.password}")
        print(f"Ticket Status: {self.status}\n")

    #submitting response
    def submitResponse(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.openTickets -= 1
        Ticket.resolvedTickets += 1

    # resolving password change request and closing ticket
    def resolvePC(self):
        if "password change" in self.desc.lower():  # checking for lowercase
            newPassword = self.generatePassword()
            self.response = f"password changed to: {newPassword}"
            self.status = "Closed"
            Ticket.openTickets -= 1
            Ticket.resolvedTickets += 1

            self.password = newPassword
    # initiating a new password
    def generatePassword(self):
        staffID_chars = self.staffID[:2]
        creatorName_chars = self.creatorName[:3]

        random_chars = ''.join(random.choices(string.ascii_letters, k=3))

        newPassword = staffID_chars + creatorName_chars + random_chars

        return newPassword

# reopening the closed ticket
    def reopenTicket(self):
        self.status = "Reopened"
        Ticket.openTickets += 1
        Ticket.resolvedTickets -= 1
# showing the ticket statistics
    @classmethod
    def ticket_stats(cls):
        return f"Tickets Created: {cls.ticketCounter - 2000}\nTickets Resolved: {cls.resolvedTickets}\nTickets To Solve: {cls.openTickets}"

# MAIN PROGRAM
def main():
    tickets = []

    while True:
        # Display menu for user interaction
        print("\nMenu:")
        print("1. Create a Ticket")
        print("2. Resolve The Ticket")
        print("3. Change The Password (if The Password requires changing)")
        print("4. View All Of The Tickets")
        print("5. View All Of The Open Tickets")
        print("6. View All Of The Closed Tickets")
        print("0 . Exit")
        choice = input("Enter your Option: ")

        if choice == "1":
            creatorName = input("Enter The Creator Name: ")
            staffID = input("Enter The Staff ID: ")
            contactEmail = input("Enter The Email Address: ")
            desc = input("Enter The Description: ")

            tickets.append(Ticket(staffID, creatorName, contactEmail, desc))
            print("Ticket constructed successfully.")
        elif choice == "2":
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. Ticket Number: {ticket.ticketNo} (Status: {ticket.status})")
            ticket_index = int(input("Enter the index of the ticket to resolve: ")) - 1
            if 0 <= ticket_index < len(tickets):
                response = input("Enter reply for the selected ticket: ")
                tickets[ticket_index].submitResponse(response)
                print("Ticket resolved successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "3":
            print("Open Tickets:\n")
            for i, ticket in enumerate(tickets, start=1):
                if ticket.status == "Open":
                    print(f"{i}. Ticket Number: {ticket.ticketNo} (Status: {ticket.status})")

            ticket_index = int(input("Enter the index of the Password Change Request to change the password: ")) - 1
            if 0 <= ticket_index < len(tickets):
                tickets[ticket_index].resolvePC()
                print("Password changed successfully. ")
            else:
                print("Invalid ticket index. ")
        elif choice == "4":
            print("\nAll Tickets:")
            for ticket in tickets:
                ticket.displayTicket()
            print("\nTicket Statistics:")
            print(Ticket.ticket_stats())
        elif choice == "5":
            print("\nOpen Tickets:\n")
            for ticket in tickets:
                if ticket.status == "Open":
                    ticket.displayTicket()
            print("\nTicket Statistics (Before Resolution and the Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "6":
            print("\nClosed Tickets:n")
            for ticket in tickets:
                if ticket.status == "Closed":
                    ticket.displayTicket()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "0":
                    #exit
            print("Exiting the program.")
            break
        else:
            print("Irrational option. Please enter a correct option.")

if __name__ == "__main__":
    main()

