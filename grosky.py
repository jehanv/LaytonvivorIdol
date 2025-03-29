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

@slash_command("talk", description="Talk to Grosky.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 14).value == "FALSE":
        m = "Greetings, citizen! Inspector Grosky here! Never lost a case, I have! ...Well, except for one. \n```ml\nPUZZLE NO. 020 \n\n\"Gael: The culprit is Ezra!\nFinley: The culprit is Hudson!\nAlex: The culprit is Blake!\nDrew: The culprit is Cameron!\nCameron: The culprit is Alex!\nBlake: The culprit is Drew!\nHudson: The culprit is Cameron!\nIzumi: The culprit is my sister!\nEzra: The culprit is Gael!\nIt was a tough case. We didn't have anything to go on except for each of the witness' words. I'll admit, it had even stumped the great Clamp Grosky! Not a single member of the force knew what to do! Of course, some people had a hard time taking this. Bloom said he had 'deduced' some things, but I imagine he was just making stuff up. Listen to this tape of him.\n\"Hm... how to solve this... alright, let's review. Precisely 3 of them know who the culprit is, and each of them accused someone different, not within their group. Those 3 will never say something truthful. The other 6 people, including Finley, Alex, and Drew, never lie on purpose. That being said, it’s possible that they can be mistaken. I did some extra interrogation, and during this Blake, Drew, Ezra, Finley and Hudson each claimed that they were not Izumi’s sister. We do however know that Izumi does have a sister within the group. Alex claimed that Hudson knows who the culprit is, Hudson claimed the same about Gael, and Gael claimed the same about Hudson. One last thing. I got a call from the Commander, and they're certain that only one of our suspects' inital statements was actually true.\nNow then. Can we figure out who the culprit is?\"\nHonestly, some people just don't know how to take a loss. At this point, we should probably just retire the case.\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Grosky.", bot.user, m, 'briefing-room')
    else:
        m = "Sorry, I didn't catch that. Got lost in my thoughts. Thinking about this time when I was at E, this spot in the desert with not a single cactus, so I just ran to the east for a while, eventually falling into this weird pit. Had a lot of pictures of masks inside it. Odd."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Grosky.", bot.user, m, 'briefing-room')
bot.start(TOKEN)
