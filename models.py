from typing import List
from fastapi import Form
from pydantic import BaseModel
class User(BaseModel):
    fname : str 
    lname : str
    user_id : int
    email_id : str
    passw : str 
    blogs : List[int] = []
    

class BlogPost(BaseModel):
    blog_id : int
    user_id : int
    title : str
    desc : str
    content : str
