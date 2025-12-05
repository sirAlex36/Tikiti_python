# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from lib.models import Base, User, Event, Ticket

DATABASE_URL = "sqlite:///tikiti.db"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def seed_data():
    Base.metadata.create_all(engine)

    session = Session()

    user1 = User(name="Kahush", email="kahush@example.com")
    user2 = User(name="Mercy", email="mercy@example.com")

    session.add_all([user1, user2])
    session.commit()

    event1 = Event(
        name="Music Festival",
        date=datetime.strptime("2025-08-12", "%Y-%m-%d").date(),
        venue="KICC Grounds",
        description="Annual music festival"
    )
    event2 = Event(
        name="Tech Conference",
        date=datetime.strptime("2025-10-01", "%Y-%m-%d").date(),
        venue="Sarit Expo Center",
        description="Technology and innovation conference"
    )

    session.add_all([event1, event2])
    session.commit()

    ticket1 = Ticket(ticket_type="VIP", price=5000, event_id=event1.id, user_id=user1.id)
    ticket2 = Ticket(ticket_type="Regular", price=2000, event_id=event2.id, user_id=user2.id)

    session.add_all([ticket1, ticket2])
    session.commit()

    print("Db seeded successfully!")

    session.close()


if __name__ == "__main__":
    seed_data()
