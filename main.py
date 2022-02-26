import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="My DMs"))
    print("Modmail Bot Ready to Go")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        modmail_channel = discord.utils.get(client.get_all_channels(), name="modmail")
        await modmail_channel.send("[" + message.author.display_name + "] "  + message.content)
    elif str(message.channel) == "modmail" and message.content.startswith("<"):
        member_object = message.mentions[0]

        index = message.content.index(" ")
        string = message.content
        mod_message = string[index:]

        await member_object.send("[" + message.author.display_name + "]" + mod_message)




client.run("PUT BOT TOKEN HERE")
