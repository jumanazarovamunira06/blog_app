from pydantic import BaseModel ,Field
from datetime import datetime, timezone





class UserBase(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int
    
    
class BlogBase(BaseModel):
    title: str =Field (max_length=100)
    text : str =Field (max_length=300)
    
    
    
    
    
class BlogCreate(BlogBase)    :
    user_id: int 

class BlogUpdate(BlogBase):
    title: str=Field(max_length=100,default=None)
    text: str=Field(max_length=300,default=False)
    
    
class BlogDelete(BlogBase):
    pass
    
class BlogOut(BlogBase):
   id: int 
   user_id:int 
   
   time :datetime =Field(default_factory=lambda: datetime.now(timezone.utc))
   
   
model_config={"from_attributes":True}
    