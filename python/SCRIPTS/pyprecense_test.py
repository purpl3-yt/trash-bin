from pypresence import Presence
import time

client_id = '961706398884954122'  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()
start_time=time.time()

RPC.update(
state='D3adC0re',
details='https://www.deadrp.pp.ua',
large_image='deadcore_best',
large_text='DEAD CORE',
small_text='Rawitti Purpl3',
small_image='purpl3_rawitti',
buttons=[
{'label': 'Website', 'url': 'https://purpl3-yt.github.io/deadcoresite/'},
{'label': 'Server', 'url': 'https://discord.gg/A4QQA9RgGs'}])

while True:
    time.sleep(999)#RPC is static that's why wait 999 seconds)