import discord
from discord.ext import commands


class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="stats", description="Shows statistics about the server.")
    async def stats(self, ctx):
        member_count = ctx.guild.member_count
        online_member_count = 0

        for member in ctx.guild.members:
            if member.status is not discord.Status.offline:
                online_member_count += 1

        creation_date = ctx.guild.created_at
        timestamp = int(creation_date.timestamp())
        boosts_count = ctx.guild.premium_subscription_count
        boost_level = ctx.guild.premium_tier

        embed = discord.Embed(
            title=f"{ctx.guild.name}'s Stats",
        )

        embed.add_field(name=":bust_in_silhouette: | All Members",
                        value=f"{member_count}",
                        inline=False)

        embed.add_field(name=":green_circle: | Online Members",
                        value=f"{online_member_count}",
                        inline=False)

        embed.add_field(name=":clock3: | Creation Date",
                        value=f"<t:{timestamp}>",
                        inline=False)

        embed.add_field(name=":rocket: | Boosts",
                        value=f"{boosts_count} Boost{'s' if boosts_count > 1 else ''}",
                        inline=False)

        embed.add_field(name=":chart_with_upwards_trend: | Boost Level",
                        value=f"Level {boost_level}",
                        inline=False)

        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Stats(bot))
