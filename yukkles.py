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

@slash_command("talk", description="Talk to Yukkles.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 4).value == "FALSE":
        m = "Phew! ...It ain't easy being a clown, you know. Constantly trying to balance on a ball, it gets tiresome soon enough. Balancing in general makes my head hurt... just like this puzzle here. \n```ml\nPUZZLE NO. 002 \n\n\"Say you had an amount of weights, with one being just slightly lighter than the rest. Such a slight difference can only be checked using a scale. If you had three weights, and one was lighter, you could consistently figure out which one was lighter with one use of the scale. With four weights, however, it would take two uses. What is the minimum amount of weights that would consistently require five uses of the scale? (a use counts as putting any number of weights on each side, then pressing a button that would measure which was lighter.)\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Yukkles.", bot.user, m, 'one-ring-circus')
    else:
        m = "...wow, not bad. There ain't too many folks around that can just chew through a puzzle like that one! I bet you'd be good at balancing! Especially around H, since there aren't any annoying cactuses around. Or is it cacti? I always forget, because my brain is just spinning around as of late. I always feel like I'm losing my balance!"
        await ctx.send(m, ephermeral=True)
        await messagelink.send_message(ctx.author, "Talk to Yukkles.", bot.user, m, 'one-ring-circus')

bot.start(TOKEN)
