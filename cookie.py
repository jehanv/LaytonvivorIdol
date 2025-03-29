import logging
import asyncio


from naff import Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen, ComponentContext
from naff import ( Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes,  )

import gspread
import messagelink
gc = gspread.service_account(filename="./service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

intents = Intents.DEFAULT

bot = Client(default_prefix='!', sync_interactions=True, intents=intents, send_command_tracebacks=False)
TOKEN = "" # Token hidden for security reasons

@ slash_command("talk", description="Talk to Cookie.", scopes=[876571805572300851])
async def talk(ctx):
    m = "Hiya! You wouldn't happen to know where my mom is, would you? She gets lost a lot, and I always have to go out and find her. It's pretty annoying. ...No. Why would I be the one wandering off?! I've only wandered once in my life, and I walked right into a cactus! Since then I try to stay focused. The flower there was pretty though. Where was this? uh... i think it was around J. You're welcome! Tell me if you see my mom!"
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to Cookie", bot.user, m, 'knickknack-alley')

bot.start(TOKEN)
