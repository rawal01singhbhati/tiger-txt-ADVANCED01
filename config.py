import os

API_ID = API_ID = 16494736

API_HASH = os.environ.get("API_HASH", "2cb7fa5859e2de684e3e10d9c049621a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6527903308:AAE1tHzZVvQ2WPy7pEfGbFVKGenN8VWS3so")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5071104456))

LOG = -1002141027585

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5071104456").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


