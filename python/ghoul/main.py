from time import sleep as wait
import os

print('''
You are ghoul?
1). Yes
2). No
''')
ghoul = input('Select: ')

sum = 1000
minus = 7

if str(ghoul).lower() in ['yes','y','1','да','н']:
    wait(0.5)
    print("I'm ghoul")
    wait(0.4)
    while True:
        if sum!=6:
            print(f'{sum} - 7 = {sum-7}')
            sum-=7
            wait(0.025)
        else:
            print(f'6 - 7 = 0')
            wait(0.025)
            print('0')
            os.system('pause')
            break

elif str(ghoul).lower() in ['no','n','2','нет','т']:
    print("You aren't ghoul :(")