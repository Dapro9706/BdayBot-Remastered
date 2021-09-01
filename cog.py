import BdayCog
import HelpCog


def setup(bot):
    bot.add_cog (BdayCog.BirthdayModule (bot))
    bot.add_cog (HelpCog.Help (bot))
