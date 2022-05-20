from datetime import datetime
from sys import prefix
import requests as r
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def supl(ctx):

    odpoved = r.get("https://skripta.ssps.cz/substitutions.php/?date=20220520")

    data = json.loads(odpoved.content)

    for i in data["ChangesForClasses"]:
        if (i["Class"]["Abbrev"] == "1.B"):
            currentWeekDay = datetime.today().weekday()
            currentWeekDayToString = ""

            if (currentWeekDay == 0):
                currentWeekDayToString = "pondělí"
            elif (currentWeekDay == 1):
                currentWeekDayToString = "úterý"
            elif (currentWeekDay == 2):
                currentWeekDayToString = "středa"
            elif (currentWeekDay == 3):
                currentWeekDayToString = "čtvrtek"
            elif (currentWeekDay == 4):
                currentWeekDayToString = "pátek"


            messageToSend = f"Suplování pro {currentWeekDayToString}\n"
            for j in i ["CancelledLessons"]:
                predmet = j["Subject"]
                ucitel = j["ChgType2"]
                skupina = j["Group"]
                typ = j["ChgType1"]
                hodina = j["Hour"]
                messageToSend += f"1.B {predmet} {ucitel} {skupina} {typ} {hodina}. hodina\n"
            await ctx.send(messageToSend)
                

bot.run('Token')
