# config/config.py
from dotenv import load_dotenv
import os
load_dotenv()

MOTHERDUCK_TOKEN = os.getenv('MOTHERDUCK_TOKEN')
if not MOTHERDUCK_TOKEN:
    raise ValueError("Please set MOTHERDUCK_TOKEN environment variable")