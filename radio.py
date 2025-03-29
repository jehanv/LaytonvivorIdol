
import asyncio
from typing import Optional

from naff import Extension, GuildVoice, listen, slash_command, slash_option
from naff.api.events import VoiceStateUpdate
from naff.api.voice.audio import AudioVolume
from naff.client.utils import find
from naff_audio import YTAudio


class Radio(Extension):

    @listen()
    async def on_ready(self):
 
        return await self.start_radio(self.bot.get_channel(1011798163457327156))

    async def start_radio(self, channel: GuildVoice):
        vc = await channel.connect(deafened=True)
        audio = await YTAudio.from_url(url="https://www.youtube.com/watch?v=FjvRUGybjRk", stream=False)
        await vc.play(audio)



def setup(bot):
    Radio(bot)