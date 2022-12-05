from random import randint, getrandbits

class Human:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.food = 100
        self.days = 0
        self.money = 0
        self.gladness = 100
        self.isAlive = True
    
    def ifAlive(self):
        if self.food<=0:
            self.isAlive=False
        if not self.isAlive:
            print(f'You died :(\n\nYou alive {str(self.days)} days')
            quit()

    def CalcStat(self, stat: int,stat_name: str, min: int, max: int):#Calculate your stats, money, gladness, food
        if not not getrandbits(1):#True
            stat += randint(min,max)
        else:#False
            stat -= randint(min,max)
        exec('self.'+stat_name+'='+str(stat))

    def live(self):

        if self.days>=360 and self.isAlive:
            print('\n\nHappy Birthday to you!\n\n')
            self.days = 100

        self.CalcStat(self.food,'food',1,10)
        self.CalcStat(self.gladness,'gladness',1,5)

        if self.food>=100:#If food bigger than 100 set it to 100
            self.food = 100#Set food 100

        self.ifAlive()#Check if human alive

        self.days+=1#Add 1 day
        
        print(f'''
Day: {self.days}
Food: {self.food}
Gladness: {self.gladness}''')#Statistics

Character = Human('John',13)

print('\nYour name is: '+Character.name+'\nAge: '+str(Character.age))

while True:
    Character.live()
    input('Next day? ')