# Import Discord Package
import discord
import json
from discord.ext import commands, tasks
import pandas as pd
import os
from itertools import cycle
import youtube_dl
from random import choice
from discord import Embed
from datetime import datetime
from discord.utils import get
from discord.voice_client import VoiceClient
import random



os.chdir("C:\\Users\\jitenpatel\\Desktop\\DiscordTestBot")



# Client (our bot)

  











client = commands.Bot(command_prefix = '/')
client.remove_command('help')













            









@client.command(pass_context=True)
async def help(context):
    author = context.message.author

    myEmbed = discord.Embed(title="NEO BASIC COMMANDS-", description="COMMANDS FOR EVERYONE!", color=0xff0000)
    myEmbed.add_field(name="/serverinfo", value= "Gives information of the following server", inline=False)
    myEmbed.add_field(name="/userinfo @<USERNAME>", value= "Gives information of the tagged user", inline=False)
    myEmbed.add_field(name="/version", value= "Loads information about NEO", inline=False)
    myEmbed.add_field(name="/ping", value="Gives you Pong!", inline=False)
    myEmbed.add_field(name="/hi", value="Type and you will get something nice or something bad!", inline=False)
    myEmbed.add_field(name="/latency", value= "Tells you your internet latency!", inline=False)
    myEmbed.add_field(name="/meme", value= "Shows up a random meme!", inline=False)
    myEmbed.add_field(name="/ban @<USERNAME><REASON>", value="Bans the tagged user!", inline=False)
    myEmbed.add_field(name="/kick @<USERNAME><REASON>", value= "Kicks the tagged user!", inline=False)
    myEmbed.add_field(name="/load", value= "Loads a command", inline=False)
    myEmbed.add_field(name="/poll <OPTION1> or <OPTION2>", value="For conducting a poll", inline=False)
    myEmbed.add_field(name="/unload", value= "Unloads a command", inline=False)
    myEmbed.add_field(name="/clear  <NUMBER OF MESSAGES TO CLEAR>", value="Clears the number of messages specified", inline=False)
    myEmbed.add_field(name="/balance", value="To see your Bank balance!", inline=False)
    myEmbed.add_field(name="/beg", value="To beg for points!", inline=False)
    myEmbed.add_field(name="/slot <AMOUNT>", value="See whether you get a TREAT of the specifed amount or TRICK of the specified amount!", inline=False)
    myEmbed.add_field(name="/withdraw <AMOUNT>", value="To withdraw the specified amount of points from your bank!", inline=False)
    myEmbed.add_field(name="/deposit <AMOUNT>", value="To deposit specified amount of points!", inline=False)
    myEmbed.add_field(name="/send @<USERNAME> <AMOUNT>", value="To send tagged user a specified amount of points!", inline=False)
    myEmbed.add_field(name="/rob @<USERNAME>", value="To rob tagged user for points!(Only for users having more than 1K points!)", inline=False)
    myEmbed.set_footer(text="This bot is created by 冬GAMEX冬VYRUS#3546")
    myEmbed.set_author(name="NEO")


    await context.send(f"{context.author.mention} **check your DM!**")
    await author.send(embed=myEmbed)
  

















@client.command(name= 'serverinfo')
async def serverinfo(context):
    name = str(context.guild.name)
    description = str(context.guild.description)
    owner = str(context.guild.owner)
    id = str(context.guild.id)
    region = str(context.guild.region)
    memberCount = str(context.guild.member_count)
    icon = str(context.guild.icon_url)


    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner-", value=owner, inline=True)
    embed.add_field(name="Server ID-", value=id, inline=True)
    embed.add_field(name="Region-", value=region, inline=True)
    embed.add_field(name="Member Count-", value=memberCount, inline=True)
    

    await context.send(embed=embed)




















async def open_account(user):
    
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0


    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True       




async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users    




@client.command(name= 'balance')
async def balance(context):
    await open_account(context.author)
    user = context.author 
    
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]


    embed = discord.Embed(title = f"{context.author.name}'s balance", color = discord.Color.dark_green())
    embed.add_field(name = "Wallet Balance", value = wallet_amt)
    embed.add_field(name = "Bank Balance", value = bank_amt)
    await context.send(embed = embed)



