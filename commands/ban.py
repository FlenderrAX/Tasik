import discord
from discord.ext import commands
import datetime


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='ban', description='Ban a user.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason: str = None):
        await member.ban(reason=reason)
        ban_embed = discord.Embed(
            title="ban",
            description=f"**Offender:** {member.name} {member.mention}\n**Banned by:** {ctx.author.mention}\n{f'**Reason:** {reason}' if reason else ''}",
            colour=discord.Colour.red()
        )
        ban_embed.timestamp = datetime.datetime.utcnow()
        ban_embed.set_footer(text=f"ID : {member.id}")
        await ctx.respond(embed=ban_embed)


def setup(bot):
    bot.add_cog(Ban(bot))
