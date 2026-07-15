from passlib.context import CryptContext

ENCRYPYT_ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated="auto")

def encrypt_password(password: str):
    return pwd_context.hash(password)