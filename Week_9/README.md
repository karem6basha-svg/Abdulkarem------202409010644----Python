# IT Helpdesk Ticket Registration System

## Purpose
A simple command-line application for City University Malaysia's IT Support
team. It lets a student report a technical issue (LMS login, WiFi, printer,
password reset, etc.) and generates a helpdesk ticket before a technician
begins investigating.

## Tech stack
- Python 3
- Standard library only (no external packages)
- Modular design across three files:
  - `main.py` - program entry point, coordinates the flow
  - `ticket.py` - collects ticket details and assigns a technician
  - `display.py` - formats and prints the final ticket

## How to use
1. Make sure Python 3 is installed.
2. From the `week_9` directory, run:
   ```
   python3 main.py
   ```
3. Enter the requested details when prompted:
   - Student Name
   - Student ID
   - Issue
   - Location
   - Priority (High / Medium / Low)
4. The program automatically assigns a technician based on priority:
   - High -> Ahmad
   - Medium -> Siti
   - Low -> Ali
5. A formatted ticket summary is printed with status `Pending`.

![Demo](week_9 demo.gif)
