from discord.ext import commands
import os


class Bot (commands.Bot):
    def __init__(self, *args, **kwargs):
        super ().__init__ (*args, **kwargs)
        self.init_commands ()
        self.remove_command('help')
        self.load_extension ('cog')

    def init_commands(self):
        @self.event
        async def on_ready():
            print ('Bot Online')


bot = Bot (command_prefix="q")
bot.run (os.getenv ('TOKEN'))
