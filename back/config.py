from dotenv import load_dotenv
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def conf():
    load_dotenv(ROOT_DIR+"/.config")
    config = {
        "HOST": os.getenv('HOST'),
        "DATABASE": os.getenv('DATABASE'),
        "DATABASE_TYPE": os.getenv('DATABASE_TYPE'),
        "USERNAME": os.getenv('DBUSER'),
        "PASSWORD": os.getenv('PASSWORD'),
        "TOKEN_KEY": os.getenv('TOKEN_KEY'),
        "Authorization": os.getenv('Authorization'),
        "IMAGE_ACCOUNT_ID": os.getenv('IMAGE_ACCOUNT_ID'),
        "DOCS": os.getenv('DOCS')
    }
    return config