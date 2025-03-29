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

@slash_command("talk", description="Talk to Gonzales.", scopes=[876571805572300851])
async def talk(ctx):
    m = "Ah, please forgive the dog, he does get quite anxious so when the master is away. ...and when he's here, which he is now. Although he is often away, searching for the precious ruins. He tells great stories of his journeys, like the one of a stunning flower on a cactus near B."
    await ctx.send(m, ephemeral=True)
    await messagelink.send_message(ctx.author, "Talk to Gonzales.", bot.user, m, 'dalston-mansion')

bot.start(TOKEN)
