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

@slash_command("talk", description="Talk to Tanya.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 10).value == "FALSE":
        m = "Oh, hi there! Sorry, I don't know anything about the Akbadain Ruins. I do have this fun puzzle, if you want it! \n```ml\nPUZZLE NO. 008 \n\n\"Tanya tells you that out of the seven people, A, B, C, D, E, F, and L, some of them are liars. You can tell which ones are lying, because they have a white shirt. Here is what each of them said:\nA: I'm not a liar. Neither is F.\nB: A usually has a white shirt.\nC: hey, why am I wearing blue? My shirt is normally white!\nD: A is telling the truth.\nE: I most certainly did not drop blue paint on C. \nF: I don't think B is lying, since his shirt is very red.\nL: D is really suspicious... he could be lying.\nWho are the liars?\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle! When solving the puzzle, put your answers in a comma seperated list, such as `A, B, C, D`.", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Tanya.", bot.user, m, 'merchant-district')
    else:
        m = "Great job! You deserve some picarats for that puzzle!"
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Tanya.", bot.user, m, 'merchant-district')

bot.start(TOKEN)
