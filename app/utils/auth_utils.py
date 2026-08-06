from passlib.context import CryptContext
from datetime import datetime, timedelta 
import jwt
import os

ENCRYPYT_ALGORITHM = "HS256"
AUTH_KEY = os.getenv("AUTHENTICATION_KEY")

pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated="auto")

def encrypt_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hash):
    return pwd_context.verify(password, hash)

def _generate_token(user_data: dict, auth_key: str = AUTH_KEY, minutes=15):
    base = {
        "user_data" : {k: v for k,v in user_data.items()},
        "created_at": datetime.timestamp(datetime.now()),
        "expires_at": datetime.timestamp(datetime.now() + timedelta(minutes=minutes)),
        "is_valid": True
    }
    print(base)
    token = jwt.encode(base, auth_key, ENCRYPYT_ALGORITHM)
    print(token)
    return token

def verify_token(token: str, auth_key=AUTH_KEY):
    base = jwt.decode(token, key=auth_key, algorithms=ENCRYPYT_ALGORITHM)
    pass
    