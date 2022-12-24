from pyrogram import *
import utils
import config

bot = Client('bot',
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.API_TOKEN)

@bot.on_message(filters.command('start'))
async def welcome(_, msg):
    await msg.reply('Hello World')

actions = [
    utils.as_code('lang'),
    utils.as_code('ide'),
    utils.as_code('site'),
]

@bot.on_message(filters.command('random'))
async def random_cmd(_,msg):
    try:what = str(msg.text).split(' ')[1]
    except:await msg.reply('Введите что вывести: '+', '.join(actions))
    else:
        
        action = what.lower()

        if action=='lang':
            await utils.random_lang(bot,msg)
        
        elif action=='ide':
            await utils.random_ide(bot,msg)

        elif action=='site':
            await utils.random_site(bot,msg)

        else:
            await msg.reply('Такого нету!')

print('\nRun bot!\n')
bot.run()