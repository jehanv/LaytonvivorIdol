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

@ slash_command("talk", description="Talk to Pascal.", scopes=[876571805572300851])
async def talk(ctx):
    m = "Welcome to the Dromedary Hotel, friend. Tell me, do you know about picrats? Each puzzle given to you by the people of Monte d'Or will offer a certain number of picrats. Once you get enough picrats, you'll be able to talk to the professor and have him find your treasure. However, be warned. If you get a puzzle wrong, you'll lose five picrats, and losing enough picrats could cause you to be locked out of getting Layton's help, so only solve a puzzle when you're sure you know the answer."
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to the parrot.", bot.user, m, 'dromedary-lobby')

bot.start(TOKEN)
