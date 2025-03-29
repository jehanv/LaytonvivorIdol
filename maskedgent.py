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

@ slash_command("talk", description="Talk to The Masked Gentleman.", scopes=[876571805572300851])
async def talk(ctx):
    m = "What are you doing here? Go back to your worthless Professor."
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to The Masked Gentleman.", bot.user, m, 'gallery-plaza')

bot.start(TOKEN)