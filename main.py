from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from models import *
from db import *

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/blog/")
async def get_all_blogs():
    response = await get_blogs()
    return response


@app.get("/blog/{blog_id}", response_model=BlogPost)
async def get_blog_by_id(blog_id):
    response = await get_one_blog(blog_id)
    if response:
        return response


@app.post("/blog/", response_model=BlogPost)
async def post_blog(blog : BlogPost):
    response = await create_blog(blog)
    if response:
        return response

@app.post("/user/", response_model=User)
async def post_user(
    firstname : str = Form(),
    lastname : str = Form(),
    email : str = Form(),
    password : str = Form()
    ):

    user = {
        "fname" : firstname,
        "lname" : lastname,
        "user_id" : 1,
        "email_id" : email,
        "passw" : password,
        "blogs" : []
    }

    response = await create_user(user)
    if response:
        return response

@app.post("/login/", response_model=User)
async def get_user_by_id(email_id):  
    response = await get_one_user(email_id)
    if response:
        return response

