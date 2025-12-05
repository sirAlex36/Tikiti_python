from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime 

Base = declarative_base()

class User(Base):

  __tablename__= 'users'
  id= Column(Integer, primary_key=True)
  name= Column(String, nullable= False)
  email= Column(String, nullable=False, unique=True)
  created_at = Column(DateTime, default=datetime.utcnow)

  #relationship
  tickets = relationship("Ticket", back_populates="user")


class Event(Base):

  __tablename__='events'
  id= Column(Integer, primary_key=True)
  name= Column(String, nullable=False)
  date = Column(String, nullable=False)
  venue= Column(String, nullable=False)
  description = Column(Text, nullable=True)
  created_at = Column(DateTime, default=datetime.utcnow)

  #relationship
  tickets = relationship('Ticket', back_populates= 'event')
  

class Ticket(Base):

  __tablename__='tickets'
  id= Column(Integer, primary_key=True)
  ticket_type= Column(String, nullable=False)
  price= Column(Integer, nullable=False)
  event_id= Column(Integer, ForeignKey('events.id'))
  user_id= Column (Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.utcnow)

  #relationship
  event = relationship('Event', back_populates='tickets')
  user = relationship("User", back_populates="tickets")


  








