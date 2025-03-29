# hey that rhymes
from naff import Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen, \
    ComponentContext
from naff import (Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes, )

import gspread
import messagelink
intents = Intents.DEFAULT

gc = gspread.service_account(filename="./service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

bot = Client(default_prefix='!', sync_interactions=True, intents=intents, send_command_tracebacks=False)
TOKEN = "" # Token hidden for security reasons

@slash_command("talk", description="Talk to Guy.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 22).value == "FALSE":
        await ctx.send(
            "Step right up, step right up! Welcome to the greatest toy shop this side of Knickknack Alley, and the other side too! We've got cheap gizmos and free smiles! And all sorts of gizmos for that matter! Stuffed bears, dollhouses, robots, anything you could want! ...No? Not interested? Are you sure? How about this then? A little set of towers and discs! A classic puzzle!  \n```ml\nPUZZLE NO. 019 \n\n\"Here I have what is called the Tower of Hanoi. It has three tall pegs which you can put discs on. All of the discs start on the far-left pillar, with the largest disc on the bottom and the smallest on the top. The rest of the discs are in order by size as well. The objective of the game is to move all the pegs to the far right-pillar, in the same order they are in the start (largest to smallest, bottom to top). Some rules you should probably know: You can only move one disc each turn, you can only move discs at the top of a stack (1 disc also counts as a stack), and discs can only be placed on discs larger than them. All in all, pretty simple! So, do you wanna give it a try? ...Still no? Come on, it's fun! Perhaps you want a really challenging version of the game... How about this. I've sold this product to 8,796,093,022,207 customers. I know, quite a large amount. It's weird, seeing as the population of Monte D'or is much smaller than that... Anyways, I can get you the most difficult set I can be solved in exactly that many moves. Obviously, if a set is more difficult, it just means it has more discs. ...Hm... now I just have to figure out how many discs would I need for that.... Can you figure it out?\"``` Use the `solve` command with Layton and Luke to solve the puzzle!",
            ephemeral=True)
    else:
        await ctx.send(
            "Ah! That's it. Thanks for that! So, what do you say? ....Still a no?! Really? Oh, fine. At least accept some picarats for helping me there. And if you ever change your mind, you know where to find me.",
            ephemeral=True)


bot.start(TOKEN)
