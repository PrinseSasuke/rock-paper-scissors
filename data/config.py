import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admin_id = [
1057421566
]
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
ip = os.getenv("ip")
POSTGRESS_URI =f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
