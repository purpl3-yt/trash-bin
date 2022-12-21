from config import *
from pyrogram import Client,filters,idle
from pyrogram.errors import *
from resources import *
import random
import asyncio
import datetime

app = Client('my_account',api_id=api_id, api_hash=api_hash)

stop = False

async def sleep(time: float):
    await asyncio.sleep(time)

@app.on_message(filters.command('arc', prefixes='.') & filters.me)
async def arc(_, msg):
    stop=False
    await msg.edit(f'Spam Started at {datetime.datetime.now().strftime("%H:%M")}!')
    while True:
        for chat in chats:
            for i in range(20):
                if stop:
                    break
                try:
                    rgroup = await app.get_chat(chat)
                    print('Spam to group: '+rgroup.title)
                except exceptions.not_acceptable_406.ChannelPrivate:
                    pass
                except exceptions.flood_420.FloodWait:
                    await asyncio.wait(1)
                    print('Wait 1 sec')
                except KeyError:
                    pass
                try:
                    await msg.edit('Spam to group: '+rgroup.title)
                except exceptions.bad_request_400.MessageNotModified:
                    continue
                try:
                    await app.send_message(rgroup.id,random.choice(message))
                except exceptions.forbidden_403.ChatWriteForbidden as e:
                    try:
                        await app.join_chat(rgroup.id)
                        print('Join group: '+rgroup.title)
                        #print('Archive group: '+rgroup.title)
                        #await app.archive_chats(rgroup.id)
                    except exceptions.flood_420.FloodWait:
                        pass
                except exceptions.flood_420.SlowmodeWait:
                    pass
                except exceptions.flood_420.FloodWait:
                    await asyncio.sleep(1)
                    print('Wait 1 sec')
            
@app.on_message(filters.command('stop',prefixes='.') & filters.me)
async def stop_com(_,msg):
    await msg.edit('Stop spam')
    stop=True
    await sleep(1)

@app.on_message(filters.command('leave',prefixes='.') & filters.me)
async def leave(_,msg):
    for i in chats:
        try:
            rgroup = await app.get_chat(i)
            await msg.edit('Leave from group: '+rgroup.title)
            await app.leave_chat(rgroup.id)
        except exceptions.bad_request_400.UserNotParticipant:
            pass
        except exceptions.not_acceptable_406.ChannelPrivate:
            pass
        except KeyError:
            pass
    await msg.delete()

@app.on_message(filters.command('join',prefixes='.') & filters.me)
async def join(_,msg):
    for i in chats:
        try:
            rgroup = await app.get_chat(i)
            await msg.edit('Join into group: '+rgroup.title)
            await app.join_chat(rgroup.id)
        except exceptions.not_acceptable_406.ChannelPrivate:
            pass
        except KeyError:
            pass
    await msg.delete()

@app.on_message(filters.command('help',prefixes='.') & filters.me)
async def help(_,msg):
    await msg.edit('''<code>
All commands:
.arc - Start spam in russian chats
.stop - Stop spam
.leave - Leave from all russian groups
.help - Shows that message
.update - Update resources.py file (not work)
.list - Get chat list
.messages - Get list of messages
.exit - Quit from this app</code>''')

@app.on_message(filters.command('exit',prefixes='.') & filters.me)
async def exit(_,msg):
    await msg.edit('Bye-Bye!')
    quit()

@app.on_message(filters.command('list',prefixes='.') & filters.me)
async def list(_,msg):
    await msg.edit('t.me/'+chats[0]+'\nt.me/'.join(chats[1:]))

@app.on_message(filters.command('messages',prefixes='.') & filters.me)
async def messages(_,msg):
    await msg.edit('\n'.join(message))

@app.on_message(filters.command('update',prefixes='.') & filters.me)
async def update(_,msg):
    exec(open('./resources.py','r',errors='ignore').read())

async def main():
    print('\n\nARC - Anti Russian Chats\nMade by Purpl3, Discord: PLNT#6825\n')
    await app.start()
    await app.send_message('me',f'''
<code>Hello! Thank you for using ARC
Type: ".arc" to start!
To help type: ".help"
Chats count: {str(len(chats))}</code>
**By Purpl3!**''')
    await idle()

app.run(main())