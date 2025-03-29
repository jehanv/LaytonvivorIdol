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

@ slash_command("talk", description="Talk to Artie.", scopes=[876571805572300851])
async def talk(ctx):
    m = "Greetings, visitor! Welcome to my Gallery. Apologies for the smell. I had a bit of a snack earlier. Do try to ignore it, so that you may enjoy the paintings. Like this one here! A landscape painted just outside the city, in Akbadain. I believe it was around point I. The lovely lone cactus, lacking even a flower to keep it any company. Such a lustrous and meaningful image."
    await ctx.send(m)
    await messagelink.send_message(ctx.author, "Talk to Artie.", bot.user, m, 'montsarton-gallery')

bot.start(TOKEN)
