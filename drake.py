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

@slash_command("talk", description="Talk to Drake.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 8).value == "FALSE":
        m = "I am the owner of this casino. What might I do for you? Perhaps you'd be interested in a game of poker? Roulette? Blackjack? Slot Machines then? Nothing? Very well, but if you're not here to gamble, I'm afraid I must ask you to leave... well, unless you solve this puzzle that's been bothering me. \n```ml\nPUZZLE NO. 012 \n\n\"A while back, I bought this roulette wheel. For a long time I had it in the casino, and it seemed to work fine. Ran it through testing a couple times, no patterns popped up, so it didn't look like it was rigged. Then this one guy came in. I later found out that he actually had rigged the roulette wheel. Somehow, we never detected it. There was no way he inputted some sort of remote control to manually set what the result was-- it just followed some sort of pattern. At the time, he came up, placed some small bets, then chuckled to himself. it looked like he knew what the next spin was going to be. He bet everything on just one number, and won. I don't remember what all the previous numbers were, but i remember it landed on 7 first, then 32, then something I didn't see, then 17, then something else, then 15, then 23, then 19, then he figured it out. Just a couple of details: He looked very thoughtful at the start, so I don't think even he knew the exact pattern before coming in here. Also, if you don't know, the numbers on a roulette wheel are 0-36. You'll probably just wanna go find a wheel for yourself to see what it looks like. So then, could you help me out? What number did he bet on at the end?\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Drake.", bot.user, m, 'scorpion-casino')
    else:
        m = "My, oh my! Not bad! Thanks for the help there! You're the one who wanted to know something 'bout the ruins, right? Well, all I can tell you is that A don't have any cacti, while C has two."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Drake.", bot.user, m, 'scorpion-casino')

bot.start(TOKEN)
