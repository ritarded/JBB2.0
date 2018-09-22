import discord
from discord.ext import commands


class Ascii():
    #module for ascii art
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def asciihum(self):
        a = ("▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒▒▒\n"
             "▒▒▒▒▒▄█▀▀░░░░░░▀▀█▄▒▒▒▒▒\n"
             "▒▒▒▄█▀▄██▄░░░░░░░░▀█▄▒▒▒\n"
             "▒▒█▀░▀░░▄▀░░░░▄▀▀▀▀░▀█▒▒\n"
             "▒█▀░░░░███░░░░▄█▄░░░░▀█▒\n"
             "▒█░░░░░░▀░░░░░▀█▀░░░░░█▒\n"
             "▒█░░░░░░░░░░░░░░░░░░░░█▒\n"
             "▒█░░██▄░░▀▀▀▀▄▄░░░░░░░█▒\n"
             "▒▀█░█░█░░░▄▄▄▄▄░░░░░░█▀▒\n"
             "▒▒▀█▀░▀▀▀▀░▄▄▄▀░░░░▄█▀▒▒\n"
             "▒▒▒█░░░░░░▀█░░░░░▄█▀▒▒▒▒\n"
             "▒▒▒█▄░░░░░▀█▄▄▄█▀▀▒▒▒▒▒▒\n"
             "▒▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒\n")
        await self.bot.say(a)

def setup(bot):
    bot.add_cog(Ascii(bot))
