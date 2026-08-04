from passlib.context import CryptContext
from datetime import datetime, timedelta 
import jwt


ENCRYPYT_ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated="auto")

def encrypt_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hash):
    hash_pass = pwd_context.hash(password)
    return hash_pass == hash

def _generate_token(user_data: dict, auth_key: str, minutes=15):
    base = {
        "user_data" : {k: v for k,v in user_data.items()},
        "created_at": datetime.timestamp(datetime.now()),
        "expires_at": datetime.timestamp(datetime.now() + timedelta(minutes=minutes)),
        "is_valid": True
    }
    token = jwt.encode(base, auth_key, ENCRYPYT_ALGORITHM)
    return token

def verify_token():
    pass