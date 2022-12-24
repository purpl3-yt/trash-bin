import random
import resources

def as_code(text):
    return '<code>'+text+'</code>'

async def random_lang(bot,msg):
    await bot.send_message(msg.chat.id,'Рандомный язык: '+as_code(str(random.choice(resources.languages))))

async def random_ide(bot,msg):
    await bot.send_message(msg.chat.id,'Рандомный ide: '+as_code(str(random.choice(resources.ides))))

async def random_site(bot,msg):
    await bot.send_message(msg.chat.id,'Рандомный сайт: '+as_code(str(random.choice(resources.sites))))