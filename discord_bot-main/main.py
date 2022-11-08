from time import sleep
from discord.ext import commands
from datetime import datetime
from youtubesearchpython import VideosSearch
from googlesearch import search
from config import TOKEN
import random
import discord
import youtube_dl
import asyncio
import requests
import gtts
#Настройки
bot = commands.Bot(case_insensitive=True,command_prefix='.',owner_id=556864778576986144,intents=discord.Intents.all())
now_bot = datetime.now()
bot_started_at = now_bot.strftime('%H:%M:%S, %m/%d/%Y')
youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
#Функции

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
class Music(commands.Cog):#Музыка
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def плейслово(self,ctx,*,text):
        if ctx.guild.id==860118087524679681:
            t1 = gtts.gTTS(f"{text}",lang='ru')
            t1.save("play_word.mp3")
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('play_word.mp3'))
            ctx.voice_client.play(source, after=lambda e: print(f'Ошибка: {e}') if e else None)
        elif ctx.guild.id!=886011808752467968160:
            await ctx.reply('Эту комманду можно выполнять только на Lumat Community!',mention_author=False)
    @commands.command()
    async def плей(self, ctx, url):
        if url[0:5]=='https' or url[0:4]=='http':
            async with ctx.typing():
                player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Ошибка: {e}') if e else None)
            await ctx.reply(f'Сейчас играет: {player.title}',mention_author=False)

        else:
            videosSearch = VideosSearch(url, limit=5)
            result = videosSearch.result()
            await ctx.reply('Выберете из 5 видео',mention_author=False)
            await ctx.reply(f'''
1)  {(result["result"][0]["title"])}
2) {(result["result"][1]["title"])}
3) {(result["result"][2]["title"])}
4) {(result["result"][3]["title"])}
5) {(result["result"][4]["title"])}''',mention_author=False)
            def check(m: discord.Message):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
            try:
                msg = await bot.wait_for(event='message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                await ctx.send("Время истекло! Введите комманду еще раз для повтора")
                return
            else:
                if msg.content=='1':
                    url = result["result"][0]["link"]
                elif msg.content=='2':
                    url = result["result"][1]["link"]
                elif msg.content=='3':
                    url = result["result"][2]["link"]
                elif msg.content=='4':
                    url = result["result"][3]["link"]
                elif msg.content=='5':
                    url = result["result"][4]["link"]
                player = await YTDLSource.from_url(f'{url}', loop=self.bot.loop, stream=True)
                ctx.voice_client.play(player, after=lambda e: print(f'Ошибка: {e}') if e else None)
                views_not = (result["result"][(int(msg.content) - 1)]["viewCount"]['short'])
                views = views_not.replace('views', 'просмотров')
                await ctx.reply(f'''
Сейчас играет: **{player.title}**
Длительность: **{(result["result"][(int(msg.content)-1)]["duration"])}**
Всего просмотров: **{views}**
    ''', mention_author=False)
                return
    @commands.command()
    async def громкость(self, ctx, volume: int):#меняет громкость
        if ctx.voice_client is None:
            return await ctx.reply('Бот не в музыкальном канале!',mention_author=False)
        elif volume>100:
            await ctx.reply('Вы не можете поставить громкость больше чем 100%',mention_author=False)
        elif volume<1:
            await ctx.reply('Вы не можете поставить громкость меньше чем 1%',mention_author=False)
        else:
            ctx.voice_client.source.volume = volume / 100
            await ctx.reply(f'Громкость поставлена на {volume}%',mention_author=False)
    @commands.command()
    async def стоп(self, ctx):
        await ctx.voice_client.stop()
    @commands.command()
    async def лив(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.reply('Отключение!',mention_author=False)
    @commands.command()
    async def пауза(self, ctx):
        await ctx.voice_client.pause()
    @commands.command()
    async def возоб(self, ctx):
        await ctx.voice_client.resume()
    @commands.command()
    async def подкл(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.reply('Подключение',mention_author=False)
    @commands.command()
    async def звук(self, ctx,*args):

        sound = ' '.join((x) for x in args)
        if not sound:
             await ctx.reply('''
Укажите звук:
1). пердежа (*.звук пердежа*) `звук мемного пука`
2). ядерного взрыва (*.звук ядерного взрыва*) `личное произведение искуства`
3). лива (*.звук лива*) `звук типо кто-то ливнул`
4). лива2 (*.звук лива2*) `звук тоже типо кто-то ливнул но реалистичнее`
5). буранье (*.звук буранье*) `звук мемного кота (NECO-ARC) который говорит *буранье*`
''',mention_author=False)
        elif sound=='пердежа':
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('./sounds/perdesh.mp3'))
            ctx.voice_client.play(source)
        elif sound=='ядерного взрыва':
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('./sounds/yadernyi_vzriv.mp3'))
            ctx.voice_client.play(source)

        elif sound=='лива':
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('./sounds/liv.mp3'))
            ctx.voice_client.play(source)

        elif sound=='лива2':
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('./sounds/liv2.mp3'))
            ctx.voice_client.play(source)

        elif sound=='буранье':
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('./sounds/buranyo.mp3'))
            ctx.voice_client.play(source)
        else:
            await ctx.reply('Такого звука нету!',mention_author=False)
    @плейслово.before_invoke
    @плей.before_invoke
    @звук.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.reply('Вы не подключены к музыкальному каналу.',mention_author=False)
                raise commands.CommandError('Автор не подключен к музыкальному каналу.')
        elif ctx.voice_client.is_playing():
            await ctx.reply('Вы не можете воспроизвести что-то другое когда уже что-то включено',mention_author=False)
