from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = input('Api token: ')

bot = Bot(token=API_TOKEN,)

dp = Dispatcher(bot,storage=MemoryStorage())
class Text_Form(StatesGroup):
    txt = State()
    format = State()

text_ = ''

@dp.message_handler(commands=['start', 'help'])
async def send_start(message: types.Message):
    await message.reply('Привет, это изменятель текста\nНапиши команду /text чтобы изменить текст')

@dp.message_handler(text='отмена', state='*')
async def stop(message: types.Message,state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('FSM отменен')


@dp.message_handler(commands=['text','txt'])
async def text_com(message: types.Message,state: FSMContext):
    await Text_Form.txt.set()
    await message.reply('Введите текст (напишите "отмена" чтобы отменить FSM)')


@dp.message_handler(state=Text_Form.txt)
async def text_com_finish(message: types.Message, state: FSMContext):
    global text_
    text = message.text
    text_ = message.text
    await message.reply(f'Ваш текст: `{text}`')
    await message.reply('Чтобы получить список что с ним можно сделать напишите команду /format')
    await state.finish()

@dp.message_handler(commands=['for','format'])
async def format_com(message: types.Message,state: FSMContext):
    await Text_Form.format.set()
    await message.reply('''Введите режим: 
1) Lower - делает весь текст маленькими буквами
2) Upper - делает весь текст большими буквами
''')

@dp.message_handler(state=Text_Form.format)
async def format_com_finish(message: types.Message,state: FSMContext):
    format_ = message.text
    if format_.lower() == 'lower':
        await message.reply(text_.lower())
    elif format_.lower() == 'upper':
        await message.reply(text_.upper())
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)