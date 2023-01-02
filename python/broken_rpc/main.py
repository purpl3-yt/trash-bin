from pypresence import Presence
import time
import random
import os,sys
client_id = '1049327004836708373'
RPC = Presence(client_id=client_id)
RPC.connect()#Connect to Discord

os.chdir(sys.path[0])

print('Connected to Discord\nBrokenRPC by Purpl3')

words = None#This line to fix ide warnings
exec(open('main_data.py','r').read())#Open file main_data and get list of words

count = 0

#small_images = ['discord_logo','123123']

small_images = ['123123']


smallimage = random.choice(small_images)

while True:
    
    start_time = time.time()-random.randint(1,3600)*random.randint(1,23)#Random start time, min = 1 max = 24
    
    time.sleep(2)

    RPC.update(large_image='glitch', large_text='What am I doing?',small_image=smallimage,small_text=random.choice(words), start=start_time,state=random.choice(words))
    
    if count>=3:#Every 3 seconds
        exec(open('main_data.py','r').read())#Refresh list of words
        smallimage = random.choice(small_images)#Random small image
        count = 0#Reset count

    count+=1
