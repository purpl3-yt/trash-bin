from pypresence import Presence
import time
import random
client_id = "1049327004836708373"
RPC = Presence(client_id=client_id)
RPC.connect()

print('Connected to Discord')

words = None
exec(open('main_data.py','r').read())

count = 0

while True:
    
    start_time = time.time()-random.randint(1,3600)*random.randint(1,23)
    
    time.sleep(2)

    RPC.update(large_image="glitch", large_text="What am I doing?",small_image='123123',small_text=random.choice(words), start=start_time,state=random.choice(words)) # We want to apply start time when you run the presence.
    
    if count>=3:#every 3 seconds
        exec(open('main_data.py','r').read())
        
        count = 0

    count+=1