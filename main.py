import logging
import asyncio

import naff
from naff import Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen, ComponentContext, utils, cooldown, Buckets, Cooldown
from naff import ( Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes,  )
from naff.models import to_snowflake
import gspread
import messagelink
import datetime

gc = gspread.service_account("././service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

intents = Intents.ALL


class CustomClient(Client):
    async def on_command_error(self, ctx: InteractionContext, error: Exception):
        if isinstance(error, naff.errors.CommandOnCooldown):
            await ctx.send("You can't do this yet, try again in **" + str(datetime.timedelta(seconds=int(error.cooldown.get_cooldown_time()))) + "**", ephemeral=True)

bot = CustomClient(default_prefix='!', intents=intents, sync_interactions=True)
TOKEN = "" # Token hidden for security reasons

def get_new_locs(channel):
    location1 = ""
    location2 = ""
    location3 = ""
    location4 = ""
    if channel == "layton’s-room":
        location1 = "Dromedary Lobby"
    elif channel == "dromedary-lobby":
        location1 = "Layton’s Room"
        location2 = "Dromedary Plaza"
    elif channel == "dromedary-plaza":
        location1 = "Dromedary Lobby"
        location2 = "One-Ring Circus"
        location3 = "City Monument"
    elif channel == "one-ring-circus":
        location1 = "Dromedary Plaza"
        location2 = "Dalston Mansion"
    elif channel == "dalston-mansion":
        location1 = "One-Ring Circus"
    elif channel == "scorpion-casino":
        location1 = "Chance Avenue"
    elif channel == "chance-avenue":
        location1 = "City Monument"
        location2 = "Scorpion Casino"
    elif channel == "city-monument":
        location1 = "Dromedary Plaza"
        location2 = "Chance Avenue"
        location3 = "Merchant District"
    elif channel == "merchant-district":
        location1 = "City Monument"
        location2 = "Gallery Plaza"
    elif channel == "montsarton-gallery":
        location1 = "Gallery Plaza"
    elif channel == "gallery-plaza":
        location1 = "Merchant District"
        location2 = "Montsarton Gallery"
        location3 = "Carnival Arcade"
        location4 = "Knickknack Alley"
    elif channel == "carnival-arcade":
        location1 = "Gallery Plaza"
        location2 = "Carnival Square"
    elif channel == "carnival-square":
        location1 = "Carnival Arcade"
    elif channel == "briefing-room":
        location1 = "City Hall Steps"
    elif channel == "city-hall-steps":
        location1 = "Knickknack Alley"
    elif channel == "knickknack-alley":
        location1 = "Gallery Plaza"
        location2 = "City Hall Steps"
        location3 = "Ledore Mansion"
    elif channel == "ledore-mansion":
        location1 = "Knickknack Alley"
    return location1, location2, location3, location4

@listen()
async def on_ready():
    print([channel.name for channel in bot.get_guild(876571805572300851).channels])



@listen()
async def on_component(event: ComponentContext):
    ctx = event.context
    guild = bot.get_guild(876571805572300851)
    old_role_name = ctx.channel.name.replace("-", " ").title()
    for comp in ctx.message.components[0].components:
        if comp.custom_id == ctx.custom_id:
            button_pressed = comp
    role = utils.find(lambda r: r.name == button_pressed.label, guild.roles)
    old_role = utils.find(lambda r: r.name == old_role_name, guild.roles)
    await ctx.author.remove_role(old_role)
    await ctx.author.add_role(role)
    await ctx.send("Moving you to " + button_pressed.label + "...", ephemeral=True)


@slash_command("move", description="Move around Monte d'Or.", scopes=[876571805572300851])
async def move(ctx):
    await ctx.defer(ephemeral=True)
    channel = ctx.channel.name
    location1, location2, location3, location4 = get_new_locs(channel)
    if location2 == "":
        await ctx.send("Where would you like to go?", components=[Button(ButtonStyles.BLURPLE, location1)], ephemeral=True)
    elif location3 == "":
        await ctx.send("Where would you like to go?", components=[Button(ButtonStyles.BLURPLE, location1), Button(ButtonStyles.BLURPLE, location2)], ephemeral=True)
    elif location4 == "":
        await ctx.send("Where would you like to go?", components = [Button(ButtonStyles.BLURPLE, location1), Button(ButtonStyles.BLURPLE, location2), Button(ButtonStyles.BLURPLE, location3)], ephemeral=True)
    else:
        await ctx.send("Where would you like to go?", components = [Button(ButtonStyles.BLURPLE, location1), Button(ButtonStyles.BLURPLE, location2), Button(ButtonStyles.BLURPLE, location3), Button(ButtonStyles.BLURPLE, location4)], ephemeral=True)

@slash_command("solve", description="Solve a puzzle.", scopes=[876571805572300851])
@slash_option(name="solution", description="The solution to the puzzle.", required=True, opt_type=OptionTypes.STRING)
@slash_option(name="number", description="The puzzle number.", required=True, opt_type=OptionTypes.INTEGER)
async def solve(ctx: InteractionContext, number: int, solution: str):
    row = worksheet.find(str(ctx.author.id)).row
    if number == 1:
        if worksheet.cell(row, 3).value == "FALSE":
            if solution == "7":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 20)
                worksheet.update_cell(row, 3, 'TRUE')
                await ctx.send("Correct! Talk to Nanna Grams again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 2:
        if worksheet.cell(row, 4).value == "FALSE":
            if solution == "243":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 30)
                worksheet.update_cell(row, 4, 'TRUE')
                await ctx.send("Correct! Talk to Yukkles again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 4:
        if worksheet.cell(row, 6).value == "FALSE":
            if solution == "1":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 25)
                worksheet.update_cell(row, 6, 'TRUE')
                await ctx.send("Correct! Talk to Tyrone again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 5:
        if worksheet.cell(row, 7).value == "FALSE":
            if solution == "1":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 30)
                worksheet.update_cell(row, 7, 'TRUE')
                await ctx.send("Correct! Talk to Dalston again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 8:
        if worksheet.cell(row, 10).value == "FALSE":
            if solution.lower() == "tanya":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 25)
                worksheet.update_cell(row, 10, 'TRUE')
                await ctx.send("Correct! Talk to Tanya again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 9:
        if worksheet.cell(row, 11).value == "FALSE":  
            if solution == "172":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 50)
                worksheet.update_cell(row, 11, 'TRUE')
                await ctx.send("Correct! Talk to Madame Lapushka again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 10:
        if worksheet.cell(row, 12).value == "FALSE":  
            if solution.lower() == "july 16":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 20)
                worksheet.update_cell(row, 12, 'TRUE')
                await ctx.send("Correct! Talk to Collette again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 11:
        if worksheet.cell(row, 9).value == "FALSE":  
            if solution == "2763":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 30)
                worksheet.update_cell(row, 9, 'TRUE')
                await ctx.send("Correct! Talk to Nils again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 12:
        if worksheet.cell(row, 8).value == "FALSE":  
            if solution == "33":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 40)
                worksheet.update_cell(row, 8, 'TRUE')
                await ctx.send("Correct! Talk to Drake again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 13:
        if worksheet.cell(row, 18).value == "FALSE":  
            if solution.lower() == "heart":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 25)
                worksheet.update_cell(row, 18, 'TRUE')
                await ctx.send("Correct! Talk to Hanna again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 14:
        if worksheet.cell(row, 16).value == "FALSE":  
            if solution.lower() == "eleven" or solution == "11":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 40)
                worksheet.update_cell(row, 16, 'TRUE')
                await ctx.send("Correct! Talk to Sheffield again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 15:
        if worksheet.cell(row, 15).value == "FALSE":  
            if solution.lower() == "45.8":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 55)
                worksheet.update_cell(row, 15, 'TRUE')
                await ctx.send("Correct! Talk to Bloom again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 16:
        if worksheet.cell(row, 20).value == "FALSE":  
            if solution.lower() == "abuoeqhbduiea":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 55)
                worksheet.update_cell(row, 20, 'TRUE')
                await ctx.send("Correct! Talk to Henry again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 3:
        if worksheet.cell(row, 5).value == "FALSE":  
            if solution.lower() == "19":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 10)
                worksheet.update_cell(row, 5, 'TRUE')
                await ctx.send("Correct! Talk to Maurice again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 17:
        if worksheet.cell(row, 21).value == "FALSE":  
            if solution.lower() == "9594":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 45)
                worksheet.update_cell(row, 21, 'TRUE')
                await ctx.send("Correct! Talk to Angela again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 18:
        if worksheet.cell(row, 13).value == "FALSE":  
            if solution.lower() == "A1-B2-C3-D3":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 45)
                worksheet.update_cell(row, 13, 'TRUE')
                await ctx.send("Correct! Talk to Stumble again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 19:
        if worksheet.cell(row, 22).value == "FALSE":  
            if solution.lower() == "42":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 20)
                worksheet.update_cell(row, 22, 'TRUE')
                await ctx.send("Correct! Talk to Guy again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    if number == 20:
        if worksheet.cell(row, 22).value == "FALSE":  
            if solution.lower() == "Gael":
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats + 60)
                worksheet.update_cell(row, 22, 'TRUE')
                await ctx.send("Correct! Talk to Grosky again to get some information.", ephemeral=True)
            else:
                picarats = int(worksheet.cell(row, 2).value)
                worksheet.update_cell(row, 2, picarats - 5)
                await ctx.send("Incorrect, try again.", ephemeral=True)
        else:
            await ctx.send("You've already solved this puzzle!")
    await messagelink.send_message(ctx.author, "Attempted puzzle number " + str(number) + ".", bot.user, "Guess: ||" + solution + "||", ctx.channel.name)


@slash_command("balance", description="Get your picarat and hint coin balance.", scopes=[876571805572300851])
async def balance(ctx: InteractionContext):
    row = worksheet.find(str(ctx.author.id)).row
    picarats = int(worksheet.cell(row, 2).value)
    await ctx.send("You have " + str(picarats) + " picarats.", ephemeral=True)

bot.start(TOKEN)
