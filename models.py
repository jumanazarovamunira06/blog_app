from database import Base, engine
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String ,Integer,Boolean,DateTime
from datetime import datetime,timezone
from database import Base

class Blog(Base):
    __tablename__='blogs'
    
    
    #ID, sarlavha, matn, yaratilgan vaqti).
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    title:Mapped[str]=mapped_column(String(length=100))
    text:Mapped[str]=mapped_column(String(length=300))
    time:Mapped[datetime]=mapped_column(DateTime,default=datetime.now)