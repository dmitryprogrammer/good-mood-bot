from dotenv import load_dotenv
from os import getenv

load_dotenv()

print(getenv("HOST_VAR"))