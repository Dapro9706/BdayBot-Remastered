from discord import Embed, Colour
from os import environ
import psycopg2


async def embed(ctx, content):
    await ctx.send (embed=Embed (description=content))


async def birthday_embed(ctx, head, content, footer="xD"):
    await ctx.send (embed=Embed (title=":birthday: " + head + " :partying_face:", description=content,
                                 color=Colour.random ()).set_footer (
        text=f"btw its also {footer}'s birthday"))


DATABASE_URL = environ['DATABASE_URL']


def create_table():
    c = psycopg2.connect (DATABASE_URL, sslmode='require')  # sqlite3.connect(DATABASE)
    c.cursor ().execute ('''CREATE TABLE LastCheck
                      (ID INTEGER PRIMARY KEY,
                       LC TEXT)''')
    c.cursor ().execute (f"INSERT INTO LastCheck VALUES (1, 21)")
    c.commit ()
    c.close ()


def edit(a):
    c = psycopg2.connect (DATABASE_URL, sslmode='require')  # sqlite3.connect(DATABASE)
    c.cursor ().execute (f"UPDATE LastCheck SET AMOUNT = '{a}' WHERE ID = 1")
    c.commit ()
    c.close ()
