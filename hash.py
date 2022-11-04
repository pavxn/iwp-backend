import hashlib
import time
from datetime import date

def email_hash(email_id : str):
    m = hashlib.md5(email_id.encode())
    return  str(m.hexdigest())

def blog_hash(user_id: str):
    user_id += str(time.time())
    m = hashlib.md5(user_id.encode())
    return  str(m.hexdigest())

def get_date():
    return date.today().strftime("%B %d, %Y")