from app.database import add_employee, remove_employee

class HRM:
    @staticmethod
    def process_command(command):
        words = command.split()
        if words[0].lower() == "add":
            return add_employee(words[1], words[2])  # Add an employee
        elif words[0].lower() == "remove":
            return remove_employee(words[1])  # Remove an employee
        else:
            return "Invalid command. Use: Add, Remove."
