from discord import Embed, Colour


async def embed(ctx, content):
    await ctx.send (embed=Embed (description=content))


async def birthday_embed(ctx, head, content, footer="xD"):
    await ctx.send (embed=Embed (title=":birthday: "+head+" :partying_face:", description=content, color=Colour.random ()).set_footer (
        text=f"btw its also {footer}'s birthday"))
