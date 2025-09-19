import os
from dotenv import load_dotenv

load_dotenv(".env")


required_env = [
    "SSH_PASSPHRASE",
    "SSH_HOST"
]


for env in required_env:
    if not os.environ.get(env):
        raise Exception(f"Missing env variable: {env}")