from pydantic import BaseModel ,Field
from datetime import datetime, timezone

class BlogBase(BaseModel):
    title: str =Field (max_length=100)
    text : str =Field (max_length=300)
    
    
    
    
    
class BlogCreate(BlogBase)    :
    pass
    

class BlogUpdate(BlogBase):
    title: str=Field(max_length=100,default=None)
    text: str=Field(max_length=300,default=False)
    
class BlogOut(BlogBase):
   id: int 
   text: str=Field(max_length=100)
   
   time :datetime =Field(default_factory=lambda: datetime.now(timezone.utc))
   

    