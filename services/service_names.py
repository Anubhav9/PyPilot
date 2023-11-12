"""All Services would be onboarded here"""

import os

env=os.environ.get("ENV","local")


if(env=="production"):
    # Using SendGrid URL to showcase on how to onbard a new URL
    SEND_GRID_URL=""

elif(env=="staging" or env=="local"):
    SEND_GRID_URL=""