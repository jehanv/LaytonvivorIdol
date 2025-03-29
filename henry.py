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

@slash_command("talk", description="Talk to Henry.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 20).value == "FALSE":
        m = "So, you've finally arrived. I've heard of your exploits, and I suppose I must thank you. The ruins are very special to me, to everyone living here in fact. But where are my manners; call me Henry. Henry Ledore. Perhaps you would like some tea? No? ...I see... Yes, I can help guide you. I don't have the exact location written, for security purposes, but there is a way to identify the spot. Though, and you must forgive me, I don't fully feel as though I can trust Layton. He's made mistakes before, through no direct fault of his own. I believe that a test would be more than understandable given the circumstances. And if you can't solve this, I doubt you would be locate the ruins anyway... \n```ml\nPUZZLE NO. 016 \n\n\"Instructions for Puzzle: https://docs.google.com/document/d/1aVFm2i_UcrDiGeIPdFZF02wVto03qtE4755_32Doqb8/edit?usp=sharing\nYou may use this grid to assist your findings: https://docs.google.com/spreadsheets/d/1tm0H0XO0apj1bt2LC1GTJZJzZcY0I3KJQkzztRkWfUg/edit\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Henry.", bot.user, m, 'ledore-mansion')
    else:
        m = "Spectacularly done. I shouldn't expect anything less from an acquaintance of the Professor. As you wish, I can aid your search for the ruins. I do hope the Masked Gentleman doesn't find them... and if he does, should he misuse the power he gains, I shall personally assure that he is stopped. He will come to understand something about me; as long as I live, this city will not be harmed. The rest is irrelevant. ...Do forgive me, I didn't mean to ramble. I must still succor. The key lies with the cacti. When I had first located the entrance, there was this tragically dried cactus. Not a single bloom upon it. It seemed somewhat symbolic at the time... Find this cactus, and you shall surely find the sought-after Ruins of Akbadain."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Henry.", bot.user, m, 'ledore-mansion')

bot.start(TOKEN)
