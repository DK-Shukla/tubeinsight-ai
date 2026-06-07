import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"

print("Looking for:", env_path)

load_dotenv(env_path)

print("KEY =", os.getenv("YOUTUBE_API_KEY"))