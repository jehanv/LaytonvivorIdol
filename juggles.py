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

@ slash_command("talk", description="Talk to Juggles.", scopes=[876571805572300851])
async def talk(ctx):
    m = "Well how do you do there? The name's Juggles, and I'm a clown! Although, most people guess that immediately. In need of any help? Perhaps a tour around town? Hey, don't you mock me, fella! I'll have you know I've got myself a PhD! In what, you ask? Clown Theory and Existential Enigma-nomics, what else? I'm no dunce, I'm no novice! Well, maybe a bit of a novice in that I just started juggling... but I'm quite skilled at it nonetheless! a regular doyen, I am! I once juggled two cactuses-- no, that ain't right, cacti-- in the middle of the desert, mind you, at K, even with their spikes and whatnot! Admittedly, I grabbed the flowers on each of them, but that's just a further testament to my talent! ...oh, sorry, didn't mean to be rude there. I'm not too privy to disrespect is all. How about I make it up to you with that tour promised earlier, huh? How about it?"
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to Juggles.", bot.user, m, 'carnival-arcade')

bot.start(TOKEN)
