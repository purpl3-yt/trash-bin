from random import choice
symbols = ['!','@','#','$','%','^','&','*','(',')','{','}','[']
temp = 'D3ad Launcher 0.2 (Alpha))'
shif = []
shif2 = []
for i in range(1,len(temp)+1):
    shif.append(choice(symbols))
steps = []
phrase = []
for i in range(1,int(len(temp))+1):
    phrase.append(temp[i-1:i])
x = 0
for i in phrase:
    shif.pop(x)
    str = ''.join(shif)
    steps.append(str)
    shif.insert(x,i)
    str = ''.join(shif)
    x+=1