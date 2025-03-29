import logging
import asyncio

from naff import Intents, Client, Button, ButtonStyles, CommandTypes, context_menu, prefixed_command, listen, ComponentContext, ActionRow, Select, SelectOption, utils
from naff import ( Client, slash_command, InteractionContext, slash_option, OptionTypes, context_menu, CommandTypes,  )

import gspread
import messagelink
gc = gspread.service_account(filename="./service_account.json")
sh = gc.open("Laytonvivor Idol Database")
worksheet = sh.get_worksheet(0)

intents = Intents.DEFAULT

bot = Client(default_prefix='!', sync_interactions=True, intents=intents, send_command_tracebacks=False)
TOKEN = "" # Token hidden for security reasons
# @listen()
# async def on_ready():
#     selects = [ ActionRow( Select( options=[ SelectOption( label="A", value="A" ), SelectOption( label="B", value="B" ), SelectOption( label="C", value="C" ), SelectOption( label="D", value="D" ), SelectOption( label="E", value="E" ), SelectOption( label="F", value="F" ), SelectOption( label="G", value="G" ), SelectOption( label="H", value="H" ), SelectOption( label="I", value="I" ), SelectOption( label="J", value="J" ), SelectOption( label="K", value="K" ), SelectOption( label="L", value="L" ), SelectOption( label="M", value="M" ), ], placeholder="Where are the ruins located?", min_values=1, max_values=1, ) ) ]
#     await bot.get_channel(879179818846011402).send("Well hello there. I am under the impression that you would be searching for the immunity idol, is that correct? Well, I've heard the idol is hidden in the Ruins of Akbadain, but you'd need to locate it. Thankfully, I have a map, with a list of locations. You might want to save the map so you have it with you. When you think you know where the Ruins are, visit me in my room and select which location contains the Ruins below. But only do it when you're sure, as if you get it wrong twice, I won't be able to help you and you will be unable to find the immunity idol in the Ruins. I believe that the people of Monte D'or should be able to give you some info about the locations by solving their puzzles. Just be sure not to inform the Masked Gentleman of all this. Soon, you, the other employees, and the entire city shall be freed from his undoubtedly wicked grasp.", file=open("map.png", "rb"), components=selects)

@listen()
async def on_component(event: ComponentContext):
    ctx = event.context
    if ctx.component_type == 3:
        letter = ctx.data["data"]["values"][0]
        components = [ActionRow( Button( style=ButtonStyles.PRIMARY, label="Confirm", disabled=False, ) ) ]
        m = "So you think the ruins are at **Location " + letter + "**. Press the button to confirm this is what you mean and I'll search that location."
        message = await ctx.send(m, ephemeral=True, components=components)
        await messagelink.send_message(ctx.author, "The ruins are in **Location " + letter + "**.", bot.user, m, 'layton’s-room')
        try:
            used_component = await bot.wait_for_component(messages=message, components=components, timeout=30)
        except asyncio.exceptions.TimeoutError:
            await ctx.send("Alright, come back to me once you're sure.", ephemeral=True)
        else:
            m = "Alright, I'll search for the ruins. I'll tell a host if I find anything, and they will be able to assist you further."
            await used_component.context.send(m, ephemeral=True)
            await messagelink.send_message(ctx.author, "Confirmed", bot.user, m, 'layton’s-room')

bot.start(TOKEN)