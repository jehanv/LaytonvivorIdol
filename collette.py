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

@slash_command("talk", description="Talk to Collette.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 12).value == "FALSE":
        m = "Well hi there! Nice to meet you! You look like you're not from around here... Well, if you're a tourist, make sure to visit the One-Ring Circus! Oh, not a fan of circuses? But they're so fun! Like birthday parties! Everyone loves birthday parties, right? \n```ml\nPUZZLE NO. 010 \n\n\"Albert and Bernard just become friends with Cheryl, and they want to know when her birthday is. Cheryl gives them a list of 10 possible dates: May 15, May 16, May 19, June 17, June 18, July 14, July 16, August 14, August 15, or August 17.\nCheryl then tells Albert and Bernard separately the month and the day of her birthday respectively.\nAlbert: I don't know when Cheryl's birthday is, but I know that Bernard doesn't know too.\nBernard: At first I didn't know when Cheryl's birthday is, but I know now.\nAlbert: Then I also know when Cheryl's birthday is.\nSo when is Cheryl's birthday?\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle! When solving the puzzle, write your answer as the full month name and then the day, such as `January 13` or `September 18`.", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Collette", bot.user, m, 'chance-avenue')
    else:
        m = "Wow, nice job! But seriously, circuses are fun! No? You're just here for the desert then or something? Well if so, watch out for the cacti. Did you know cacti actually store water inside of them? Or was that camels? Maybe it was camels, but either way watch out for cacti because they're pretty prickly. I guess you already know that though, you'd have to be kind of dumb not to know that cacti are sharp. Kind of like stalatgi- slatatmite-- slag- whatever, the pokey rocks in caves. Whatever you call them. Oh right, it's stalactite. and stalagmite. there's a ton of those things at L, so maybe dont go down there unless its absolutely necessary, unless you wanna get poked by a stalagmite. Actually wait, no, that's stalactite. Get those two mixed up a lot. Kind of like cacti and camels. But yeah, don't go down to L, because of lots of sharp stuff. There are even cacti down there too? How'd they grow down there? I guess cacti are pretty good at surviving anywhere, since they absorb water-- assuming they do, anyways, because again, that could just be camels. Wow, I've been talking for a while. Should probably stop now."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Collette", bot.user, m, 'chance-avenue')

bot.start(TOKEN)
