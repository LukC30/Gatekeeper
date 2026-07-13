import os
from dotenv import load_dotenv

def get_database_config() -> dict:
    load_dotenv()
    config = {
        'user_db' : "",
        'password' : "",
        'host' : "",
        'port' : "",
        'database' : ""
    }
    for key in config.keys():
        v = os.getenv(key.upper(), "")
        config[key] = v
    print(config)
    return config