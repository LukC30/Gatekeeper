from passlib.context import CryptContext

ENCRYPYT_ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated="auto")

def encrypt_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hash):
    hash_pass = pwd_context.hash(password)
    return hash_pass == hash