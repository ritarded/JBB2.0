import discord
import json
import subprocess
from random import randint
from discord.ext import commands

class Interact():
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def hug(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("You have to tell me who to hug!")
        elif size > 1:
            await self.bot.say("Calm down! Hug one at a time!")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("You can't fake human interaction like that!")
        else:
            await self.bot.say("c⌒っ╹v╹ )っ {0}  received a hug from {1}.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def slap(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("You have to tell me who to slap!")
        elif size > 1:
            await self.bot.say("Calm down! You have two hands but can only slap one at a time!")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("You can't slap yourself! Well... You shouldn't.")
        else:
            await self.bot.say("( ‘д‘ ⊂ 彡☆))Д´) {0} received a slap from {1}.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def punch(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("You have to tell me who to punch!")
        elif size > 1:
            await self.bot.say("Calm down! I advise you to first punch the worst one!")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("You can punch yourself! But first you should get some help.")
        else:
            await self.bot.say("(*＇Д＇)ﾉｼ)ﾟﾛﾟ ) {0} was punched by {1}.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))
    
    @commands.command(pass_context=True)
    async def whip(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("You have to tell me who to whip!")
        elif size > 1:
            await self.bot.say("I know you are kinky, but please whip one at a time!")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("Perhaps you sould ask someone to do that for you.")
        else:
            await self.bot.say("(˵ ͡~ ͜ʖ ͡°˵)ﾉ⌒{0} was whipped by {1}.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def table(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("Tell me who made you flip tables!")
        elif size > 1:
            await self.bot.say("It is not healthy to flip more than one table at once.")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("You shouldn't make yourself flip tables.")
        else:
            await self.bot.say("(╯°□°）╯︵ ┻━┻ {0} just made {1} flip.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def snipe(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("Tell me who to snipe!")
        elif size > 1:
            await self.bot.say("You are using a sniper. Not a minigun.")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("you could just do a flip.")
        elif randint(0,9) == 0:
            await self.bot.say("Oh no! You failed the shot, like everything you do in your life.")
        else:
            await self.bot.say("︻デ═一 {0} was sniped by {1}.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def giveup(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("Tell me who made you lose fate in humanity!")
        elif size > 1:
            await self.bot.say("You should lose hope in one person at a time.")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("You matter, unless you multiply yourself by ligthspeed then you energy.")
        else:
            await self.bot.say("¯\\_( ツ )_/¯ {0} just made {1} lose hope in humanity.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def tbag(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("Tell me who to humiliate!")
        elif size > 1:
            await self.bot.say("You only have one bag to tbag.")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("I can't picture a pose in wich this is possible.")
        else:
            await self.bot.say("( ﾟДﾟ)┌┛Σ( ﾟ∀ﾟ)･∵ {0}, the last thing you see before you die  is {1} tbag.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def angry(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("Tell me who pissed you off!")
        elif size > 1:
            await self.bot.say("It is better to direct anger at only one person at a time.")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("Keep it to yourself then.")
        else:
            await self.bot.say("( ╬ Ò ‸ Ó) {0} just made {1} angry.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def touch(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("Tell me who to touch!")
        elif size > 1:
            await self.bot.say("Direct your love to one person at a time.")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("Touch yourself in private!")
        else:
            await self.bot.say("( ͡° ͜ʖ ͡°) {0} was gently touched by {1}.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def lick(self, ctx):
        size = len(ctx.message.mentions)
        if size == 0:
            await self.bot.say("Tell me who to lick!")
        elif size > 1:
            await self.bot.say("You only have one tongue.")
        elif ctx.message.author in ctx.message.mentions:
            await self.bot.say("Stop licking yourself! It is unsanitary")
        else:
            await self.bot.say("(っˆڡˆς){0} was licked by {1}.".format(ctx.message.mentions[0].mention, ctx.message.author.mention))


def setup(bot):
    bot.add_cog(Interact(bot))
