from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_1 import Base, User, Ticket, Event
from datetime import datetime

DATABASE_URL = "sqlite:///tikiti.db"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)


def initialize_database():
    """Create tables if they do not exist."""
    Base.metadata.create_all(engine)



def create_user(session):
    name = input("Enter user name: ")
    email = input("Enter email: ")

    user = User(name=name, email=email)
    session.add(user)
    session.commit()

    print(f"User created: {user.name} (ID: {user.id})")


def delete_user(session):
    user_id = int(input("Enter user ID to delete: "))
    user = session.query(User).filter_by(id=user_id).first()

    if not user:
        print("User not found!")
        return

    session.delete(user)
    session.commit()
    print("User deleted!")



def create_event(session):
    name = input("Event name: ")
    date_str = input("Event date (YYYY-MM-DD): ")
    venue = input("Venue: ")
    description = input("Description (optional): ")

   
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        date_formatted = date_obj.strftime("%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Using input as-is.")
        date_formatted = date_str

    event = Event(name=name, date=date_formatted, venue=venue, description=description)
    session.add(event)
    session.commit()

    print(f"Event created: {event.name} (ID: {event.id})")


def update_event(session):
    event_id = int(input("Event ID to update: "))
    event = session.query(Event).filter_by(id=event_id).first()

    if not event:
        print("Event not found!")
        return

    event.name = input(f"New name ({event.name}): ") or event.name
    event.venue = input(f"New venue ({event.venue}): ") or event.venue
    event.description = input(f"New description ({event.description}): ") or event.description

    session.commit()
    print("Event updated!")



def create_ticket(session):
    ticket_type = input("Ticket type: ")
    price = int(input("Price: "))

    event_id = int(input("Event ID: "))
    event = session.query(Event).filter_by(id=event_id).first()
    if not event:
        print("Error: Event not found!")
        return

    user_id = int(input("User ID: "))
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("Error: User not found!")
        return

    ticket = Ticket(ticket_type=ticket_type, price=price, event_id=event_id, user_id=user_id)
    session.add(ticket)
    session.commit()
    print(f"Ticket created: ID {ticket.id}")



def view_users(session):
    users = session.query(User).all()
    print("\n--- Users ---")
    for u in users:
        print(f"{u.id}: {u.name} - {u.email}")


def view_events(session):
    events = session.query(Event).all()
    print("\n--- Events ---")
    for e in events:
        print(f"{e.id}: {e.name} on {e.date} at {e.venue}")


def view_tickets(session):
    tickets = session.query(Ticket).all()
    print("\n--- Tickets ---")
    for t in tickets:
        print(f"{t.id}: {t.ticket_type} - KES {t.price} (User {t.user_id}, Event {t.event_id})")



def main_menu():
    print("""
======== TIKITI APP ========
1. Create User
2. Create Event
3. Create Ticket
4. View Users
5. View Events
6. View Tickets
7. Delete User
0. Exit
============================
""")


def run():
    initialize_database()
    session = Session()

    while True:
        main_menu()
        choice = input("Choose option: ")

        if choice == "1":
            create_user(session)
        elif choice == "2":
            create_event(session)
        elif choice == "3":
            create_ticket(session)
        elif choice == "4":
            view_users(session)
        elif choice == "5":
            view_events(session)
        elif choice == "6":
            view_tickets(session)
        elif choice == "7":
            delete_user(session)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    run()
