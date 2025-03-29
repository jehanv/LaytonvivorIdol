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

@slash_command("talk", description="Talk to Hanna.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 8).value == "FALSE":
        m = "Ah, he's probably in there right now, solving crimes as no other could... Hm? Oh, my apologies, I did not see you standing there! I am Hanna, and I am the founder of the Groskettes. True, we don't have any other members, but that is of no matter. Are you also here to see Grosky? ...Who's Grosky?! What do you mean, who is he? Only the top inspector in all of Scotland Yard, perhaps even the world! How could one not know of him? Honestly, I find your questioning rather rude. Here, have a try at this devious puzzle, and perhaps by the time you are done you will see Clamp in a different light! \n```ml\nPUZZLE NO. 013 \n\n\"Below is a link to a set of 12 shapes. 7 of these shapes can be used to form a square. The other five contain letters that spell out a word. Can you tell me what that word is? (You are not allowed to rotate or flip any shapes, and remember only 7 of them are to be used to make the square.) \n https://docs.google.com/drawings/d/1Rjal1FIQLWL5c8sYmcz4eydIWBHtgSKb9UFbhApeGPg/copy \"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Hanna.", bot.user, m, 'city-hall-steps')
    else:
        m = "My, oh my! Not bad! Thanks for the help there! You're the one who wanted to know something 'bout the ruins, right? Well, all I can tell you is that A don't have any cacti, while C has two."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Hanna.", bot.user, m, 'city-hall-steps')

bot.start(TOKEN)
