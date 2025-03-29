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

@slash_command("talk", description="Talk to Stumble.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 13).value == "FALSE":
        m = "Hello there! Welcome to Monte D'or! The city of miracles! Why not come down to the circus! It's a load of fun! I'd guide you, but I'm having some trouble at the moment. Not too much trouble, just some tangled balloons. Don't worry about it. It's a bit important, because I need to untangle these for-- no, no, really, that's fine! I can handle it! ...Alright, fine, if you insist. But I should warn you that they are incredibly tangled! I can't make heads or tails of this mess! Admittedly, I can't make heads or tails of a lot of things... \n```ml\nPUZZLE NO. 018 \n\n\"To untangle these balloons, you can press the orange arrows to swap the positions of the green dots. When an arrow is pressed, it will swap the dots on both squares it is pointing to-- That is to say, the dots on top of the squares to the immediate left and right of the arrow will swap positions, and the dots on the bottom of the squares will swap with each other as well. The dots are connected to the strings of the balloons, and these strings will stay connected when the dots swap. So, swapping dots will affect the strings as well. The objective is to arrange the strings in to five parallel vertical lines, thus untangling the balloons. Input your answer by listing the arrows that need to be pressed. Each arrow's name is determined by the letter and number it aligns with, so the top-left arrow would be A1, and the bottom-right would be D4. The answer should contain as few arrows pressed as possible. List the arrows in alphabetical order, then numerical. For example, if you needed to press every arrow, your answer should be A1-A2-A3-A4-B1-B2-B3-B4-C1-C2-C3-C4-D1-D2-D3-D4.\"``` https://docs.google.com/drawings/d/1PbMAZJVJ5iygNPlwYjis5HwnVxRRfeSOSAyjJPMKPFw/edit?usp=sharing"
        await ctx.send(m + " \nUse the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Stumble.", bot.user, m, 'carnival-square')
    else:
        m = "Wow! That was great! I really appreciate this; now I can get my clown nose! I don't really have anything to give you as thanks... All I have is this yarn. If you'd like, you can have it! If I keep it, I'm bound to get tangled."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Stumble.", bot.user, m, 'carnival-square')

bot.start(TOKEN)
