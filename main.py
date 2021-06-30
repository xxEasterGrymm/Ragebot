import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from keep_running import keep_running
import random

client = commands.Bot(command_prefix = '.')

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52]

@client.event
async def on_ready():
  print("The bot is ready!")
'''
@client.command()
async def help(ctx):
  await ctx.send("List of Commands for Ichizaya bot\n\n.help\t\t.join\t\t.leave\n.purpleshield\t\t.boombot\t\t.bullshit")
'''

@client.command(pass_context = True)
async def purpleshield(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('1.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def dogshit(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('2.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def norte(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('5.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def bazooka(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('10.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def bodyshot(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('11.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def fuckoff(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('12.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def boombot(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('13.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def armour(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('14.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def jett(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('15.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def how(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('16.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def ma(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('17.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def getlost(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('18.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def gooda(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('19.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def hattbe(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('20.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def noob(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('21.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def cover(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('22.mpeg')
    player = voice.play(source)
    player.start()

@client.command(pass_context = True)
async def join(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    random.shuffle(a)
    source = FFmpegPCMAudio('{}.mpeg'.format(a[0]))
    player = voice.play(source)
    player.start()
  else:
    await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")

@client.command(pass_context = True)
async def leave(ctx):
  voice_client = ctx.guild.voice_client
  await voice_client.disconnect()
'''
@client.command(pass_context = True)
async def next(ctx):
  random.shuffle(a)
  source = FFmpegPCMAudio('{}.mpeg'.format(a[0]))
  channel = ctx.message.author.voice.channel
  #vc = get(self.bot.voice_clients, guild=ctx.guild)
  #channel.play(discord.FFmpegPCMAudio(source))
  
  player = channel.play(source)
  #player.start()
'''
keep_running()
client.run('ODM0MDQ0NjYzMDcyOTQ4Mjg0.YH7Knw.FZG8bLwz8Eg08hvrEh5S4t4U52U')