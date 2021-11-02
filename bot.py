import os
import asyncio
import json
from typing import Dict, Optional, List

from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

from pyrogram.errors import MessageNotModified


class Config:
    API_ID = 5119765
    API_HASH = ("ab310ff746864c1a33f3c590f1598c06")
    BOT_TOKEN = ("1969588186:AAG_KlhwDyOGZm9c6WuaTROuEH-fJylSKnI")
    APP_NAME = os.environ.get("APP_NAME", None)
    API_KEY = os.environ.get("API_KEY", None)
    HU_APP = from_key(API_KEY).apps()[APP_NAME]


class Bot(Client):
    def __init__(self):
        kwargs = {
            'api_id': Config.API_ID,
            'api_hash': Config.API_HASH,
            'session_name': ':memory:',
            'bot_token': Config.BOT_TOKEN
        }
        super().__init__(**kwargs)

    async def start(self):
        await super().start()

    async def stop(self):
        await super().stop()

    async def sleep(self, msg):
        await msg.reply("`Sleeping for (10) Seconds.`")
        Config.HU_APP.restart()
