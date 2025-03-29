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

@slash_command("talk", description="Talk to Nils.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 9).value == "FALSE":
        m = "And who might you be? A tourist of some kind? Hm. You seem smart. Mind solving this puzzle for me? \n```ml\nPUZZLE NO. 011 \n\n\"After playing in the playground, also known as the ground on which children play, the children (who were playing in the playground) subsequently came to the realization that they had realized that some of them may have had dirt on their faces. These children were all very intelligent and logical, and each one knew the others were logical and intelligent. Each of them could see all the other children's faces, but not their own, because that would require a mirror, and there were no mirrors in this specific playground that the children were playing in, as playgrounds are typically used for playing, and not looking in a mirror. Anyways, a police officer came over, and told the children that at least one of them had dirt on their face. He then thought of a game to play, since these children seemed to enjoy playing, which was evident by them being in the playground in which children often play. He decided that he would take several turns, and on each turn he would ask the children if they had dirt on their face. If they were absolutely sure they did, they would step forward and say so. But remember, they couldn't see their face. Without telling you how many children there were in total, I ask you to figure out how many of them had dirt on their face. The only info I will give you is that all of the children with dirt on their face had stepped forward on precisely the 2,763rd turn, less than 10% of the children had dirt on their faces, there were over 30,000 children, and they all enjoyed playing at the playground which most children, including them, typically enjoyed playing at. So now then, how many children had dirt on their face?\"```"
        await ctx.send(m + " Use the `solve` command with Layton and Luke to solve the puzzle!", ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Nils.", bot.user, m, 'scorpion-casino')
    else:
        m = "...huh. What's that? You wanna know about Akbadain? Why would I know anything about that place?"
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Nils.", bot.user, m, 'scorpion-casino')

bot.start(TOKEN)
