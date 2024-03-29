from fastapi import FastAPI, HTTPException, Form, status
from fastapi.middleware.cors import CORSMiddleware
from models import *
from db import *
from hash import email_hash

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def test():
    return {'name' : 'pavan'}

@app.get("/blog/")
async def get_all_blogs():
    response = await get_blogs()
    return response


@app.get("/blog/{blog_id}", response_model=BlogPost)
async def get_blog_by_id(blog_id ):
    response = await get_one_blog(blog_id)
    if response:
        return response


@app.post("/blog/", response_model=BlogPost)
async def post_blog(blog : BlogPost):
    response = await create_blog(blog)
    if response:
        return response

@app.put("/blog/", )
async def put_blog(blog: BlogPost):
    response = await update_blog(blog.blog_id, blog)
    if response:
        return response

    raise HTTPException(500,
    f"Update could not be executed.")


@app.delete("/blog/")
async def delete_blog(blog_id , user_id):
    response = await remove_blog(blog_id, user_id)
    if response:
        return status.HTTP_200_OK

    raise HTTPException(500,
    f"Delete could not be executed.")

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
        "user_id" : email_hash(email),
        "email_id" : email,
        "passw" : password,
        "blogs" : []
    }

    response = await create_user(user)
    if response:
        return response

    raise HTTPException(409,
    f"Email ID {email} already exists.")


@app.put("/user/")
async def put_user(user : User):
    response = await update_user(user.user_id, user)
    if response:
        return response

    raise HTTPException(500,
    f"Update could not be executed.")

@app.delete("/user/")
async def delete_user(user_id : str):
    response = await remove_user(user_id)
    if response:
        return status.HTTP_200_OK

    raise HTTPException(500,
    f"Delete could not be executed.")
    
    
@app.get("/login/", response_model=User)
async def get_user_by_id(user_id : str):  
    response = await get_one_user_by_email(user_id)
    if response:
        return response


