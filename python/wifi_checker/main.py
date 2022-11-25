from time import sleep as wait
import requests
import playsound
#^-- imports
while True:
    try:
        getsite = requests.get('https://google.com')#send request
    except requests.exceptions.ConnectionError:#if request bad
        print('Check wifi...')
        wait(10)#every 10 seconds
        pass
    else:#if request good
        for i in range(3):#play sound 3 times
            playsound.playsound('internet_true.mp3')
        break#end