@client.command(name= 'beg')
async def beg(context):
    await open_account(context.author)
    user = context.author
    
    users = await get_bank_data()


    earnings = random.randrange(101)

    await context.send(f"Someone just gave you {earnings} coins!")



    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(users,f)



async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]    
    return bal


@client.command(name= 'withdraw')
async def withdraw(context,amount = None):
    await open_account(context.author)
    if amount == None:
        await context.send("Please enter the amount")
        return

    bal = await update_bank(context.author)

    amount = int(amount)
    if amount>bal[1]:
        await context.send("You don't have enough points!")
        return
    if amount<0:
        await context.send("The amount must be positive and above 0!")
        return   

    await update_bank(context.author,amount)
    await update_bank(context.author,-1*amount,"bank")
    await context.send(f"You have withdrawed {amount} points succesfully!")







@client.command(name= "meme")
async def meme(context):


    images = ["Lmaooo.png", "meme1.png", "meme2.png", "meme3.png", "meme4.png", "meme5.png", "meme6.png", "meme7.png", "meme8.png", "meme9.png", "meme10.png", "meme11.png", "meme12.png", "meme13.png", "meme14.png", "meme15.png", "meme16.png", "meme17.png", "meme18.png"]
    random_image = random.choice(images)

    await context.send(file=discord.File(random_image))



    











@client.command(name= 'deposit')
async def deposit(context,amount = None):
    await open_account(context.author)
    if amount == None:
        await context.send("Please enter the amount")
        return

    bal = await update_bank(context.author)

    amount = int(amount)
    if amount>bal[0]:
        await context.send("You don't have enough points!")
        return
    if amount<0:
        await context.send("The amount must be positive and above 0!")
        return   

    await update_bank(context.author,-1*amount)
    await update_bank(context.author,amount,"bank")
    await context.send(f"You have deposited {amount} points succesfully!")







@client.command(name= 'send')
async def send(context, member:discord.Member, amount = None):
    await open_account(context.author)
    await open_account(member)

    if amount == None:
        await context.send("Please enter the amount")
        return

    bal = await update_bank(context.author)
    if amount == "all":
        amount = bal[0]

    amount = int(amount)
    if amount>bal[1]:
        await context.send("You don't have enough points!")
        return
    if amount<0:
        await context.send("The amount must be positive and above 0!")
        return   

    await update_bank(context.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")
    await context.send(f"You gave {amount} points succesfully!")





@client.command(name= 'slot')
async def slot(context, amount = None):
    await open_account(context.author)
    if amount == None:
        await context.send("Please enter the amount")
        return

    bal = await update_bank(context.author)

    amount = int(amount)
    if amount>bal[0]:
        await context.send("You don't have enough points!")
        return
    if amount<0:
        await context.send("The amount must be positive and above 0!")
        return

    final = []
    for i in range(5):
        a = random.choice(["🎃","👻","💀","🦇","😈"])
        final.append(a)

    await context.send(str(final))

    if final[0] == final[1] or final[0] == final[4] or final[4] == final[1]:     
      
        await update_bank(context.author,2*amount)
        await context.send(f"Good Luck!! You get a **TREAT** of **{amount}**!!")
    else:
         await update_bank(context.author,-1*amount)   
         await context.send(f"Bad Luck!! You got a **TRICK** of **{amount}**!!")





@client.command(name= 'rob')
async def rob(context, member:discord.Member):
    await open_account(context.author)
    await open_account(member)

    

    bal = await update_bank(member)

    
    if bal[0]<10000:
        await context.send("It's useless to rob this little poor ||lad||! He doesn't have above 1K points in his bank!!")
        return
       
    earnings = random.randrange(0, bal[0])

    await update_bank(context.author,earnings)
    await update_bank(member,-1*earnings)
    await context.send(f"You robbed {earnings} points succesfully from {context.member.mention}!")










@client.event
async def on_member_join(member, context):
    
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention} to {context.guild.name} by {context.guild.owner}. Type `/help` command for details!')




 
@client.command(name= 'latency')
async def latency(context):
    await context.send(f'*{context.author.mention},Your Latency is*  **{round(client.latency * 1000)}ms**')