def add(x, y):#математика
    return x + y
def subtract(x, y):#математика
    return x - y
def multiply(x, y):#математика
    return x * y
def divide(x, y):#математика
    return x / y
#Комманды
class Logic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def матем(ctx, *args):
        math = ' '.join((x) for x in args)
        if not args:
            await ctx.reply('Ошибка введите правильный пример (например .матем 2 + 2)',mention_author=False)
        elif math == '+':
            finish = add(int(args[0]),int(args[2]))
            await ctx.reply(finish,mention_author=False)
        elif math == '-':
            finish = subtract(int(args[0]), int(args[2]))
            await ctx.reply(finish,mention_author=False)
        elif math == '*':
            finish = multiply(int(args[0]), int(args[2]))
            await ctx.reply(finish,mention_author=False)
        elif math == '/':
            finish = divide(int(args[0]), int(args[2]))
            await ctx.reply(int(finish),mention_author=False)
#Действия
@bot.command()
async def ушатать(ctx, member):
    finish = str(ctx.message.author.mention)+(f' ушатал {member}')
    await ctx.reply(str(finish),mention_author=False)
@bot.command()
async def хелп(ctx):
    embed = discord.Embed(title='Все комманды тут', url='https://sites.google.com/view/lumatsite/help', color=0x630de3, timestamp=datetime.utcnow())
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/698068083360792576/911943881732542524/standard_1.gif')
    await ctx.reply(embed=embed,mention_author=False)
#Рандом
@bot.command()
async def монетка(ctx):
    orel_reshka = random.randint(1,2)
    if int(orel_reshka)==1:
        await ctx.reply('Орел',mention_author=False)
    elif int(orel_reshka)==2:
        await ctx.reply('Решка',mention_author=False)
@bot.command()
async def карта(ctx, arg):
    if not arg:
        await ctx.reply('''
Введите ```.карта открыть``` - чтобы открыть карту
Введите ```.карта список``` - чтобы посмотреть список карт
        ''')
    if arg=='открыть':
        cards = [
        'https://cdn.discordapp.com/attachments/1018810396964044810/1037121298003931247/Picsart_22-11-01_23-30-41-537.png',
        'https://cdn.discordapp.com/attachments/1018810396964044810/1037121298394009601/Picsart_22-11-01_23-35-07-524.png',
        'https://cdn.discordapp.com/attachments/1018810396964044810/1037121298784059492/Picsart_22-11-01_23-28-47-454.png',
        'https://cdn.discordapp.com/attachments/1018810396964044810/1037121299161559060/Picsart_22-11-01_23-40-41-186.png',
        'https://cdn.discordapp.com/attachments/1018810396964044810/1037121299551637604/Picsart_22-11-01_23-26-15-851.png',
        'https://cdn.discordapp.com/attachments/1018810396964044810/1037121299929104444/Picsart_22-11-01_23-38-50-137.png',
        'https://cdn.discordapp.com/attachments/1018810396964044810/1037121300323381268/Picsart_22-11-01_23-41-52-279.png',
        ]
        await ctx.reply(random.choice(cards),mention_author=False)
    elif arg=='список':
        await ctx.reply('''
Пустота - 0
Комп с помойки - 200
Золотой ноут - 1777
Белый комп - 2000
Черный комп - 2500
        ''',mention_author=False)

