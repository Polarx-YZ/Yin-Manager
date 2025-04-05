import discord
from discord.ext import commands, tasks
from settings import config

class SystemMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_status = {"Yin": "online"}
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        
        welcomeID = config.get("welcomeChannel")
        
        channel = self.bot.get_channel(welcomeID)
        
        embed = discord.Embed(
            description=f"## Welcome {member.mention}!\n Enjoy your stay!",
        )
        
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        
        departureID = config.get("departureChannel")
        
        channel = self.bot.get_channel(departureID)
        
        embed = discord.Embed(
            description=f"### {member.mention} has left the server!"
        )
        
        await channel.send(embed=embed)
    
    # @commands.Cog.listener()
    # async def on_member_update(self, before, after):
    #     print("works")
    #     if str(after.status) == "online":
    #         print(f"{after.name} has gone {after.status}")
    
async def setup(bot):
    await bot.add_cog(SystemMessages(bot))