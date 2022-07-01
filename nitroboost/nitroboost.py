import discord
from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        print(message.type)
        if message.type == discord.MessageType.premium_guild_subscription:
            tit="ㅤㅤㅤㅤ` F ` ` R ` ` E ` ` E ` ` Z ` ` E ` ` ! `"
            des="ㅤㅤ❝**Look there! Is that a new tagger for freeze tag?**❞\nㅤㅤㅤㅤ❝ **Players __MUST__ freeze when tagged!**❞\n❝**Run, even if you're on ice, let it go and run for your life!**❞\nㅤㅤ❝**SHOOT, you caught me! Here's your award..**❞\nㅤ `congrats!` __all perks are listed in the pinned messages__\nㅤ\⛸️ Message <@950936706914344960> to claim tagger perks!"
            embed = discord.Embed(title=tit, description=des, color=0x2f3136)
            embed.set_thumbnail(url="https://i.pinimg.com/736x/4c/67/2f/4c672f707cead8e5109893cf236a37e8.jpg")
            m = await message.channel.send(embed=embed)
            await m.add_reaction("<a:Heartanimated:707510241276985425>")
            
def setup(bot):
    bot.add_cog(BoostPlugin(bot))
