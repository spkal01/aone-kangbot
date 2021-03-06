# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """


from userbot import CMD_HELP, is_mongo_alive, is_redis_alive, ALIVE_NAME
from userbot.events import register

# ================= CONSTANT =================
if ALIVE_NAME is not None:
    DEFAULTUSER = str(ALIVE_NAME)
else:
    DEFAULTUSER = "User"
# ============================================


@register(outgoing=True, pattern="^.dbs$")
async def amireallydbs(dbs):
    if not is_mongo_alive() and not is_redis_alive():
        db = "Both Mongo and Redis Database seems to be failing!"
    elif not is_mongo_alive():
        db = "Mongo DB seems to be failing!"
    elif not is_redis_alive():
        db = "Redis Cache seems to be failing!"
    else:
        db = "Databases functioning normally!"
    await dbs.edit("`"
                   f"User: {DEFAULTUSER} \n"
                   f"Database status: {db}\n"
                   f"OpenUserBot Version: v7.7.7"
                   "`")


CMD_HELP.update(
    {"db": ".dbs\n"
     "Usage: Shows database related info."})
