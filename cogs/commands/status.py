import discord
from discord.ext import commands
from settings import config

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    async def status(self, ctx):
        guild = self.bot.get_guild(config.get("support_server_ID"))
        member = guild.get_member(1356002572913217696)
        title = ""
        status = ""
        if member.status == discord.Status.online:
            title = "🟢 | Status of Yin"
            status = "The bot is online!"
        elif member.status == discord.Status.offline:
            title = "🔴 | Status of Yin"
            status = "The bot is offline!"
        
        embed = discord.Embed(
            title=title,
            description=str(status)
        )
        await ctx.reply(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Status(bot))