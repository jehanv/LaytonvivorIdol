import logging
import asyncio

from naff import Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen, ComponentContext
from naff import  (Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes,) 

import gspread
import messagelink

gc = gspread.service_account(filename="./service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

inten = Intents.DEFAULT

bot = Client(default_prefix='!', sync_interactions=True, intents=inten, send_command_tracebacks=False)
TOKEN = "" # Token hidden for security reasons

@prefixed_command()
async def starting(ctx):
    await ctx.send("To begin your quest around Monte d'Or, click the button below.", components=Button(ButtonStyles.GREEN, "Begin!"))


@listen()
async def on_component(event: ComponentContext):
    ctx = event.context
    row = worksheet.col_values(1).index('') + 1
    worksheet.update('A' + str(row) + ":X" + str(row), [[str(ctx.author.id), 0, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, 0, ctx.author.display_name]])
    m = "Ah, mon ami, it is good to meet you! My name is Aldus. I welcome you to Monte D'or! A fabulous place, as I am told. Now, you may be wondering how to speak to fine people like myself. Well, the answer to that is quite simple! All you have to do is press the `/` key, find the person you want to talk to, and press the talk command. Then send your message, and that person will respond to you! Why don't you try talking to me this way?"
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Start the idol hunt.", bot.user, m, 'dromedary-lobby')


@slash_command("talk", description="Talk to Aldus.", scopes=[876571805572300851])
async def talk(ctx):
    m="Well done, mon ami! You can talk to everyone else in this fabulous city by doing the exact same thing! You may journey through this magnificent city by simply saying '/move' and then the name of the channel you wish to go to. You can only travel to nearby locations of course. You should come across many puzzle-loving fellows throughout the city. Solving their puzzles will earn you picarats. If you guess wrong, you'll *lose* picrats. If you have enough picarats, you can travel to the Ruins of Akbadain! ...assuming you know where it is. If not, perhaps talk to the professor. He should be in his room. Now then, until we next meet, I bid you... adieu!"
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to Aldus.", bot.user, m, 'dromedary-lobby')

bot.start(TOKEN)
