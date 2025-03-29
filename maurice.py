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

@slash_command("talk", description="Talk to Maurice.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 5).value == "FALSE":
        m = "Grr. Growl Gar. (Maurice seems to be toying with a piece of fruit. You probably won’t be able to grab it, unless you distract him…) \n```ml\nPUZZLE NO. 003 \n\n\"Next to Maurice you notice some cat-shaped toys and a board. You realize it’s a peg solitaire board, and the cats are the pegs. They currently have the formation shown below. If you can quickly solve the peg solitaire, Maurice might be entertained enough to drop the fruit. To solve it, you have to jump pegs over each other until only one remains in the center of the board. Pegs can only jump over one other peg at a time, and those pegs have to be directly adjacent to it. Pegs cannot jump diagonally, and once a peg is jumped over, it’s removed from the board. What is the minimum number of jumps required to solve the board?\"\n```https://docs.google.com/drawings/d/1zXRNoYau219wjifIBHoTz3RBxgObyyIFytgniRC2Rjc/edit?usp=drivesdk"
        await ctx.send(m + " \nUse the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Maurice.", bot.user, m, 'one-ring-circus')
    else:
        m = "Gar? Groof. (He drops an apple, and you take it with you.)"
        await ctx.send(m, ephermeral=True)
        await messagelink.send_message(ctx.author, "Talk to Maurice.", bot.user, m, 'one-ring-circus')

bot.start(TOKEN)
