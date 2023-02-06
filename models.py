from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,Mapped
from database import Base

class Students(Base):
    __tablename__ = "signup_students"

    # id = Column(Integer,index=True)
    name = Column(String)
    Age = Column(Integer)
    Gender = Column(String)
    Address_line_1 = Column(String)
    Address_line_2 = Column(String)
    City = Column(String)
    State = Column(String)
    Pincode= Column(Integer)
    Country = Column(String)
    Phone = Column(Integer)
    email = Column(String,nullable=False,primary_key=True)
    institute= Column(String)

    food_consumed=relationship("Consumption",back_populates="user")

class StudentOrder(Base):
    __tablename__="studentorders_internalvendor"
    id = Column(Integer,index=True, primary_key=True)
    name = Column(String)
    Address_line_1 = Column(String)
    Address_line_2 = Column(String)
    Phone = Column(Integer)
    date = Column(String)
    email = Column(String)
    institute= Column(String)
    items=Column(String)
    quantities=Column(String)
    prices=Column(String)
    outlet_name=Column(String)


class Consumption(Base):
    __tablename__ = "food_consumed"
   
    student_phone = Column(Integer,ForeignKey("signup_students.Phone",ondelete="CASCADE"),primary_key=True,nullable=False) 
    date = Column(String)
    type = Column(String)
    total_calories = Column(Integer)

    user=relationship("Students",back_populates="food_consumed")

class SessionModel(Base):
    __tablename__="student_session"
    
    sessionId = Column(String, primary_key=True)
    email = Column(String)

class ConsumptionHistory(Base):
    __tablename__="consumption_history"
    id = Column(Integer,index=True, primary_key=True)
    user_id = Column(String)
    date = Column(String)
    consumed= Column(String)
    mess_name = Column(String)
    institute=Column(String)
    calories_breakfast=Column(Integer)
    calories_lunch=Column(Integer)
    calories_snacks=Column(Integer)
    calories_dinner=Column(Integer)

class StudentRating(Base):
    __tablename__ = 'student_rating'
    id = Column(Integer,index=True, primary_key=True)
    consumer_email = Column(String)
    outlet_name = Column(String)
    item=Column(String)
    rating = Column(Integer)
    


    



