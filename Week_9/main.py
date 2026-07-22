from ticket import create_ticket
from display import display_ticket


def main():
    name, student_id, issue, location, priority, technician, status = create_ticket()

    if technician == "Unassigned":
        print("\nInvalid priority entered. Please use High, Medium, or Low.")
        return

    display_ticket(name, student_id, issue, location, priority, technician, status)


if __name__ == "__main__":
    main()
