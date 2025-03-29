from naff import Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen, ComponentContext
from naff import ( Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes,  )

import gspread
import messagelink
intents = Intents.DEFAULT

gc = gspread.service_account(filename="./service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

bot = Client(default_prefix='!', sync_interactions=True, intents=intents, send_command_tracebacks=False)
TOKEN = "" # Token hidden for security reasons

@slash_command("talk", description="Talk to the parrot.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 5).value == "FALSE":
        m = "Squawk! I'm hungry! Squawk!"
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to the parrot.", bot.user, m, 'dromedary-plaza')
    else:
        m = "Squawk! *munch* Thank you! I'm going west now, which is left on that map of yours, and north is up, south is down, east is right. Just so that you know. Squawk!"
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to the parrot.", bot.user, m, 'dromedary-plaza')

bot.start(TOKEN)
