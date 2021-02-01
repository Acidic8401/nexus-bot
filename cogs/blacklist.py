import discord 
from discord.ext import commands
import json
import datetime

class Blacklist(commands.Cog):
    def __init__(self, client):
        print('started')
        self.client=client
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        blacklist=self.client.get_guild(699852946363514902)
        with open(r"C:\Users\Bailey\Documents\Programs\Nexus\nexus-bot\servers.json") as f:
            time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            servers=json.load(f)
            channel_id=servers[str(guild.name)]["channel"]
            if channel_id is not "None":
                channel=blacklist.get_channel(channel_id)
                ban_em=discord.Embed(
                    title="A member has been banned",
                    description=f"{user.mention} has been banned from the server {guild.name}",
                    color=discord.Color.red()
                )
                ban_em.add_field(name="**Info:**", value=f"Time of ban: {time}")
                await channel.send("Member banned", embed=ban_em)
            else:
                pass


def setup(client):
    client.add_cog(Blacklist(client))