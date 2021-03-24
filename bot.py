import discord
from discord.ext import commands
import datetime
from discord.utils import get

bot = commands.Bot(command_prefix = '.zp ')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def dm(ctx, *, message):
    await ctx.author.send(f'{message}')

@bot.command()
async def ping(ctx):
    moderator = get(ctx.guild.roles, id=824187269363007490)
    embed = discord.Embed(
    title="Kolokwium z pogramowania",
    colour=discord.Colour(0x108510),
    url="https://discordapp.com",
    description=" Zagadnienia na kolokwium są na stronie [XYZ](https://pl.wikipedia.org/wiki/Programowanie_komputerów)",
    timestamp=datetime.datetime(2021,3,10))

    embed.set_image(url="https://www.perforce.com/sites/default/files/image/2019-01/image-blog-what-code-quality.jpg")

    embed.add_field(name="Termin", value="25.03.2021")
    embed.add_field(name="Role", value=f'{moderator.mention}', inline=True)
    embed.add_field(name="Utworzone przez", value='XYZ', inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def tag_user(ctx, member : discord.Member, *, message):
    await ctx.send(f'{member.mention} {message}')

@bot.command()
async def tag_mod(ctx):
    moderator = discord.utils.get(ctx.guild.roles, id=819239664753573929)
    await ctx.send(f'Hello {moderator.mention}!')


bot.run('ODE5MjMzODI4OTAzODQ1OTE4.YEjo9Q.dW3QwZ_BQirfiPUMl6XIxgJ6RPY')
