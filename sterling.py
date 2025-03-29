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

@ slash_command("talk", description="Talk to Sterling.", scopes=[876571805572300851])
async def talk(ctx):
    m = "My name is Sterling. I'm a rich man. And you're not. So why should I bother speaking to you? What's that? Akbadain? Oh, that pitiful place. They tell of great stories, stories of unbelievable riches-- for most people, not for me-- but you try and find it, searching around F, and what do I get for it? I trip over a cactus, and almost scrape my favorite gold tooth! Ridiculous, the whole thing."
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to Sterling.", bot.user, m, 'dromedary-plaza')

bot.start(TOKEN)
