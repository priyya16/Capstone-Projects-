class CollegeEventManagement:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name):
        if event_name not in self.events:
            self.events[event_name] = []
        else:
            print(f"Event '{event_name}' already exists.")

    def add_participant(self, event_name, name, contact, department, status="Not Attended"):
        if event_name in self.events:
            self.events[event_name].append((name, contact, department, status))
        else:
            print(f"Event '{event_name}' does not exist.")

    def display_participants(self, event_name):
        if event_name in self.events:
            participants = self.events[event_name]
            if participants:
                print(f"\nParticipants for '{event_name}':")
                for p in participants:
                    print(f"Name: {p[0]}, Contact: {p[1]}, Department: {p[2]}, Status: {p[3]}")
            else:
                print(f"No participants registered for '{event_name}'.")
        else:
            print(f"Event '{event_name}' does not exist.")

    def search_participant(self, name):
        found = False
        for event, participants in self.events.items():
            for p in participants:
                if p[0].lower() == name.lower():
                    print(f"\nParticipant '{name}' found in '{event}' event:")
                    print(f"Contact: {p[1]}, Department: {p[2]}, Status: {p[3]}")
                    found = True
        if not found:
            print(f"Participant '{name}' not found.")

    def mark_attendance(self, name, status):
        found = False
        for event, participants in self.events.items():
            for i, p in enumerate(participants):
                if p[0].lower() == name.lower():
                    self.events[event][i] = (p[0], p[1], p[2], status)
                    print(f"Updated '{name}' status to '{status}' in '{event}' event.")
                    found = True
        if not found:
            print(f"Participant '{name}' not found.")

    def generate_summary(self):
        print("\nEvent Summary:")
        for event, participants in self.events.items():
            print(f"{event}: {len(participants)} participants")


# Interactive Menu
event_system = CollegeEventManagement()

while True:
    print("\n🎉 College Event Management System 🎉")
    print("1. Add Event")
    print("2. Add Participant")
    print("3. Display Participants")
    print("4. Search Participant")
    print("5. Mark Attendance")
    print("6. Generate Summary")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        event_name = input("Enter event name: ")
        event_system.add_event(event_name)
    elif choice == "2":
        event_name = input("Enter event name: ")
        name = input("Enter participant name: ")
        contact = input("Enter contact number: ")
        department = input("Enter department: ")
        event_system.add_participant(event_name, name, contact, department)
    elif choice == "3":
        event_name = input("Enter event name: ")
        event_system.display_participants(event_name)
    elif choice == "4":
        name = input("Enter participant name: ")
        event_system.search_participant(name)
    elif choice == "5":
        name = input("Enter participant name: ")
        status = input("Enter attendance status (Attended/Not Attended): ")
        event_system.mark_attendance(name, status)
    elif choice == "6":
        event_system.generate_summary()
    elif choice == "7":
        print("Exiting... Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please try again.")
