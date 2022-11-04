from typing import List
from pydantic import BaseModel
class User(BaseModel):
    fname : str 
    lname : str
    user_id : str
    email_id : str
    passw : str 
    blogs : List[str] = []
    
class NewUser(BaseModel):
    fname : str 
    lname : str
    email_id : str
    passw : str 

class BlogPost(BaseModel):
    blog_id : str
    user_id : str
    last_edited : str
    title : str
    desc : str
    content : str


class UpdateUser(BaseModel):
    user_id : str
    fname : str
    lname : str
    passw : str