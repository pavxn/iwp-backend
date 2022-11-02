from typing import List
from pydantic import BaseModel
class User(BaseModel):
    fname : str 
    lname : str
    user_id : str
    email_id : str
    passw : str 
    blogs : List[str] = []
    

class BlogPost(BaseModel):
    blog_id : str
    user_id : str
    title : str
    desc : str
    content : str

#class UpdateUser(BaseModel):