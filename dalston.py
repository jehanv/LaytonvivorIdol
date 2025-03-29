import logging
import asyncio

from naff import Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen
from naff import ( Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes,  )
import gspread
import messagelink
intents = Intents.DEFAULT

gc = gspread.service_account(filename="./service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

bot = Client(default_prefix='!', sync_interactions=True, intents=intents, send_command_tracebacks=False)
TOKEN = "" # Token hidden for security reasons

@slash_command("talk", description="Talk to Dalston.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 7).value == "FALSE":
        m = "Well, well. Did Layton send you? He always was putting his nose around, trying to solve each and every puzzle thrown his way. Well, let's see how you fare with this one! \n```ml\nPUZZLE NO. 005 \n\n\"Mice are famous for their ability to multiply at breakneck speeds. The type of mouse we have here gives birth once a month, birthing 12 babies each time. Baby mice mature and can give birth two months after they are born. You picked up one of these darling baby mice at the pet shop and brought it home the day after it was born. In 10 months from now, assuming you don't buy anymore, how many mice will you have?\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Dalston.", bot.user, m, 'dalston-mansion')
    else:
        m = "...wow, not bad. There ain't too many folks around that can just chew through a puzzle like that one! I bet you'd be good at balancing! Especially around H, since there aren't any annoying cactuses around. Or is it cacti? I always forget, because my brain is just spinning around as of late. I always feel like I'm losing my balance!"
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Dalston.", bot.user, m, 'dalston-mansion')

bot.start(TOKEN)
