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

@slash_command("talk", description="Talk to Tyrone.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 6).value == "FALSE":
        m = "I am the ringmaster of this here circus. Hello, how do you do. Yes, indeed, I climbed up the ladder to the top! unlike these poor hapless characters... \n```ml\nPUZZLE NO. 004 \n\n\"You are climbing up the rungs of a ladder, but it isn't exactly going well. Each time, you go up three rungs, you back down two, then jump up 5, then fall down 4. Then this process repeats. For every fifth ladder rung that you step on (i.e. rung 5, 10, 15, etc.), the rung beneath it breaks, and you can't land on that rung-- if you try to, you will fall off. When going up/down rungs you only touch the ones you start and end on, for fear of breaking any rungs in between. You can choose to start on rung 1, 2, 3, 4, or 5. Which rung should you start on to climb up as long as possible before falling?)\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Tyrone.", bot.user, m, 'one-ring-circus')
    else:
        m = "Impressive! Perhaps you would like to join my circus? ...No? Very well, I shall then leave you with information as to the location of the ruins which you seek. At B, when I traveled there, I had no luck finding it, although that may have just been I was clumsy, bumping into one cactus only to fall back onto yet another."
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Tyrone.", bot.user, m, 'one-ring-circus')

bot.start(TOKEN)
