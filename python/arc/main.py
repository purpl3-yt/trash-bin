from config import *
from pyrogram import Client,filters,idle
from pyrogram.errors import *
from resources import *
import random

app = Client('my_account',api_id=api_id, api_hash=api_hash)


stop = False

@app.on_message(filters.command('arc', prefixes='.') & filters.me)
async def acs(_, msg):
    stop=False
    await msg.edit('Spam Started!')
    while True:
        for i in chats:
            if stop:
                break
            try:
                rgroup = await app.get_chat(i)
            except exceptions.not_acceptable_406.ChannelPrivate:
                pass
            print('Spam to group: '+rgroup.title)
            try:
                await msg.edit('Spam to group: '+rgroup.title)
            except exceptions.bad_request_400.MessageNotModified:
                continue
            for i in range(20):
                try:
                    await app.send_message(rgroup.id,random.choice(message))
                except exceptions.forbidden_403.ChatWriteForbidden:
                    await app.join_chat(rgroup.id)
                except exceptions.flood_420.SlowmodeWait:
                    pass
            
@app.on_message(filters.command('stop',prefixes='.') & filters.me)
async def stop_com(_,msg):
    await msg.edit('Stop spam')
    stop=True

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


@app.on_message(filters.command('help',prefixes='.') & filters.me)
async def help(_,msg):
    await msg.edit('''<code>
All commands:
.arc - Start spam in russian chats
.stop - Stop spam
.leave - Leave from all russian groups
.help - Shows that message
.exit - Quit from this app</code>''')

@app.on_message(filters.command('exit',prefixes='.') & filters.me)
async def exit(_,msg):
    await msg.edit('Bye-Bye!')
    quit()


async def main():
    print('\n\nARC - Anti Russian Chats\nMade by Purpl3\n')
    await app.start()
    await app.send_message('me','<code>Hello! Thank you for using ACS\nType: ".arc" to start!\nTo help type: ".help"</code>\n**By Purpl3!**')
    await idle()

app.run(main())