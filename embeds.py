import discord 

def ban_em(user, guild, time):
    ban_em=discord.Embed(
        title="A member has been banned",
        description=f"{user.mention} has been banned from the server {guild.name}",
        color=discord.Color.red()
    )
    ban_em.add_field(name="**Info:**", value=f"Time of ban: {time}")
    return ban_em

def verify_ex_em(guild):
    verify_em=discord.Embed(
        title="You have been verified in a network staff server!",
        description=f"You have been verified in the server: {str(guild.name)} if you have any questions feel free to ask a network administrator",
        color=discord.Color.green()
    )
    verify_em.add_field(name="**Info:**", value="If this is an error please dm Acidic#9633")
    return verify_em