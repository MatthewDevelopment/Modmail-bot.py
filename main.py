import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix= commands.when_mentioned_or('>'), intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="My DMs"))
    print("Modmail Bot Version 2 Ready to Go")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        modmail_channel = discord.utils.get(client.get_all_channels(), name="modmail")
        await modmail_channel.send(f"**{str(message.author)} | {str(message.author.id)}:** " + message.content)
    elif str(message.channel) == "modmail" and message.content.startswith("<"):
        member_object = message.mentions[0]

        index = message.content.index(" ")
        string = message.content
        mod_message = string[index:]

        await member_object.send("[" + message.author.display_name + "]" + mod_message)

    await client.process_commands(message)



@client.command()
async def ping(ctx):
    await ctx.send(f'PONG!\nLatency: {round(client.latency * 1000)}ms')

@client.command()
async def setupmodmail(ctx):
    channel = await guild.create_text_channel('modmail')
    guild = ctx.guild
    channel = discord.utils.get(guild.text_channels, name="modmail")
    role = discord.utils.get(guild.roles, name="@everyone")
    await channel.set_permissions(role, send_messages=False, read_messages=False)
    await ctx.send("The Modmail channel has been set up.")




client.run("")
