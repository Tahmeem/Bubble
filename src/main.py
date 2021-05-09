import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import MemberConverter
import csv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.command(name = "image", help = 'Sends out images to users with a footer')
async def flyers(ctx, arg1):
    CSVfile = await ctx.message.attachments[0].to_file()
    CSVfile.filename = ctx.message.attachments[0].filename
    memberList = []
    with open(f'{CSVfile.filename}', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rowContent = row[0]
            converter = MemberConverter()
            member = await converter.convert(ctx, rowContent)
            memberList.append(member)
    await ctx.send("Upload image now in jpeg or png format")
    def check(m):
        return (m.attachments[0].content_type == "image/jpeg") or (m.attachments[0].content_type == "image/png")
    msg = await bot.wait_for('message', check=check)

    file = await msg.attachments[0].to_file()
    file.filename = f'{CSVfile.filename}image.png'
    embed = discord.Embed()
    embed.set_image(url=f'attachment://{CSVfile.filename}image.png')
    embed.set_footer(text = arg1)
    for member in memberList:
        await member.send(file = file,embed = embed)



@bot.command(name = "website", help = 'Sends out website link with a description')
async def promo(ctx):
    CSVfile = await ctx.message.attachments[0].to_file()
    CSVfile.filename = ctx.message.attachments[0].filename
    memberList = []
    with open(f'{CSVfile.filename}', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rowContent = row[0]
            converter = MemberConverter()
            member = await converter.convert(ctx, rowContent)
            memberList.append(member)

    embed = discord.Embed(title="Intact Insurance", url="https://www.intact.ca/on/en/personal-insurance.html",
                          description="To find out more about us and our insurance plans visit our website",
                          color=discord.Color.blue())
    await ctx.send("Your message(s) has been sent!")
    for member in memberList:
        await member.send(embed=embed)

@bot.command(name = "contacts", help = "Set up contacts and send to a list of people")
async def contact(ctx):
    CSVfile = await ctx.message.attachments[0].to_file()
    CSVfile.filename = ctx.message.attachments[0].filename
    memberList = []
    with open(f'{CSVfile.filename}', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            rowContent = row[0]
            converter = MemberConverter()
            member = await converter.convert(ctx, rowContent)
            memberList.append(member)

    await ctx.send("Add a name: ")
    def checkForname(e):
        return type(e.content) == str
    name = await bot.wait_for('message', check=checkForname)

    await ctx.send("Add email address: ")
    def checkForemail(e):
        return '@' in e.content
    email = await bot.wait_for('message', check=checkForemail)

    await ctx.send("Add Phone number(no spaces or hypens): ")
    def checkForphone(e):
        return type(int(e.content)) == int
    number = await bot.wait_for('message', check=checkForphone)

    embed = discord.Embed(title="Contact Info for Intact Insurance", url="https://www.intact.ca/on/en/contact-us.html",
                          description = f"If you would like to reach out to us go to the link or call {number.content} or email us at {email.content}",
                          color=discord.Color.blue())
    embed.set_author(name=f"{name.content}",
                     icon_url="http://tny.im/oIH")
    await ctx.send("Your message(s) has been sent!")
    for member in memberList:
        await member.send(embed=embed)

bot.run(TOKEN)