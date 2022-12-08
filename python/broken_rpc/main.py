from pypresence import Presence
import time
import random
import os,sys
client_id = '1049327004836708373'
RPC = Presence(client_id=client_id)
RPC.connect()

os.chdir(sys.path[0])

print('Connected to Discord\nBrokenRPC by Purpl3')

words = None
exec(open('main_data.py','r').read())

count = 0

small_images = ['discord_logo','123123']

smallimage = random.choice(small_images)

while True:
    
    start_time = time.time()-random.randint(1,3600)*random.randint(1,23)
    
    time.sleep(2)

    RPC.update(large_image='glitch', large_text='What am I doing?',small_image=smallimage,small_text=random.choice(words), start=start_time,state=random.choice(words))
    
    if count>=3:#every 3 seconds
        exec(open('main_data.py','r').read())
        smallimage = random.choice(small_images)
        count = 0

    count+=1