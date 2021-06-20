import discord
from discord.ext import commands
import random
import pandas as pd
from tkn import key



client = commands.Bot(command_prefix='jojo ', help_command=None)
# globally reading csv file once for all
col = ["name", "url", "description", "active", "votes", ]
anime = pd.read_csv("anime.csv", usecols=col)  # 69

developer = pd.read_csv("developer.csv", usecols=col)  # 6

economy = pd.read_csv("economy.csv", usecols=col)  # 69

fun = pd.read_csv("fun.csv", usecols=col)  # 70

gaming = pd.read_csv("gaming.csv", usecols=col)  # 39

kpop = pd.read_csv("kpop.csv", usecols=col)  # 8

meme = pd.read_csv("meme.csv", usecols=col)  # 70

music = pd.read_csv("music.csv", usecols=col)  # 70

poll = pd.read_csv("poll.csv", usecols=col)  # 12

reddit = pd.read_csv("reddit.csv", usecols=col)  # 70

roleplay = pd.read_csv("roleplay.csv", usecols=col)  # 70

social = pd.read_csv("social.csv", usecols=col)  # 70

stream = pd.read_csv("stream.csv", usecols=col)  # 70

@client.event
async def on_ready():
    activity = discord.Game(name="hard to get", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)



@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed2 = discord.Embed(title="Hey there! I am the jojo bot, I am here to well...help you get acquainted with other bots", color=0xFD0061)
            embed2.add_field(name="You can access various bots according to their tags, Get the top 3 bots for the category of your choice or get a random bot of a particular category\n\nHere are all the commands:",value="Hope you enjoy!",inline=False)
            embed2.add_field(name="jojo all", value="📄All bot tags", inline=False)
            embed2.add_field(name="jojo top3'tag'", value="🏅 Top 3 Bots \n(For eg.: jojo top3anime for Top 3 anime bots)", inline=False)
            embed2.add_field(name="jojo get'tag'", value="🎁 1 Random Bot \n(For eg: jojo getanime for 1 Random anime bot)", inline=False)
            embed2.add_field(name="Dont worry you can always call me back with the \"jojo help\" command! GLHF!",value="byeiee! ",inline=False)    
            await channel.send(embed=embed2)  
        break       
     
        
@client.command()
async def jojo(ctx):
    channel = ctx.channel
    num = random.randrange(3)
    if num == 0:
        await ctx.channel.send("Hi,they call me jojo")
    elif num == 1:
        await ctx.channel.send("Tail")
    else:
        await ctx.channel.send("bhosad pappu")


@client.command()
async def ily(ctx):
    channel = ctx.channel
    await ctx.channel.send("FUCKING SIMP")


@client.command()
async def intro(ctx):
    channel = ctx.channel
    await ctx.channel.send("My creators and caretaker are BLACK MAMBAS")

# alltags


@client.command()
async def help(ctx):
    channel = ctx.channel
    embed1 = discord.Embed(title="All jojo commands:", color=0x00D166)

    embed1.add_field(name="jojo all", value="📄All bot tags", inline=False)
    embed1.add_field(
        name="jojo top3'tag'", value="🏅Top 3 Bots \n(For eg.: jojo top3anime for Top 3 anime bots)", inline=False)
    embed1.add_field(
        name="jojo get'tag'", value="🎁 1 Random Bot \n(For eg: jojo getanime for 1 Random anime bot)", inline=False)
    await ctx.channel.send(embed=embed1)


@client.command()
async def all(ctx):
    channel = ctx.channel
    # await ctx.channel.send("Available Tags:  \n ☯Anime \n ⌘Developer \n ✎Economics \n ✌Fun \n ☣Gaming \n ∞Kpop \n (≖_≖ )Meme \n ♫Music \n ✔Poll \n ✉Reddit \n ☃Roleplay \n ʕ•́ᴥ•̀ʔっSocial \n ᕙ(`▿´)ᕗStream")
    embed = discord.Embed(title="Available Tags:", description=" \n ☯Anime \n :computer:Developer \n :pencil:Economy \n ✌Fun \n :video_game:Gaming \n :revolving_hearts:Kpop \n :frog:Meme \n :headphones:Music \n :bar_chart:Poll \n :ribbon:Reddit \n :jack_o_lantern:Roleplay \n :people_hugging:Social \n :tv: Stream", color=0x00D166)
    await ctx.channel.send(embed=embed)

# @client.command()
# async def embed(ctx):
  #   embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
   #  await ctx.send(embed=embed)

# random---------------


@client.command()
async def getanime(ctx):
    channel = ctx.channel
    i = random.randrange(68)
    await ctx.channel.send(anime.at[i, "url"])


@client.command()
async def getdeveloper(ctx):
    channel = ctx.channel
    i = random.randrange(6)
    await ctx.channel.send(developer.at[i, "url"])


@client.command()
async def geteconomy(ctx):
    channel = ctx.channel
    i = random.randrange(69)
    await ctx.channel.send(economy.at[i, "url"])


@client.command()
async def getfun(ctx):
    channel = ctx.channel
    i = random.randrange(70)
    await ctx.channel.send(fun.at[i, "url"])


@client.command()
async def getgaming(ctx):
    channel = ctx.channel
    i = random.randrange(39)
    await ctx.channel.send(gaming.at[i, "url"])


@client.command()
async def getkpop(ctx):
    channel = ctx.channel
    i = random.randrange(8)
    await ctx.channel.send(kpop.at[i, "url"])


@client.command()
async def getmeme(ctx):
    channel = ctx.channel
    i = random.randrange(70)
    await ctx.channel.send(meme.at[i, "url"])


@client.command()
async def getmusic(ctx):
    channel = ctx.channel
    i = random.randrange(70)
    await ctx.channel.send(music.at[i, "url"])


@client.command()
async def getpoll(ctx):
    channel = ctx.channel
    i = random.randrange(12)
    await ctx.channel.send(poll.at[i, "url"])


@client.command()
async def getreddit(ctx):
    channel = ctx.channel
    i = random.randrange(70)
    await ctx.channel.send(reddit.at[i, "url"])


@client.command()
async def getroleplay(ctx):
    channel = ctx.channel
    i = random.randrange(70)
    await ctx.channel.send(roleplay.at[i, "url"])


@client.command()
async def getsocial(ctx):
    channel = ctx.channel
    i = random.randrange(70)
    await ctx.channel.send(social.at[i, "url"])


@client.command()
async def getstream(ctx):
    channel = ctx.channel
    i = random.randrange(70)
    await ctx.channel.send(stream.at[i, "url"])


# top3--------------
@client.command()
async def top3anime(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(anime.at[i, "url"])


@client.command()
async def top3developer(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(developer.at[i, "url"])


@client.command()
async def top3gaming(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(gaming.at[i, "url"])


@client.command()
async def top3fun(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(fun.at[i, "url"])


@client.command()
async def top3kpop(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(kpop.at[i, "url"])


@client.command()
async def top3economy(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(economy.at[i, "url"])


@client.command()
async def top3roleplay(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(roleplay.at[i, "url"])


@client.command()
async def top3social(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(social.at[i, "url"])


@client.command()
async def top3stream(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(stream.at[i, "url"])


@client.command()
async def top3poll(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(poll.at[i, "url"])


@client.command()
async def top3music(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(music.at[i, "url"])


@client.command()
async def top3meme(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(meme.at[i, "url"])


@client.command()
async def top3reddit(ctx):
    channel = ctx.channel
    for i in range(3):
        await ctx.channel.send(reddit.at[i, "url"])


client.run(key)
