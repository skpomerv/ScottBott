import subprocess
from discord.ext import commands
from discord.ext.commands import Bot

class OSCommands(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(brief='Generates a random fortune!', description='Generates a random fortune using the linux command "fortune" and posts it for all to see.')
    async def fortune(self, ctx):
        proc = subprocess.Popen(["/usr/games/fortune"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        await ctx.send("```" + out.decode('utf-8') + "```")


if __name__=="__main__":

    out = get_fortune()
    print(out)
