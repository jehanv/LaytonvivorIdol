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

@slash_command("talk", description="Talk to Nanna Grams.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 3).value == "FALSE":
        m = "Hi there! If it's puzzles you're after, you're in the right place! ...No? Not puzzles? Ah, I see, you're after the idol! Well I can help with that as well. From the clues that you can gather from all the city folks around here, there's an easy way to give them some meaning. I'll tell you how to understand what they say... if you solve this puzzle! \n```ml\nPUZZLE NO. 001 \n\n\"There is a cactus in the desert with 30 needles poking out of it. Every time this cactus pokes someone, it loses a needle as a result. One person bumps into it once, is hurt, and goes to tell two people about it. Any person who knows about it comes the next day and bumps into it, so on the second day 3 people bump into it, and each of them tell 2 people about the encounter, and this process repeats until the cactus is out of needles. Now, can you tell me the difference between the maximum and minimum amount of days it takes for the cactus to run out of needles?\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Nanna Grams.", bot.user, m, 'dromedary-lobby')
    else:
        m = "Well... not bad! Expert solving! Now, for the information! Each location has a number of cacti near it, and some of them will have flowers. Each location either has no cacti, one cactus, one flowering cactus, two cacti, two flowering cacti, or two cacti where one is flowering and the other isn't. With that info, you should... Hm? Tell you which spot has which cacti? No, where's the fun in that! You'll have to ask the citizens for that."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Nanna Grams.", bot.user, m, 'dromedary-lobby')

bot.start(TOKEN)
