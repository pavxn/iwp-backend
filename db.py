from http import client
from unittest import result
from models import *
from motor import motor_asyncio

client = motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://iwp:iwp123@cluster0.u0lqc19.mongodb.net/?retryWrites=true&w=majority"
)

blog_collection = client.IWP.blogs
user_collection = client.IWP.users

async def get_blogs():
    blogs = []
    curs = blog_collection.find({})
    async for doc in curs:
        blogs.append(BlogPost(**doc))

    return blogs

async def get_one_blog(blog_id):
    doc = await blog_collection.find_one({"blog_id" : blog_id})
    return doc

async def create_blog(blog):
    result = await blog_collection.insert_one(blog.dict())
    return blog


async def create_user(user):
    result = await user_collection.insert_one(user)
    return user

async def get_one_user(email_id):
    doc = await user_collection.find_one({"email_id" : email_id})
    return doc