@bot.command()
async def рандом(ctx, *args: int):
    if not args:
         await ctx.reply('Укажите число от и до (например .рандом [0] [10000])',mention_author=False)
    elif args[1]>10000:
        await ctx.reply('Нельзя сгенерировать число больше 10000 (иначе нагружает бота)',mention_author=False)
    else:
        ran_num1 = random.randint(args[0],args[1])
        await ctx.reply(f'Рандомное число {ran_num1}',mention_author=False)
@bot.command()
async def стрелка(ctx, member):
    finish = str(ctx.message.author.mention)+(' кинул стрелку {}').format(member)
    await ctx.reply(str(finish),mention_author=False)
#Инфо
@bot.command()
async def инфо(ctx, member: discord.Member):

    await ctx.reply(f'''
Никнейм: {member.name}
Статус-Сети: {member.status}
Цвет профиля: {member.colour}
Статус-профиля: {member.activity}
Дата создания профиля: {member.created_at}
Айди: {member.id}
Лучшая роль: {member.top_role}
Сервер: {member.guild}''',mention_author=False)
#События
@bot.command()
async def сcылкабота(ctx):
    print('info commands run!')
    await ctx.reply('**Вот сыллка на бота ---->** ||https://bit.ly/3kWiYYH||',mention_author=False)
@bot.command()
async def приглашение(ctx):
    await ctx.reply('**Вот сыллка на Lumat Community** ||https://bit.ly/312UV3E||')
@bot.command()
async def скажи(ctx,*args):
    if len(args[0])>50:
        await ctx.reply('Бот не может сказать больше чем 100 символов!',mention_author=False)
    else:
        str = ' '.join((x) for x in args)
        await ctx.reply(f'{str}',mention_author=False)
@bot.command()
async def бот_запуск(ctx):
    await ctx.reply(f'Бот запущен с: {bot_started_at}',mention_author=False)
