from time import sleep as delay
import configparser
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext,Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton
from logs.logs import find_accounts,lts
config = configparser.RawConfigParser()
config.read('settings.ini')
TOKEN = input('Enter Token: ')

conusers = configparser.RawConfigParser()
conusers.read('users.ini')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


button_netflix = KeyboardButton('Аккаунты нетфликс 🎲')
button_search = KeyboardButton('Поиск по логам 🎲')
button_google = KeyboardButton('Аккаунты гугл 🎲')
logs_kb = ReplyKeyboardMarkup(resize_keyboard=True)
logs_kb.add(button_netflix,button_search,button_google)

button_go_admin = KeyboardButton('Админка 🔧')
logs_kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
logs_kb_admin.add(button_go_admin,button_netflix,button_search,button_google)

button_admin_add = KeyboardButton('Добавить админа ✅')
button_admin_exit = KeyboardButton('Выйти ❎')
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(button_admin_add,button_admin_exit)

def rate_limit(limit: int, key=None):
    def decorator(func):
        setattr(func, 'throttling_rate_limit', limit)
        if key:
            setattr(func, 'throttling_key', key)
        return func
    return decorator

class Id_Form(StatesGroup):
    user_id = State()
    rasilka = State()
    finder = State()

users = []
for x in conusers['user']:
    users.append(conusers['user'][x])

admins = []

for i in config['admins']:
    admins.append(config['admins'][i])

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    if str(message.chat.id) not in str(users):
        with open('users.ini', 'a') as conusr:
            conusr.write('user'+str(len(users)+1)+' = '+str(message.chat.id)+'\n')
        print(f'A user with id was added: {message.chat.id}')
    if str(message.chat.id) not in str(admins):
        await message.reply('Привет я бот который собрал очень много логов :)', reply_markup=logs_kb)
    if str(message.chat.id) in str(admins):
        await message.reply('Привет админ :)', reply_markup=logs_kb_admin)

@dp.message_handler(text='Админка 🔧')
async def admin_menu(message: types.Message):
    if str(message.chat.id) in str(admins):
        await message.answer('Ты в админке', reply_markup=kb_admin)
    if str(message.chat.id) not in str(admins):
        await message.reply('У вас нету доступа 🔒')



@dp.message_handler(text='Добавить админа ✅')
async def admin_add(message: types.Message,state: FSMContext):
    if str(message.chat.id)==str('1291658598') or str(message.chat.id)==str('1047311374'):
        await Id_Form.user_id.set()
        await message.reply('Введите айди админа (напишите "отмена" чтобы не отправлять рассылку)')

    else:
        await message.reply('У вас нету прав чтобы собирать логи 🔒')

@dp.message_handler(text='отмена', state='*')
async def stop(message: types.Message,state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('FSM отменен')

@dp.message_handler(state=Id_Form.user_id)
async def add_admin_finish(message: types.Message, state: FSMContext):
    global admins
    user_id = message.text
    if len(user_id)>11:
        await message.reply('Айди админа не может быть больше чем 11!')
    elif len(user_id)<10:
        await message.reply('Айди админа не может быть меньше чем 11!')
    else:
        with open('settings.ini', 'a') as confile:
            confile.write('admin'+str(len(admins)+1)+' = '+user_id+'\n')
        await state.finish()
        await message.reply('Админ добавлен!')
        for i in config['admins']:
            admins.append(config['admins'][i])


@dp.message_handler(text='Выйти ❎')
async def exit_admin_menu(message: types.Message):
    await message.reply('Вы вышли из админ меню', reply_markup=logs_kb_admin)

@dp.message_handler(text='Поиск по логам 🎲')
async def admin_add(message: types.Message,state: FSMContext):
    if str(message.chat.id) in str(admins):
        await Id_Form.finder.set()
        await message.reply('Введите то что хотите найти')
    else:
        await message.reply('У вас нету прав чтобы собирать логи 🔒')

done = False
accounts_finder = []
@dp.message_handler(state=Id_Form.finder)
async def logs_finder_finish(message: types.Message,state: FSMContext):
    global done
    global accounts_finder
    await Id_Form.finder.set()
    find_text = message.text
    if str(message.chat.id) not in str(admins):
        await message.reply('У вас нету прав чтобы собирать логи 🔒')
    if str(message.chat.id) in str(admins):
        if done==False:
            await message.answer('Начинаю собирать логи')
            accounts_finder.append(find_accounts(find_text))
            await message.reply('Готово!')
            delay(0.5)
            done=True
            await message.reply(accounts_finder[0:4096])
            await message.reply(accounts_finder[4096:8198])
            accounts_finder = []
        else:
            await message.reply(accounts_google[0][0:4096])
            await message.reply(accounts_google[0][4096:8198])
            accounts_finder = []

accounts_netflix = []
accounts_google = []
done_netflix = False
done_google = False
@dp.message_handler()
async def start_logs(message: types.Message):
    if message['text'] == 'Аккаунты гугл 🎲':
        global done_google
        global accounts_google
        if str(message.chat.id) not in str(admins):
            await message.reply('У вас нету прав чтобы собирать логи 🔒')
        if str(message.chat.id) in str(admins):
            if done_google==False:
                await message.answer('Начинаю собирать логи')
                accounts_google.append(find_accounts('google'))
                await message.reply('Готово!')
                delay(0.5)
                done_google=True
                await message.reply(accounts_google[0][0:4096])
                await message.reply(accounts_google[0][4096:8198])
            else:
                await message.reply(accounts_google[0][0:4096])
                await message.reply(accounts_google[0][4096:8198])
    if message['text'] == 'Аккаунты нетфликс 🎲':
        global done_netflix
        global accounts_netflix
        if str(message.chat.id) not in str(admins):
            await message.reply('У вас нету прав чтобы собирать логи 🔒')
        if str(message.chat.id) in str(admins):
            if done_netflix==False:
                await message.answer('Начинаю собирать логи')
                accounts_netflix.append(find_accounts('netflix'))
                await message.reply('Готово!')
                delay(0.5)
                done_netflix=True
                await message.reply(accounts_netflix[0][0:4096])
                await message.reply(accounts_netflix[0][4096:8198])
            else:
                await message.reply(accounts_netflix[0][0:4096])
                await message.reply(accounts_netflix[0][4096:8198])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
