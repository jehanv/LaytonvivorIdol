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

@ slash_command("talk", description="Talk to Firth.", scopes=[876571805572300851])
async def talk(ctx):
    m = "When I was younger, this area was mostly sand, and rumors of Akbadain were aplenty. I once searched for the entrance, and then lo and behold! After a flower got stuck in my beard, I sneezed, and before I knew it, I had fallen right into the ruins. Though... with my old body I didn't make it all that far... in fact, I'm feeling tired just from the explanation... give me a moment..."
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to Firth.", bot.user, m, 'city-monument')

bot.start(TOKEN)
