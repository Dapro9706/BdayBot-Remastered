import discord
from discord.ext import commands
from discord.errors import Forbidden


async def send_embed(ctx, embed):
    try:
        await ctx.send (embed=embed)
    except Forbidden:
        try:
            await ctx.send ("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send (
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Help (commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command ()
    # @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx):
        """Shows all modules of that bot"""

        prefix = 'r!'
        version = 'v1.7'

        # setting owner name - if you don't wanna be mentioned remove line 49-60 and adjust help text (line 88)
        owner = 727790616003739668

        try:
            owner = ctx.guild.get_member (owner).mention

        except AttributeError:
            owner = self.bot.get_user (owner)

        # starting to build embed
        emb = discord.Embed (title='Commands and modules', color=discord.Color.blue (),
                             description=f"Prefix: `{prefix}\n\n"
                                         f"Listen customisation isn't done yet so `{prefix}setup` "
                                         f"just makes a new role")

        # setting information about author
        emb.add_field (name="About", value=f"This bot was developed by {owner}")
        emb.set_footer (text=f"Bot is running {version}")

        # sending reply embed using our own function defined above
        await send_embed (ctx, emb)
