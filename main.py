import discord
from discord.ext import commands

intents = discord.Intents().all()
intents.members=True
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    channel = client.get_channel(CHANNEL ID)
    embed=discord.Embed(title=f"Welcome {member.name}", description="Thanks for joining,please read our server rules.!")             
    embed.set_thumbnail(url=member.avatar)
  
    await channel.send(embed=embed)
  
    role = discord.utils.get(member.guild.roles, name='ROLE TO GIVE TO MEMBER')
    await member.add_roles(role)
    
    client.run('BOT TOKEN') 
