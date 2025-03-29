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

@slash_command("talk", description="Talk to Angela.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 21).value == "FALSE":
        m = "Oh, hello! Welcome! You're here to help Hershel with his investigation, correct? Well, it seems as though you've been doing well so far. Why not take a break for now? We could play a game of some sort... how about Battleship? I can explain the rules if you're unfamiliar. \n```ml\nPUZZLE NO. 017 \n\n\"https://laytonvivor.com/ There are 10 ships scattered across the grid. Every ship is one square wide, and will be placed in a straight line somewhere on the grid. The battleship is 4 squares long. The 2 cruisers are each three squares long. The 3 destroyers are each two squares long. The 4 submarines only take up a single square. With a bit of deduction and guesswork, you should be able to find all of them. You can attempt this as many times as you like.\"```"
        await ctx.send(m + "When you beat the game, enter the code using the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Angela.", bot.user, m, 'ledore-mansion')
    else:
        m = "Well done! It seems I've been outplayed. It's always good to relax for a bit, isn't it? Though you probably need to get back to work by now. But truly, don't forget to rest if you need to. I, for one, often take walks nearby F and M, out in the desert. Each spot has a magnificent flower on a cactus. Simply wondrous to look at."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Angela.", bot.user, m, 'ledore-mansion')

bot.start(TOKEN)