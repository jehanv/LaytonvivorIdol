from naff import ActionRow, Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen, ComponentContext
from naff import ( Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes,  )

import gspread
import messagelink
intents = Intents.DEFAULT

gc = gspread.service_account(filename="./service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

bot = Client(default_prefix='!', sync_interactions=True, intents=intents, send_command_tracebacks=False)
TOKEN = "" # Token hidden for security reasons

@slash_command("talk", description="Talk to Madame Lapushka.", scopes=[876571805572300851])
async def talk(ctx):
    row = worksheet.find(str(ctx.author.id)).row
    if worksheet.cell(row, 11).value == "FALSE":
        components = [ ActionRow( Button( style=ButtonStyles.GREEN, label="Yes", custom_id="yes" ), Button( style=ButtonStyles.GREEN, label="No", custom_id = "no" ) ) ]
        m = "Good day. Would you like to purchase something from my store? It will, of course, cost you some hint coins. 5, to be specific."
        await ctx.send(m, components=components, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Lapushka.", bot.user, m, 'merchant-district')
        try:
            used_component = await bot.wait_for_component(components=components, timeout=60)
        except TimeoutError:
            used_component.context.send("Timed out, try again!", ephemeral=True)
        else:
            if used_component.context.custom_id == "yes":
                if int(worksheet.cell(row, 23).value) >= 5:
                    worksheet.update_cell(row, 23, int(worksheet.cell(row, 23).value)-5)
                    picarats = int(worksheet.cell(row, 2).value)
                    worksheet.update_cell(row, 2, picarats + 50)
                    worksheet.update_cell(row, 11, 'TRUE')
                    m = "Thank you! Here is your product, a fine mask, some picrats, and also, some information. There is a large canyon by the ruins, which I'm sure you've seen. On the east side of this gorge, there is a total of 7 cacti and 3 flowers. Hope that helps!"
                    await used_component.context.send(m, ephemeral=True)
                    await messagelink.send_message(ctx.author, "Make sale.", bot.user, m, 'merchant-district')
                else: 
                    m = "Sorry, you don't have enough hint coins. Talk to me again if you change your mind. How about a puzzle instead? \n```ml\nPUZZLE NO. 009 \n\n\"I have here several sets of numbers, all of which follow the same pattern. When following this pattern, the sets I have here each lead to one specific integer, which throws the pattern into a never-ending loop.\n6382 365 199 364 _ 103 19 102 6 37 102 6 37 102\n3999 904 _ 103 19 102 6 37 102 6 37 102 \n2784 445 _ 103 19 102 6 37 102 6 37 102\n6829 629 292 _ 103 19 102 6 37 102 6 37 102\nUsing these four sets, can you figure out what the integer is? It's the same in each one, and also, you'll have to figure out the sequence on your own.\"``` Use the `solve` command with Layton and Luke to solve the puzzle!"
                    await used_component.context.send(m, ephemeral=True)
                    await messagelink.send_message(ctx.author, "Not enough hint coins.", bot.user, m, 'merchant-district')
            else:
                m = "Well that's a shame. Talk to me again if you change your mind. How about a puzzle instead? \n```ml\nPUZZLE NO. 009 \n\n\"I have here several sets of numbers, all of which follow the same pattern. When following this pattern, the sets I have here each lead to one specific integer, which throws the pattern into a never-ending loop.\n6382 365 199 364 _ 103 19 102 6 37 102 6 37 102\n3999 904 _ 103 19 102 6 37 102 6 37 102 \n2784 445 _ 103 19 102 6 37 102 6 37 102\n6829 629 292 _ 103 19 102 6 37 102 6 37 102\nUsing these four sets, can you figure out what the integer is? It's the same in each one, and also, you'll have to figure out the sequence on your own.\"``` Use the `solve` command with Layton and Luke to solve the puzzle!"
                await used_component.context.send(m, ephemeral=True)
                await messagelink.send_message(ctx.author, "Refuse sale.", bot.user, m, 'merchant-district')


    else:
        m = "There is a large canyon by the ruins, which I'm sure you've seen. On the east side of this gorge, there is a total of 7 cacti and 3 flowers. Hope that helps!"
        await ctx.send(m, ephemeral=True)
        await messagelink.send_message(ctx.author, "Talk to Lapushka.", bot.user, m, 'merchant-district')

bot.start(TOKEN)
