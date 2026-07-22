
def create_ticket():
    print("=== IT Helpdesk Ticket ===")

    name = input("Student Name : ")
    student_id = input("Student ID : ")
    issue = input("Issue : ")
    location = input("Location : ")
    priority = input("Priority (High/Medium/Low): ")

    # Assign technician based on priority level
    if priority.lower() == "high":
        technician = "Ahmad"
    elif priority.lower() == "medium":
        technician = "Siti"
    elif priority.lower() == "low":
        technician = "Ali"
    else:
        technician = "Unassigned"

    status = "Pending"

    return (name, student_id, issue, location, priority, technician, status)
