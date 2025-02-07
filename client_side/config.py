from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")
private_group_id = os.getenv("PRIVATE_GROUP_ID")
