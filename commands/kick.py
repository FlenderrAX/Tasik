import datetime

import discord
from discord.ext import commands
import datetime


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="kick", description="Kick a user.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason: str = None):
        await member.kick(reason=reason)
        kick_embed = discord.Embed(
            title="kick",
            description=f"**Offender:** {member.name} {member.mention}\n**Kicked by:** {ctx.author.mention}\n{f'**Reason:** {reason}' if reason else ''}",
            colour=discord.Colour.red()
        )
        kick_embed.timestamp = datetime.datetime.utcnow()
        kick_embed.set_footer(text=f"ID : {member.id}")
        await ctx.respond(embed=kick_embed)


def setup(bot):
    bot.add_cog(Kick(bot))
