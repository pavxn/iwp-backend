from hash import blog_hash, get_date
from models import *
from motor import motor_asyncio
from pymongo import ReturnDocument

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
    blog.blog_id = blog_hash(blog.user_id)
    blog.last_edited = get_date()
    await blog_collection.insert_one(blog.dict())
    blog_user = await get_one_user(blog.user_id)
    blog_user["blogs"].append(blog.blog_id)
    await update_user(blog.user_id, blog_user)
    return blog

async def update_blog(blog_id, blog : BlogPost):
    doc = await blog_collection.find_one_and_update(
        {"blog_id" : blog_id}, {"$set" : blog},
        return_document = ReturnDocument.AFTER
    )

    return doc
async def remove_blog(blog_id, user_id):
    result = await blog_collection.delete_one({"blog_id" : blog_id})
    
    if result.deleted_count > 0:
        doc = await get_one_user(user_id)
        print(doc['blogs'])
        doc["blogs"] = doc["blogs"].remove(blog_id)
        if not doc['blogs'] :  doc['blogs'] = []
        if user := await update_user(user_id, doc):
            return 200

    return None

async def create_user(user):
    emails = await get_email_ids()
    if user["email_id"] not in emails:
        print(user)
        result = await user_collection.insert_one(user)
        return user["user_id"]
    
    return None

async def get_users():
    blogs = []
    curs = user_collection.find({})
    async for doc in curs:
        blogs.append(User(**doc))

    return blogs
async def get_one_user(user_id):
    doc = await user_collection.find_one({"user_id" : user_id})
    return doc

async def get_one_user_by_email(user_id):
    doc = await user_collection.find_one({"email_id" : user_id})
    return 

async def update_user(user_id, user : User):
    doc = await user_collection.find_one_and_update(
        {"user_id" : user_id}, {"$set" : user},
        return_document = ReturnDocument.AFTER
    )

    return doc  

async def remove_user(user_id):
    user = await user_collection.find_one({"user_id" : user_id})
    blogs = user['blogs']
    print(blogs)
    for blog_id in blogs:
        await blog_collection.delete_one({"blog_id" : blog_id})
        

    await user_collection.delete_one({"user_id" : user_id})

    return 200

async def get_email_ids():
    emails = []
    curs = user_collection.find({})
    async for doc in curs:
        emails.append(doc["email_id"])

    return emails

