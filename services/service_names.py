"""
All Services would be onboarded here. The URLs will be different based on different envs

Author: Anubhav Sanyal
Creation Date:12/11/2023
"""

import os

env=os.environ.get("ENV","local")

if env=="production":
    # Using SendGrid URL to showcase on how to onbard a new URL
    SEND_GRID_URL=""

elif env=="staging" or env=="local":
    SEND_GRID_URL=""
