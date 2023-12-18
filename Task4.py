class Train:
    def __init__(self, train_id, capacity):
        self.train_id = train_id
        self.capacity = capacity
        self.tickets_sold = 0

    def sell_ticket(self):
        if self.tickets_sold < self.capacity:
            self.tickets_sold += 1
            return f"Ticket for Train {self.train_id} sold successfully."
        else:
            return f"Train {self.train_id} is full. No more tickets available."

class TicketingSystem:
    def __init__(self):
        self.trains = {}

    def add_train(self, train_id, capacity):
        if train_id not in self.trains:
            self.trains[train_id] = Train(train_id, capacity)

    def sell_ticket(self, train_id):
        if train_id in self.trains:
            return self.trains[train_id].sell_ticket()
        else:
            return "Train not found."

# Example usage with user input
ticketing_system = TicketingSystem()

while True:
    print("\nCommands:")
    print("1. Add Train")
    print("2. Sell Ticket")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        train_id = input("Enter train ID: ")
        capacity = int(input("Enter train capacity: "))
        ticketing_system.add_train(train_id, capacity)
        print(f"Train {train_id} added with a capacity of {capacity}.")

    elif choice == "2":
        train_id = input("Enter train ID to sell ticket: ")
        result = ticketing_system.sell_ticket(train_id)
        print(result)

    elif choice == "3":
        print("Exiting the Ticketing System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