@client.command(name= 'hi')
async def Hello(context):
    responses = ['***Bruh...*** **Why did you woke me? You know i was resting, you ||lad||!**', '**What do you want now?**', f"**Heyo {context.author.mention}! Looking nice today!**", f"**HI {context.author.mention}!**"]
    await context.send(choice(responses))        



@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await context.send('Please pass in right commands. Type **/help** for more info!')


@client.command(name= 'userinfo')
async def userinfo(context, member: discord.Member):
    

    roles = [role for role in member.roles]
    

    embed = discord.Embed(colour=member.color, timestamp=context.message.created_at, title="Userinfo")

    embed.set_author(name=f"User Info - {member}",)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {context.author}", icon_url=context.author.avatar_url)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="In-Server name:", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name=f"Top role:", value=member.top_role.mention)
    embed.add_field(name="Bot?", value=member.bot)
    embed.set_footer(text=f'Asked by {context.author.mention}') 

    await context.send(embed=embed)




@client.command()
@commands.has_permissions(manage_messages=True)
async def load(context, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
@commands.has_permissions(manage_messages=True)
async def unload(context, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')     


@client.command(name='version')
async def version(context):

   myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
   myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
   myEmbed.add_field(name="Date Released:", value="October 5,2020", inline=False)
   myEmbed.set_footer(text="This bot is created by 冬GAMEX冬VYRUS#3546")
   myEmbed.set_author(name="NEO")

   await context.message.channel.send(embed=myEmbed)




@client.command()
@commands.has_permissions(kick_members=True)
async def kick(context, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await context.send('User ' + member.display_name + ' has been kicked!')



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(context, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await context.send(f'Banned {member.mention}')  


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(context, *, member):
    banned_users = await context.guild.bans()
    member_name, member_discriminator = member.split('#')


    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await context.guild.unban(user)
            await context.send(f'Unbanned {user.mention}')
            return





@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(context, amount=2):
    await context.channel.purge(limit=amount)



@client.command(name= 'poll', aliases = ['pl'])
async def poll(context,*, message):
    channel = context.channel
    try:
        op1 , op2 = message.split("or")
        txt = f"React with ✅ for {op1} or ❎ for {op2}"
    except:
        await channel.send("Correct Syntax: [Choice1] or [Choice2]")
        return



    embed = discord.Embed(title="Poll", description = txt, colour = discord.Colour.red())
    message_ = await channel.send(embed=embed)
    await message_.add_reaction("✅")
    await message_.add_reaction("❎")
    await context.message.delete()












@client.event
async def on_message(message):



   if "/help" in message.content:
       await message.add_reaction("☑️")
    


    
   if message.content == 'what is the version':
        general_channel = client.get_channel(720567133960011776)

        myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="v1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="October 5,2020", inline=False)
        myEmbed.set_footer(text="This is a sample footer!")
        myEmbed.set_author(name="VYRUS")

        await general_channel.send(embed=myEmbed)

   

   if message.content == "/append":

        #Add a row to my Dataframe that contains message.
        df = pd.read_csv('C:\\Users\\jitenpatel\\Desktop\\DiscordTestBot\\output.csv', index_col=0)
        df = df.append({"A": 'This is the message i want to append'}, ignore_index=True)
        df.to_csv('C:\\Users\\jitenpatel\\Desktop\\DiscordTestBot\\output.csv')

   await client.process_commands(message)


@client.event
async def on_ready():
    
    print('NEO is online!')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(' /help'))   

    #df = pd.DataFrame({"A": ['Hello', 'Test']})
    #df.to_csv('C:\\Users\jitenpatel\Desktop\DiscordTestBot\output.csv')


# Run the client on the server
client.run('NzcwMTU0MjAxMjQ1NDE3NDgz.X5Zb_g.A3Lt00TinrY_TBsmhn_092AoQm0')
