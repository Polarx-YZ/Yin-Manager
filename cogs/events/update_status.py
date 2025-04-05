import discord
from discord.ext import commands, tasks
from settings import config

class UpdateStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_status = {"Yin": discord.Status.online}
        
    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.bot.get_guild(config.get("support_server_ID"))
        member = guild.get_member(1356002572913217696)
        self.bot_status["Yin"] = member.status
        self.check_bot_status.start()
        
    
    @tasks.loop(seconds=2)
    async def check_bot_status(self):
        try:
            guild = self.bot.get_guild(config.get("support_server_ID"))
            member = guild.get_member(1356002572913217696)
            prev_status = self.bot_status.get("Yin")
            
            if prev_status != member.status:
                if member.status == discord.Status.online or member.status == discord.Status.idle or member.status == discord.Status.dnd:
                    self.bot_status["Yin"] = discord.Status.online
                elif member.status == discord.Status.offline:
                    self.bot_status["Yin"] = discord.Status.offline
                    
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
                await guild.get_channel(1357863908668346542).send(content="<@&1356024937365770370>", embed=embed)

        except Exception as e:
            print(e)
    
    # @commands.Cog.listener()
    # async def on_member_update(self, before, after):
    #     print("works")
    #     if str(after.status) == "online":
    #         print(f"{after.name} has gone {after.status}")
    
async def setup(bot):
    await bot.add_cog(UpdateStatus(bot))