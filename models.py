from database import Base, engine
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String ,Integer,Boolean,DateTime, ForeignKey
from datetime import datetime,timezone
from database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(length=100))
    last_name: Mapped[str] = mapped_column(String(length=100))

    users: Mapped['Blog'] = relationship(back_populates='user',
                                         cascade='all, delete-orphan')


class Blog(Base):
    __tablename__='blogs'
    
    
    
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    title:Mapped[str]=mapped_column(String(length=100))
    text:Mapped[str]=mapped_column(String(length=300))
    time:Mapped[datetime]=mapped_column(DateTime,default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='users')