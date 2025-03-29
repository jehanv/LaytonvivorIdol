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

@slash_command("talk", description="Talk to Sheffield.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 6).value == "FALSE":
        m = "Welcome to City Hall. I'm the Chief Inspector. It's my understanding that you are aiding the professor with investigations into these ruins. I may be able to aid you, emphasis on 'may', but, in all honesty, you look a bit... shifty. A test is no doubt in order. What are they called, the ones Layton is so fond of...? Puzzles! That's it. Let's see how you handle this one! \n```ml\nPUZZLE NO. 014 \n\n\"This sentence contains exactly ___ occurrences of the letter 'e'. Your objective is to fill in the blank with a number. Now, you may be looking for a correct answer, but I don't want that-- I want to hear the mean answer. Now then, solve away!\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Sheffield.", bot.user, m, 'briefing-room')
    else:
        m = "....Ha! Ha! Not bad, that was. to be perfectly honest, that wasn't really a test as such, I just wanted to try out that puzzle on someone. Not nearly as clever as Bloom's version, but I'm rather proud of the 'mean' part. My apologies for lying, have some hint coins for your troubles. I believe the others have some information about the area you're searching."
        await ctx.send(m, ephemeral=True)
        worksheet.update_cell(row, 23, int(worksheet.cell(row, 23).value)+4)
        await messagelink.send_message(ctx.author, "Talk to Sheffield.", bot.user, m, 'briefing-room')

bot.start(TOKEN)
