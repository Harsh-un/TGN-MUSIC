import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from UNMusic import LOGGER, app, userbot
from UNMusic.core.call import TGN
from UNMusic.misc import sudo
from UNMusic.plugins import ALL_MODULES
from UNMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await sudo()
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("TGNMusic.plugins" + all_module)
    LOGGER("UNMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await TGN.start()
    try:
        await UN.stream_call("https://graph.org/file/ec8a35dd5f1ef90947167.mp4")
    except NoActiveGroupCall:
        LOGGER("UNMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await UN.decorators()
    LOGGER("UNMusic").info(
        "UN Music Bot Started Successfully"
    )
    await idle()
    await app.stop()
    LOGGER("UNMusic").info("Stopping UN Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