@bot.command()
@commands.has_permissions(administrator=True)
async def модер(ctx,*args):
    help_moder = '''
**Все комманды**
Что означает:
[]=означает что надо ввести
()=означает что делает комманда
*.модер хелп (выводит все комманды)
.модер имя [новое имя сервера] (меняет имя сервера)
.модер вериф (меняет уровень верификации)
.бан [@Участник,Причина] (банит пользователя на сервере)
.кик [@Участник, Причина] *
'''
    if not args:
        await ctx.reply(f'''{help_moder}''', mention_author=False)
    elif args[0]=='хелп':
        await ctx.reply(f'''{help_moder}''',mention_author=False)
    elif args[0]=='имя':
        str = ' '.join((x) for x in args[1:])
        await ctx.guild.edit(name=f'{str}')
    elif args[0]=='вериф':
        await ctx.reply('''
**Введите уровень верификации**
1). Никакой (*Без ограничений. На сервер смогут приходить кто угодно и когда угодно*)
2). Низкий (*Участнику необходимо иметь подтверждённый e-mail*)
3). Средний (*Участник так же должен быть зарегистрирован в Discord более 5 минут*)
4). Высокий (*Участник должен быть участником этого сервера более 10 минут.*)
5). **УЛЬТРА ХАРД** (*Участник должен иметь подтверждённый телефон в учётной записи Discord. Включая все верхние пункты,*)
    ''',mention_author=False)
        def check(m: discord.Message):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        try:
            msg = await bot.wait_for(event='message', check=check, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send("Время истекло! Введите комманду еще раз для повтора")
            return
        else:
            if msg.content=='1':
                discord.VerificationLevel.none
            if msg.content=='2':
                discord.VerificationLevel.low
            if msg.content=='3':
                discord.VerificationLevel.medium
            if msg.content=='4':
                discord.VerificationLevel.high
            if msg.content=='5':
                discord.VerificationLevel.extreme
            return
@bot.command()
@commands.has_permissions(administrator=True)
async def бан(ctx,member: discord.User, reason):
        await ctx.reply(f'Вы уверены да или нет? Будет забанен участник {member}, по причине {reason}',mention_author=False)
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
                   msg.content.lower() in ["да", "нет"]
        msg = await bot.wait_for("message", check=check)
        if msg.content.lower() == "да":
            await ctx.guild.ban(member, reason=reason, delete_message_days=1)
            await ctx.reply(f'''**Был забанен участник!**
Кто был забанен: {member}
Причина: {reason}
''',mention_author=False)
        else:
            await ctx.reply("Не банить!",mention_author=False)
@bot.command()
@commands.has_permissions(administrator=True)
async def кик(ctx,member: discord.User, reason):
        await ctx.reply(f'Вы уверены (да) или (нет)? Будет кикнут участник {member}, по причине {reason}',mention_author=False)
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
                   msg.content.lower() in ['да', 'нет']
        msg = await bot.wait_for("message", check=check)
        if msg.content.lower() == "да":
            await ctx.guild.kick(member, reason=reason)
            await ctx.reply(f'''**Был кикнут участник!**
Кто был кикнут: {member}
Причина: {reason}
''',mention_author=False)
        else:
            await ctx.reply("Не кикать!",mention_author=False)
@bot.command()
async def поисквид(ctx,*args):
    search_text = ' '.join((x) for x in args[0:])
    videosSearch = VideosSearch(f'{search_text}', limit=5)
    result = videosSearch.result()
    await ctx.reply(f'''
**Найдено 5 видео**
Чтобы узнать информацию то напишите цифру (например 4)
1) *{(result["result"][0]["title"])}*
2) *{(result["result"][1]["title"])}*
3) *{(result["result"][2]["title"])}*
4) *{(result["result"][3]["title"])}*
5) *{(result["result"][4]["title"])}*
''',mention_author=False)
    def check(m: discord.Message):
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
    try:
        msg = await bot.wait_for(event='message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send("Время истекло! Введите комманду еще раз для повтора")
        return
    else:
        views_not = str(result["result"][0]["viewCount"]['short'])
        views = views_not.replace('views','просмотров')
        search_text_fin = f'''
**Все данные видео**
Название: *{(result["result"][(int(msg.content)-1)]["title"])}*
Тип: *{(result["result"][(int(msg.content)-1)]["type"])}*
Длительность: *{(result["result"][(int(msg.content)-1)]["duration"])}*
Айди: *{(result["result"][(int(msg.content)-1)]["id"])}*
Дата опубликования: *{(result["result"][(int(msg.content)-1)]["publishedTime"])}*
Просмотры: *{views}*
Сыллка на видео: *{(result["result"]['link'])}*'''
        if msg.content == '1':
            views_not = str(result["result"][0]["viewCount"]['short'])
            views = views_not.replace('views', 'просмотров')
            await ctx.send(f'''
{search_text_fin}''')
        if msg.content == '2':
            views_not = str(result["result"][1]["viewCount"]['short'])
            views = views_not.replace('views', 'просмотров')
            await ctx.send(f'''
{search_text_fin}''')
        if msg.content == '3':
            views_not = str(result["result"][2]["viewCount"]['short'])
            views = views_not.replace('views', 'просмотров')
            await ctx.send(f'''
{search_text_fin}''')
        if msg.content == '4':
            views_not = str(result["result"][3]["viewCount"]['short'])
            views = views_not.replace('views', 'просмотров')
            await ctx.send(f'''
{search_text_fin}''')
        if msg.content == '5':
            views_not = str(result["result"][4]["viewCount"]['short'])
            views = views_not.replace('views', 'просмотров')
            await ctx.send(f'''
{search_text_fin}''')
@bot.command()
async def кот(ctx):
    r = requests.get('https://aws.random.cat/meow')
    cat = r.json()['file']
    await ctx.reply(f'{cat}' ,mention_author=False)
@bot.command()
async def собака(ctx):
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    dog = r.json()['message']
    await ctx.reply(f'{dog}', mention_author=False)
@bot.command()
async def ковид(ctx):
    r = requests.get('https://corona-api.com/countries')
    await ctx.reply(f'''
**Информация по крупным странам!**
:flag_ua:**Украина**:flag_ua:
Код: {r.json()['data'][177]['code']}
Заболело: {r.json()['data'][177]['latest_data']['confirmed']}
Выздоровело: {r.json()['data'][177]['latest_data']['recovered']}
Смертей: {r.json()['data'][177]['latest_data']['deaths']}
:flag_kz:**Казахстан**:flag_kz:
Код: {r.json()['data'][189]['code']}
Заболело: {r.json()['data'][189]['latest_data']['confirmed']}
Выздоровело: {r.json()['data'][189]['latest_data']['recovered']}
Смертей: {r.json()['data'][189]['latest_data']['deaths']}
:flag_by:**Беларусь**:flag_by:
Код: {r.json()['data'][24]['code']}
Заболело: {r.json()['data'][24]['latest_data']['confirmed']}
Выздоровело: {r.json()['data'][24]['latest_data']['recovered']}
Смертей: {r.json()['data'][24]['latest_data']['deaths']}
''',mention_author=False)
@bot.command()
async def текст(ctx, *args):
    text = ' '.join((x) for x in args[0:])
    if not args:
        await ctx.reply('Укажите текст (например .текст привет)',mention_author=False)
    await ctx.reply('''
Какой текст надо сделать?
1) **Жирный**
2) *Кривой*
3)  __С линией__
4) `Код`
5) Спойлер
''',)
    def check(m: discord.Message):
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

    try:
        msg = await bot.wait_for(event='message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send("Время истекло! Введите комманду еще раз для повтора")
        return
    else:
        if msg.content=='1':
            await ctx.reply(f'**{text}**',mention_author=False)
        elif msg.content=='2':
            await ctx.reply(f'*{text}*',mention_author=False)
        elif msg.content=='3':
            await ctx.reply(f'__{text}__', mention_author=False)
        elif msg.content=='4':
            await ctx.reply(f'`{text}`', mention_author=False)
        elif msg.content=='5':
            await ctx.reply(f'||{text}||', mention_author=False)
@bot.command()
async def поиск(ctx,*args):
    search_text = ' '.join((x) for x in args[0:])
    results = []
    for i in search(search_text, num=5, stop=5, pause=2):
        results.append(i)
    await ctx.reply(f'''
Найдено 5 ссылок
1) ***{results[0]}***
2) ***{results[1]}***
3) ***{results[2]}***
4) ***{results[3]}***
5) ***{results[4]}***
''',mention_author=False)

@bot.command()
async def картастраны(ctx):
    await ctx.reply('''
Какую показать карту страны?
1) **Украина**
2) **Польша**
3) **Европа**
''',)
    def check(m: discord.Message):
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

    try:
        msg = await bot.wait_for(event='message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send("Время истекло! Введите комманду еще раз для повтора")
        return
    else:
        if msg.content=='1':
            await ctx.reply(f'https://cdn.discordapp.com/attachments/698068083360792576/1003304795907575818/political-and-administrative-map-of-ukraine.png',mention_author=False)
        elif msg.content=='2':
            await ctx.reply(f'http://www.maps-of-europe.com/maps/maps-of-poland/detailed-political-and-administrative-map-of-poland-with-all-cities-roads-and-airports.jpg',mention_author=False)
        elif msg.content=='3':
            await ctx.reply(f'http://www.maps-of-europe.com/maps/political-map-of-europe.jpg', mention_author=False)   
class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):# меняет статус бота
            twitch_url = 'https://twitch.tv/rawitti'
            await bot.change_presence(activity=discord.Streaming(name='Lumat Bot (Для помощи напишите .хелп)', url=twitch_url))
            print('Bot started')
    @commands.Cog.listener()
    async def on_message(self,message):
            msg_cnt = message.content.lower()
            if "discord.gg" in msg_cnt:
                await message.delete()

bot.add_cog(Events(bot))
bot.add_cog(Music(bot))
bot.add_cog(Logic(bot))
bot.run(TOKEN)#запуск бота  