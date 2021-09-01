import json
from discord.ext import commands, tasks
from .utils import embed, birthday_embed, Colour, edit, create_table
from datetime import datetime, timedelta
from .globals import *
from random import choice

if DEBUG:
    edit(1)

def save(j):
    pass

#     with open (SAVE, 'w') as f:
#         json.dump (j, f, indent=4 if DEBUG else None)


class BirthdayModule (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open (SAVE, 'r') as f:
            self.json = dict (json.load (f))

        with open (WISHES, 'r') as f:
            self.wishes = dict (json.load (f))

        self.birthday_loop.start ()

    @commands.command (name="ping", hidden=True)
    async def ping(self, ctx):
        await ctx.send ('TEST')

    #     @commands.command (name="setup")
    #     async def setup(self, ctx: commands.Context, msg_link: str):
    #         self.json['account'][ctx.guild.id] = {'data': msg_link, 'channel': ctx.channel.id}
    #         await ctx.channel.purge (limit=1)
    #         await ctx.guild.create_role (name="bday", color=Colour (0xFFFF00))
    #         await embed (ctx, 'Data saved')
    #         save (self.json)
    @commands.command (name="setup")
    async def setup(self, ctx: commands.Context):
        await ctx.channel.purge (limit=1)
        await ctx.guild.create_role (name="bday", color=Colour (0xFFFF00))
        await embed (ctx, 'Role created')

    @tasks.loop (minutes=1)
    async def birthday_loop(self):
        if DEBUG:
            print ('loop')
        now = (datetime.now ()+timedelta(hours=5,minutes=30)).strftime ('%j')
        if DEBUG:
            print(datetime.now (),datetime.now ()+timedelta(hours=5,minutes=30))
        if now != self.json['lastCheck']:
            if not DEBUG:
                self.json['lastCheck'] = now
                edit (self.json['lastCheck'])
            now = datetime.now ().strftime ('%b %d')

            for i in self.json['account']:
                current = self.json['account'][i]['data'].split ('/')[-2:]
                c_id = current[0]
                m_id = current[1]

                current = (await (await self.bot.fetch_channel (c_id)).fetch_message (m_id)).content.replace (
                    "```", '').replace ('py', '').split ('\n')[1:-1]
                for j in current:
                    if " ".join (j.split (' ')[:-1]) == now:
                        name = j.split (' ')[-1]
                        channel = await self.bot.fetch_channel (self.json['account'][i]['channel'])
                        await channel.send ('@bday')
                        await birthday_embed \
                            (channel, name, choice (self.wishes['wishes']), footer=self.wishes['dates'][now])

    @birthday_loop.before_loop
    async def before_loop(self):
        await self.bot.wait_until_ready ()
        print ('Task ready')
