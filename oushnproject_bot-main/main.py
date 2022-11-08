import discord
from config import TOKEN
from utils import *
intents = discord.Intents.default()
bot = discord.Bot()

hostname1 = ugetdata(0,True)['HostName']
hostname2 = ugetdata(1,True)['HostName']
hostname3 = ugetdata(2,True)['HostName']

class PublicView(discord.ui.View):
    @discord.ui.select(
        placeholder = 'Выберите паблик!',
        min_values = 1,
        max_values = 1,
        options = [
            discord.SelectOption(
                label='Сервер 1',
                description=hostname1
            ),
            discord.SelectOption(
                label='Сервер 2',
                description=hostname2
            ),
            discord.SelectOption(
                label='Сервер 3',
                description=hostname3
            ),
        ]
    )
    async def select_callback(self, select, interaction: discord.Interaction):
        convert = {'Сервер 1': 0,'Сервер 2': 1,'Сервер 3': 2}
        await interaction.response.edit_message(content=str('\n'.join(ugetdata(int(convert[select.values[0]])))))

class PlayerView(discord.ui.View):
    options = []
    for i in range(0,2):
        data = getplayers(i)
        for i in data[1]:
            if i!='oushnproject':
                options.append(discord.SelectOption(label=i,description='Игрок'))
    @discord.ui.select(
        placeholder='Выберите игрока!',
        min_values=1,
        max_values=1,
        options = options[:-1]
    )
    async def select_callback(self,select,interaction: discord.Interaction):
        try:
            await interaction.response.edit_message(content=getplayers(0)[0][select.values[0]])
        except KeyError:
            try:
                await interaction.response.edit_message(content=getplayers(1)[0][select.values[0]])
            except KeyError:
                await interaction.response.edit_message(content=getplayers(2)[0][select.values[0]])
@bot.slash_command(description='Выводит информацию об паблике')
async def getdata(ctx):
    await ctx.respond(view=PublicView())

@bot.slash_command(description='Выводит информацию об игроке на паблике')
async def getplayer(ctx):
    await ctx.respond(view=PlayerView())

@bot.slash_command(description='Информация об боте')
async def about(ctx):
    await ctx.respond('''
Создатель бота: PLNT#6825 aka Purpl3_YT
Бот написан на: Python, pycord''')

@bot.event
async def on_ready():
    login_message = f'Logged to: {bot.user}'
    print(login_message)
    print('-'*len(login_message))

bot.run(TOKEN)