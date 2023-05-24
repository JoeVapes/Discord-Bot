import discord
import os
from discord.ext import commands

intents = discord.Intents().all()
intents.members=True
intents.message_content = True
bot = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'VapeLabs Connected {bot.user}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(CHANNEL ID)
    embed=discord.Embed(title=f"Welcome {member.name}", description="Thanks for joining,please read our server rules.!")             
    embed.set_thumbnail(url=member.avatar)
  
    await channel.send(embed=embed)

    role = discord.utils.get(member.guild.roles, name='ROLE TO GIVE MEMBER')
    await member.add_roles(role)

@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(CHANNEL ID)
    embed=discord.Embed(title=f"Goodbye {member.name}", description="Its a Shame to see you leave!")             
    embed.set_thumbnail(url=member.avatar)
  
    await channel.send(embed=embed)

@bot.command()
async def calculator(ctx):
    await ctx.send("To Calculate Day & Night please visit https://lix.tools/dayz.html")
@bot.command()
async def notepad(ctx):
    await ctx.send("We advise the use of notepad++ which you can download here https://notepad-plus-plus.org/downloads/  ")
    
    client.run('BOT TOKEN') 
