import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
from discord.utils import get, find
from discord.ext.commands import command, cooldown, BucketType, CommandOnCooldown
import sys
from discord import Embed, utils
import aiohttp
import os
import json
import datetime
import shutil
from os import system
import urllib.parse, urllib.request, re
import time
import asyncio
import traceback
import sqlite3
import youtube_dl
from random import randint



intents = discord.Intents.all()
intents.members = True


bot = commands.Bot(command_prefix = "+", description = "Yako", intents = intents)
songs = asyncio.Queue()
play_next_song = asyncio.Event()

@bot.event
async def on_ready():
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(status=discord.Status.do_not_disturb, activity = discord.Activity(
        type = discord.ActivityType.watching,

        #Bot status
        name = f'{members} membres' 

    ))
    print('Ready to support ✅')

    

@bot.command()
@cooldown(1, 2, commands.BucketType.guild)
async def ping(ctx):
    embed = discord.Embed(description=f'Pong! :ping_pong:  {round(bot.latency * 1000)}ms', colour=discord.Color.red())
    await ctx.send(embed=embed)

@bot.command(aliases=['8ball'])
@cooldown(1, 2, commands.BucketType.guild)
async def _8ball(ctx, *, question):
    responses = ['C\'est certain',
                 'Oui',
                 'Non',
                 'Il y a de fortes chances',
                 'Euh, attendez, je reviens',
                 'Mes sources disent que non',
                 'Inchallah',
                 'Plutot oui',
                 'Sûrement pas',
                 'Pas du tout',
                 'Certainement pas',
                 'Je ne pense pas',]
    embed = discord.Embed(description=f'Question: {question}\nRéponse: {random.choice(responses)}', colour=discord.Color.red())
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandOnCooldown):
        embed = discord.Embed(description=f":no_entry: ┃ Veuillez réessayer dans {error.retry_after:,.2f} secondes ", colour=discord.Color.red())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.NSFWChannelRequired):
        embed = discord.Embed(description=":no_entry: ┃ Vous n'êtes pas dans un salon NSFW", colour=discord.Color.red())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description=":no_entry: ┃ Vous n'avez pas la permission pour utiliser cette commande", colour=discord.Color.red())
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingAnyRole):
        embed = discord.Embed(description=":no_entry: ┃ Vous n'êtes pas DJ", colour=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
@cooldown(1, 2, commands.BucketType.guild)
async def serverlist(ctx):
    serverlist = len(bot.guilds)


    await ctx.send(f"Le bot est sur {serverlist} serveurs")


@bot.command()
async def say(ctx, *texte):

    await ctx.message.delete()
    await ctx.send(" ".join(texte))


@bot.command(aliases=['hug'])
@cooldown(1, 4, commands.BucketType.guild)
async def calin(ctx, *, user: discord.Member):

    who_hugged = ctx.message.author

    gifs = [
        "https://cdn.weeb.sh/images/BkotddXD-.gif",
        "https://cdn.weeb.sh/images/S1qhfy2cz.gif",
        "https://cdn.weeb.sh/images/Sy65_OQvZ.gif",
        "https://cdn.weeb.sh/images/HJU2OdmwW.gif",
        "https://cdn.weeb.sh/images/rJ_slRYFZ.gif",
        "https://cdn.weeb.sh/images/rkYetOXwW.gif",
        "https://cdn.weeb.sh/images/S1a0DJhqG.gif",
        "https://cdn.weeb.sh/images/rJaog0FtZ.gif",
        "https://cdn.weeb.sh/images/HkfgF_QvW.gif",
        "https://cdn.weeb.sh/images/S18oOuQw-.gif",
        "https://cdn.weeb.sh/images/ByuHsvu8z.gif",
        "https://cdn.weeb.sh/images/Hy0KO_7DZ.gif",
        "https://cdn.weeb.sh/images/r1kC_dQPW.gif",
        "https://cdn.weeb.sh/images/Sk80wyhqz.gif",
    ] 
    gif = random.choice(gifs)
    embed = discord.Embed(description=f'{who_hugged.mention} a fait un câlin à {user.mention}!', colour=discord.Color.green())
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Calin")
    await ctx.send(embed=embed)

@bot.command(aliases=['slap'])
@cooldown(1, 4, commands.BucketType.guild)
async def gifle(ctx, *, user: discord.Member, ):
    who_smacked = ctx.message.author
    embed = discord.Embed(description=f"{who_smacked.mention} a giflé {user.mention}!", colour=discord.Color.green())
    gifs = [
        "https://cdn.weeb.sh/images/BJSpWec1M.gif",
        "https://cdn.weeb.sh/images/r1siXJKw-.gif",
        "https://cdn.weeb.sh/images/B1-nQyFDb.gif",
        "https://cdn.weeb.sh/images/S1lf3XkKvW.gif",
        "https://cdn.weeb.sh/images/ry_RQkYDb.gif",
        "https://cdn.weeb.sh/images/HJfXM0KYZ.gif",
        "https://cdn.weeb.sh/images/SJdXoVguf.gif",
        "https://cdn.weeb.sh/images/BkzyEktv-.gif",
        "https://cdn.weeb.sh/images/ByHUMRNR-.gif",
        "https://cdn.weeb.sh/images/BJLCX1Kw-.gif",
        "https://cdn.weeb.sh/images/SkdyfWCSf.gif",
        "https://cdn.weeb.sh/images/B1jk41KD-.gif",
        "https://cdn.weeb.sh/images/B1oCmkFw-.gif",
        "https://cdn.weeb.sh/images/SJL3Q1Fvb.gif",
        "https://cdn.weeb.sh/images/HkHCm1twZ.gif",
        "https://cdn.weeb.sh/images/SkSCyl5yz.gif",
        "https://cdn.weeb.sh/images/HJcoQ1Fwb.gif",
        "https://cdn.weeb.sh/images/BJgsX1Kv-.gif",
        "https://cdn.weeb.sh/images/r1PXzRYtZ.gif",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Gifle")
    await ctx.send(embed=embed)


@bot.command(aliases=['boude'])
@cooldown(1, 4, commands.BucketType.guild)
async def sulk(ctx, *, user: discord.Member, ):
    who_smacked = ctx.message.author
    embed = discord.Embed(description=f"{who_smacked.mention} boude {user.mention}!", colour=discord.Color.green())
    gifs = [
        "https://cdn.weeb.sh/images/H11heJYPZ.gif",
        "https://cdn.weeb.sh/images/S1_HWih0b.gif",
        "https://cdn.weeb.sh/images/BkdB9PuLz.gif",
        "https://cdn.weeb.sh/images/ByG6gkYDZ.gif",
        "https://cdn.weeb.sh/images/HkIclytPW.gif",
        "https://cdn.weeb.sh/images/Hkg7slyFDW.gif",
        "https://cdn.weeb.sh/images/H1lfpxkFw-.gif",
        "https://cdn.weeb.sh/images/H1e83lytw-.jpeg",
        "https://cdn.weeb.sh/images/Hy3plkFDZ.gif",
        "https://cdn.weeb.sh/images/SkRUqPuUf.gif",
        "https://cdn.weeb.sh/images/S1vFlkYwW.gif",
        "https://cdn.weeb.sh/images/B10og1FPb.gif",
        "https://cdn.weeb.sh/images/SJLKgJFPb.gif",
        "https://cdn.weeb.sh/images/HJggqe1FP-.gif",
        "https://cdn.weeb.sh/images/S1Vpeytwb.gif",
        "https://cdn.weeb.sh/images/r1PiHy3cM.gif",
        "https://cdn.weeb.sh/images/SyP6e1tDZ.gif",
        "https://cdn.weeb.sh/images/SylseyKvZ.gif",
        "https://cdn.weeb.sh/images/Bk5D5wuUf.gif",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Boude")
    await ctx.send(embed=embed)


@bot.command(aliases=['regarde'])
@cooldown(1, 4, commands.BucketType.guild)
async def stare(ctx, *, user: discord.Member, ):
    who_smacked = ctx.message.author
    embed = discord.Embed(description=f"{who_smacked.mention} est en train de regarder {user.mention} :eyes: ", colour=discord.Color.green())
    gifs = [
        "https://cdn.weeb.sh/images/BkkqI1YPZ.jpeg",
        "https://cdn.weeb.sh/images/HyHdUJYwW.gif",
        "https://cdn.weeb.sh/images/SyA_LJYPb.png",
        "https://cdn.weeb.sh/images/SygCDUkYPb.gif",
        "https://cdn.weeb.sh/images/rybcUktvb.jpeg",
        "https://cdn.weeb.sh/images/rkHFLyKDZ.gif",
        "https://cdn.weeb.sh/images/B1zZ9LyFDZ.jpeg",
        "https://cdn.weeb.sh/images/rye_F8JKD-.jpeg",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Regarde")
    await ctx.send(embed=embed)


@bot.command()
@cooldown(1, 4, commands.BucketType.guild)
async def check(ctx, *, user: discord.Member, ):
    who_smacked = ctx.message.author
    embed = discord.Embed(description=f"{who_smacked.mention} check {user.mention}! :hand_splayed: ", colour=discord.Color.blurple())
    gifs = [
        "https://cdn.weeb.sh/images/BJnxKJXsZ.gif",
        "https://cdn.weeb.sh/images/HkYzKyXjW.gif",
        "https://cdn.weeb.sh/images/rJYQt1mjZ.gif",
        "https://cdn.weeb.sh/images/B1-7KkQsZ.gif",
        "https://cdn.weeb.sh/images/H1Lj9ymsW.gif",
        "https://cdn.weeb.sh/images/HysYckQs-.gif",
        "https://cdn.weeb.sh/images/B1-7KkQsZ.gif",
        "https://cdn.weeb.sh/images/Sy3ncJmi-.jpeg",
        "https://cdn.weeb.sh/images/r1FWFyQob.gif",
        "https://cdn.weeb.sh/images/S1kKq1XiZ.gif",
        "https://cdn.weeb.sh/images/ByRqqy7jb.gif",
        "https://cdn.weeb.sh/images/Hy_U1QBT-.gif",
        "https://cdn.weeb.sh/images/rJzn5kms-.gif",
        "https://cdn.weeb.sh/images/rJenY1XsW.gif",
        "https://cdn.weeb.sh/images/r1MMK1msb.gif",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Check")
    await ctx.send(embed=embed)


@bot.command(aliases=['punch'])
@cooldown(1, 4, commands.BucketType.guild)
async def frappe(ctx, *, user: discord.Member, ):
    who_smacked = ctx.message.author
    embed = discord.Embed(description=f"{who_smacked.mention} a frappé {user.mention}!", colour=discord.Color.green())
    gifs = [
        "https://cdn.weeb.sh/images/BkdyPTZWz.gif",
        "https://cdn.weeb.sh/images/SJAfH5TOz.gif",
        "https://cdn.weeb.sh/images/ByI7vTb-G.gif",
        "https://cdn.weeb.sh/images/BJXxD6b-G.gif",
        "https://cdn.weeb.sh/images/rJRUk2PLz.gif",
        "https://cdn.weeb.sh/images/BJg7wTbbM.gif",
        "https://cdn.weeb.sh/images/SkFLH129z.gif",
        "https://cdn.weeb.sh/images/B1rZP6b-z.gif",
        "https://cdn.weeb.sh/images/HJqSvaZ-f.gif",
        "https://cdn.weeb.sh/images/SJR-PpZbM.gif",
        "https://cdn.weeb.sh/images/SyYbP6W-z.gif",
        "https://cdn.weeb.sh/images/rJHLDT-Wz.gif",
        "https://cdn.weeb.sh/images/SJvGvT-bf.gif",
        "https://cdn.weeb.sh/images/B1-ND6WWM.gif",
        "https://cdn.weeb.sh/images/HkFlwpZZf.gif",
        "https://cdn.weeb.sh/images/ryYo_6bWf.gif",
        "https://cdn.weeb.sh/images/ryYo_6bWf.gif",
        "https://cdn.weeb.sh/images/rkkZP6Z-G.gif",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Frappe")
    await ctx.send(embed=embed)


@bot.command(aliases=['dance'])
@cooldown(1, 4, commands.BucketType.guild)
async def danse(ctx):
    who_smacked = ctx.message.author
    embed = discord.Embed(description=f"{who_smacked.mention} est en train de danser :man_dancing: !", colour=discord.Color.green())
    gifs = [
        "https://cdn.weeb.sh/images/Hke6uUXwb.gif",
        "https://cdn.weeb.sh/images/HJUd_LXwW.gif",
        "https://cdn.weeb.sh/images/BJeGC_87DW.gif",
        "https://cdn.weeb.sh/images/Synj_ImDb.gif",
        "https://cdn.weeb.sh/images/SJo040wTW.gif",
        "https://cdn.weeb.sh/images/HkxwwOUXvZ.gif",
        "https://cdn.weeb.sh/images/HkbBOUQw-.gif",
        "https://cdn.weeb.sh/images/ryGyYU7vW.gif",
        "https://cdn.weeb.sh/images/B1vJK8XPb.gif",
        "https://cdn.weeb.sh/images/r1geo_Umwb.gif",
        "https://cdn.weeb.sh/images/B1LUuImvZ.gif",
        "https://cdn.weeb.sh/images/S1CV_87vb.gif",
        "https://cdn.weeb.sh/images/Syl3tOL7wW.gif",
        "https://cdn.weeb.sh/images/rJXpOLmD-.gif",
        "https://cdn.weeb.sh/images/H1ha_L7DW.gif",
        "https://cdn.weeb.sh/images/rJPkUkn9G.gif",
        "https://cdn.weeb.sh/images/SyWh_U7PZ.gif",
        "https://cdn.weeb.sh/images/SJWuu8mwW.gif",
        "https://cdn.weeb.sh/images/SkpOHJh5M.gif",
        "https://cdn.weeb.sh/images/BkmPO8Xwb.gif",
        "https://cdn.weeb.sh/images/B1Rtd8XvZ.gif",
        "https://cdn.weeb.sh/images/S1r6uLmvb.gif",
        "https://cdn.weeb.sh/images/HkRqdIXP-.gif",
        "https://cdn.weeb.sh/images/HyeT__Imw-.gif",
        "https://cdn.weeb.sh/images/SkyOOImvW.gif",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Danse")
    await ctx.send(embed=embed)


@bot.command(aliases=['kiss'])
@cooldown(1, 4, commands.BucketType.guild)
async def bisous(ctx, *, user: discord.Member, ):
    who_smacked = ctx.message.author
    embed = discord.Embed(description=f"{who_smacked.mention} a embrassé {user.mention} !", colour=discord.Color.green())
    gifs = [
        "https://cdn.weeb.sh/images/SJn43adDb.gif",
        "https://cdn.weeb.sh/images/BydoCy9yG.gif",
        "https://cdn.weeb.sh/images/rkde2aODb.gif",
        "https://cdn.weeb.sh/images/H1Gx2aOvb.gif",
        "https://cdn.weeb.sh/images/H1a42auvb.gif",
        "https://cdn.weeb.sh/images/ByiMna_vb.gif",
        "https://cdn.weeb.sh/images/BkUJNec1M.gif",
        "https://cdn.weeb.sh/images/rJ6PWohA-.gif",
        "https://cdn.weeb.sh/images/B12LhT_Pb.gif",
        "https://cdn.weeb.sh/images/B13D2aOwW.gif",
        "https://cdn.weeb.sh/images/HJ5khTOP-.gif",
        "https://cdn.weeb.sh/images/SJrBZrMBz.gif",
        "https://cdn.weeb.sh/images/r10UnpOPZ.gif",
        "https://cdn.weeb.sh/images/SJJUhpOD-.gif",
        "https://cdn.weeb.sh/images/Skv72TuPW.gif",
        "https://cdn.weeb.sh/images/Bkuk26uvb.gif",
        "https://cdn.weeb.sh/images/BJMX2TuPb.gif",
        "https://cdn.weeb.sh/images/rypMnpuvW.gif",
        "https://cdn.weeb.sh/images/SJ8I2Tuv-.gif",
        "https://cdn.weeb.sh/images/ryEvhTOwW.gif",
        "https://cdn.weeb.sh/images/HkZyXs3A-.gif",
        "https://cdn.weeb.sh/images/H1e7nadP-.gif",
        "https://cdn.weeb.sh/images/rymvn6_wW.gif",
        "https://cdn.weeb.sh/images/S1y-4l5Jf.gif",
        "https://cdn.weeb.sh/images/BJSdQRtFZ.gif",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Bisous")
    await ctx.send(embed=embed)


@bot.command()
@cooldown(1, 4, commands.BucketType.guild)
async def wasted(ctx):

    embed = discord.Embed(colour=discord.Color.dark_gold())
    gifs = [
        "https://cdn.weeb.sh/images/B1qosktwb.gif",
        "https://cdn.weeb.sh/images/BJO2j1Fv-.gif",
        "https://cdn.weeb.sh/images/B1VnoJFDZ.gif",
        "https://cdn.weeb.sh/images/r11as1tvZ.gif",
        "https://cdn.weeb.sh/images/HyXTiyKw-.gif",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Wasted")
    await ctx.send(embed=embed)

    

@bot.command(aliases=['landscape'])
@cooldown(1, 4, commands.BucketType.guild)
async def paysage(ctx):

    embed = discord.Embed(colour=discord.Color.dark_gold())
    gifs = [
        "https://cdn.discordapp.com/attachments/722389463199907901/739630444210946068/1QaUIpB.jpg",
        "https://cdn.discordapp.com/attachments/738388294060081174/739631105367605268/b044af6aa239b2fe08d1b51d569d6957.png",
        "https://cdn.discordapp.com/attachments/738388294060081174/739631387446870036/AS0893_26-10-2015__japon.png",
        "https://cdn.discordapp.com/attachments/738388294060081174/739631625981132861/6dc58e01bbdffc128662cdea0d5dcbe0.png",
        "https://cdn.discordapp.com/attachments/738388294060081174/739631923709739078/0fe4255df5a6ef28e4e1bce3ae154320.png",
        "https://cdn.discordapp.com/attachments/738388294060081174/739634080181780511/796a588be5e9dae7d6d01cd7abff432e.png",
        "https://cdn.discordapp.com/attachments/738388294060081174/739634315431772260/f3c9b02c8d95c777eabd11f4927ac6d4.png"
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    embed.set_footer(text="La Parade ┃ Paysage")
    await ctx.send(embed=embed)


@bot.command()
@cooldown(1, 2, commands.BucketType.guild)
@commands.has_permissions(manage_nicknames=True)
async def pseudo(ctx, user: discord.Member, nickname):
    await user.edit(nick=nickname)
    embed = discord.Embed(description=f"Le pseudo de {user} a été changé en {nickname}", colour=discord.Color.purple())
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx,
               user: discord.User,
               *,
               reason="Aucune raison n'a été renseignée!"):

    await ctx.message.delete()
    embed = discord.Embed(title="Un utilisateur a reçu un warn ",
                          description="Un modérateur/admin a averti un membre",
                          color=discord.Color.red())
    embed.set_thumbnail(
        url=
        "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffr%2Ficone-gratuite%2Fpanneau-davertissement_5766521&psig=AOvVaw0VDaHMfX_9FZE2p7WKYOe_&ust=1651762616270000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCKDilLWNxvcCFQAAAAAdAAAAABAD"
    )
    embed.add_field(name="Membre averti:",
                    value=user.name + "#" + str(user.discriminator))
    embed.add_field(name="concernant:",
                    value=ctx.author.name + "#" +
                    str(ctx.author.discriminator))
    embed.add_field(name="Raison:", value=reason, inline=False)
    await ctx.send(embed=embed)


@bot.command()
@cooldown(1, 2, commands.BucketType.guild)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(description=f":o: ┃ {member} s'est fait emprisonner dans le nouveau monde car il a {reason}", colour=discord.Color.yellow())
        await ctx.send(embed=embed)
  
@bot.command()
async def serverinfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. \nCe serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
	await ctx.send(message)

@bot.command()
async def chinois(ctx, *text):
	chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))



@bot.command()
async def cuisiner(ctx):
	await ctx.send("Envoyez le plat que vous voulez cuisiner")

	def checkMessage(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	try:
		recette = await bot.wait_for("message", timeout = 10, check = checkMessage)
	except:
		await ctx.send("Veuillez réitérer la commande.")
		return
	message = await ctx.send(f"La préparation de {recette.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
	await message.add_reaction("✅")
	await message.add_reaction("❌")


	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
		if reaction.emoji == "✅":
			await ctx.send("La recette a démarré.")
		else:
			await ctx.send("La recette a bien été annulé.")
	except:
		await ctx.send("La recette a bien été annulé.")

@bot.command(aliases=['Csc'])
@cooldown(1, 4, commands.BucketType.guild)
async def csc(ctx,):
    embed = discord.Embed(description="contre son camps la un peu ")
    gifs = [
        "https://tenor.com/view/foot-meme-cest-le-pire-but-contre-son-camp-qui-pouvait-arriver-gif-26451866",
    ]
    gif = random.choice(gifs)
    embed.set_image(url=gif)
    await ctx.send(embed=embed)




@bot.command(aliases=['reglement'])
async def règlement(ctx):
    embed=discord.Embed(title="Voici le règlement du discord !", url="https://www.tiktok.com/@fxgamer737", description="**• __Le Respect__**\n"
                                                        "Il est obligatoire de se respecter les uns et les autres. Les conflits, le manque de respect, la provocation et les insultes sont interdits au sein de notre équipe (sauf si c'est au deuxième degrés.)\n"
                                                       "Conseil: Si vous avez un problème avec un membre du serveur, contactez un Staff et/ou parlez-en avec ce membre en privé.\n"
                                                       "**•__La vulgarité et les rapport sexuelle__ **\n"
                                                     "Il est strictement interdit de faire des rapport sexuelle et de critiqué les formes du corps !\n"
                                                     " La vulgarité n'est pas autoriser, Il est également interdit d'harceler tout cela peut prendre des mesures très grave!\n"
                                                     "**•__La Publicité__ **\n"
                                                     "L'envoie d'un lien pour son serveur n'est pas toléré sur le serveur.\n"
                                                     "L'envoie d'un lien d'un autre serveur est interdit.\n"
                                                     "Conseil : Si un nouveau membre vient vous faire de la publicité en privé, contactez directement un Staff.\n"
                                                     "**•__Spam / Flood__ **\n"
                                                     "Il est interdit de spam plusieurs fois le même message.\n"
                                                     "**• __Racisme / Discrimination__ **\n"
                                                     "Il est bien évidemment interdit d'évoquer l'un de ses sujets. La sanction pourrait être très lourde, pouvant même conduire à la justice.\n"
                                                     "**•__La spécificité des salons__ **\n"
                                                     "Chacun de ses salons a une spécificité, merci de les respecter.\n"
                                                       
                                                       
                                                       
                                                       
                                                       
                                                       , color=0xFFB90F)
         

    embed.set_thumbnail(url="https://www.ellipseformation.com/images/pictos/ellipse-formation-reglement-interieur.png")
    embed.set_footer(text="La parade ┃ règlement")
 
    await ctx.send(embed=embed)

@bot.command(aliases=['clean', 'delmsgs'])
@commands.has_permissions(manage_messages = True)
async def clear( ctx, limit = 100 ): # or any limit you like
    await ctx.channel.purge( limit = limit )
    embed = discord.Embed(title = f'Supprimé {limit} messages dans ce canal.', description = f'Merci à {ctx.author} pour libérer le canal')
    await ctx.send(embed = embed)    


@bot.command()
async def roulette(ctx):
    await ctx.send(
        "La roulette commencera dans 10 secondes. Envoyez \"moi\" dans ce channel pour y participer."
    )

    players = []

    def check(message):
        return message.channel == ctx.message.channel and message.author not in players and message.content == "moi"

    try:
        while True:
            participation = await bot.wait_for('message',
                                               timeout=10,
                                               check=check)
            players.append(participation.author)
            print("Nouveau participant : ")
            print(participation)
            await ctx.send(
                f"**{participation.author.name}** participe au tirage ! Le tirage commence dans 10 secondes"
            )
    except:  #Timeout
        print("Demarrage du tirrage")

    gagner = ["ban", "kick", "role personnel", "mute", "gage"]

    await ctx.send("Le tirage va commencer dans 3...")
    await asyncio.sleep(1)
    await ctx.send("2")
    await asyncio.sleep(1)
    await ctx.send("1")
    await asyncio.sleep(1)
    loser = random.choice(players)
    price = random.choice(gagner)
    await ctx.send(f"La personne qui a gagnée un {price} est...")
    await asyncio.sleep(1)
    await ctx.send("**" + loser.name + "**" + " !")


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="__**Info**__",
        description=
        ("**Hey !**" +
         "__ pour vous servir j'ai était créer pour servir nos membres\n"
         "**Info:**\n"
         "**Créateur**: **`FXgamer737#0001`**\n"
         "**Langage : `Python`**\n"
         "**Serveur** : **https://discord.gg/cqQu6fYGrZ**\n"),
        color=0xFF5733)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def activity(ctx, *, activity):
    await bot.change_presence(activity=discord.Game(name=activity))
    await ctx.send(f" L'activité du bot est passée à  {activity}")


@bot.command()
async def role(ctx):
    member = ctx.message.author
    roles = [role.mention for role in member.roles[1:]]  # don't get @everyone
    roles.append('@everyone')  # set string @everyone instead of role
    await ctx.send(" ".join(roles))

@bot.command(aliases=['kaz'])
async def Kaz(ctx):
    embed=discord.Embed(
        title='kaz i love you <3!',
        description="Kazaame est magnifique et super intelligente cest une giga blg kaz la plus belle la reine du monde la plus belle l'excellence elle est extraordinaire unique:heart_eyes::heart_eyes::heart_eyes:",
        color=0xFF5733)
    embed.set_thumbnail(url="https://images5.alphacoders.com/120/1202237.jpg")
    embed.set_image(url="https://i.pinimg.com/736x/6b/ac/a6/6baca6b8ad8deaa2e4bf79ac2edf32c2.jpg")


    await ctx.send(embed=embed)

@bot.command()
async def este(ctx):
    embed=discord.Embed(
        title='**__Esteban__**',
        description='**Depuis notre rencontre**, tu m’as apporté plein de belle chose. Tu m’as rendu meilleur et j’aime penser que je t’apporte aussi du bonheur. Je t’aime de tout mon cœur et je souhaite t’épouser. Tu es une femme qui possède tout ce qu’un homme peut désirer pour vivre heureux et j’espère avoir la chance de pouvoir enfin t’appeler ma femme.',
        color=0x774dea)
    embed.set_thumbnail(url="https://www.pngmart.com/files/1/Wedding-Ring-PNG-Clipart.png")


    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
   if 'discord.gg' in message.content:
      await message.delete()
      await message.channel.send(f"{message.author.mention} N'envoyez pas de liens!")
   else:
      await bot.process_commands(message)

@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(1057459107516391486)
    await channel.send(f"En cette belle journée nous déplorons la perte d'un membre bien aimé, {member.mention}.")
  

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(1057459107516391486)
    await channel.send(f"Acceuillons a bras ouvert {member.mention} ! Bienvenue dans ce magnifique serveur :)")

@bot.command()
@commands.has_permissions(administrator=True)
async def addrole(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role) 
    await ctx.send(f"{role} est ajouté à {member}.")

@bot.command()
@commands.has_permissions(administrator=True)
async def removerole(ctx, member : discord.Member, role : discord.Role):
    await member.remove_roles(role) 
    await ctx.send(f"{role} est retiré de {member}.")

@bot.command()
async def dm(ctx, user: discord.User, *, message):
    await user.send(message)
    await ctx.message.delete()
    await ctx.send("Message envoyé !")

@bot.command()
async def alldm(ctx, *, message):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"Sent {user.name} a DM.")
        except:
            print(f"Couldn't DM {user.name}.")
    print("Sent all the server a DM.")
  
bot.run("MTAxNTIxODIwMjE2ODUzMjk5Mg.G5wnsT.JJQBCWjYfnJsd1fLWrbe7zmgrlvRCiJZSReg4M")
