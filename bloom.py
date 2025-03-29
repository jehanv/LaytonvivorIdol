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

@slash_command("talk", description="Talk to Inspector Bloom.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 4).value == "FALSE":
        m = "Greetings. I am Detective Inspector Leonard Bloom. How may I be of assistance? ...Of course. The fabled Ruins of Akbadain. I myself am rather interested in them. You'll have to forgive me, but I have no wish to give you any clues for free. Perchance, you could prove yourself a like-minded individual by solving this puzzle, devised by my own hand.  \n```ml\nPUZZLE NO. 015 \n\n\"Overall, this sentence consists of [] letters, and of those letters, [] are the letter “e”. There are numerous ways you can fill in the two sets of square brackets with numerical values to make the sentence true. In fact, there are 5. If you are to take every value used in all of those solutions, and divide their sum by 10, what number would you end up with?\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Bloom.", bot.user, m, 'briefing-room')
    else:
        m = "Rather impressive. ...I suppose I must now give you the information I have collected. ...by spot D, my suspicions were aroused, by.... a... unusually tall cactus. Yes, it looked quite odd, standing there alone. I'm afraid that is all I have to tell you. Good day."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Bloom.", bot.user, m, 'briefing-room')

bot.start(TOKEN)