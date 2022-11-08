import sqlite3
import sys
import os

class Game:
    def __init__(self,name,genres,type,description,year,systemrequirements,cost,likes,img,gamelink,id=0):
        self.id = id
        self.name = name
        self.genres = genres
        self.type = type
        self.description = description
        self.year = year
        self.systemrequirements = systemrequirements
        self.cost = cost
        self.likes = likes
        self.img = img
        self.gamelink = gamelink

    def getname(self):
        return self.name
    def setname(self, newname):
        self.name = newname
    def gettype(self):
        return self.type
    def settype(self, type):
        self.type = type
    def getlikes(self):
        return self.likes
    def setlikes(self,likes):
        self.likes = likes
    def getid(self):
        return self.id
    def getgenres(self):
        return self.genres
    def setdescription(self, description):
        self.description = description
    def getdescription(self):
        return self.description
    def setyear(self, year):
        self.year = year
    def getyear(self):
        return self.year
    def setsystemrequirements(self, sysrequire):
        self.systemrequirements = sysrequire
    def getsystemrequirements(self):
        return self.systemrequirements
    def setcost(self, cost):
        self.cost = cost
    def getcost(self):
        return self.cost
    def setimg(self, img):
        self.img = img
    def getimg(self):
        return self.img
    def setgamelink(self,gamelink):
        self.gamelink = gamelink
    def getgamelink(self):
        return self.gamelink

    def __str__(self) -> str:
        return f'''
ID: {self.id}
NAME: {self.name}
GENRES: {self.genres}
TYPE: {self.type}
DESCRIPTION: {self.description}
YEAR: {self.year}
SYSTEM REQUIREMENTS: {self.systemrequirements}
COST: {self.cost}₴
LIKES: {self.likes}
URL: {self.img}
GameLink: {self.gamelink}'''
class Genre:
    def __init__(self,name, id=0):
        self.id = id
        self.name = name
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name = newname
    def getid(self):
        return self.id
    def __str__(self):
        return f"""
ID: {self.id}
NAME: {self.name}
        """
def superuser():
    con = condb()
    cursor = con.cursor()

    qwery = f'''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login STRING,
    password STRING
    );
    '''

    cursor.execute(qwery)
    con.commit()
    qwery = f'''
    INSERT INTO users VALUES(0,"Purpl3_YT","admin");
    '''
    cursor.execute(qwery)
    con.commit()
    con.close()

def start():
    db = 'game.db'
    try:
        con=sqlite3.connect(db)
        cursor = con.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS genre(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name STRING);
        ''')
        con.commit()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS game(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name STRING,
            genres INTEGER,
            type STRING,
            description TEXT,
            year INTEGER,
            systemrequirements STRING,
            cost INTEGER,
            likes REAL,
            img STRING,
            gamelink STRING,
            FOREIGN KEY (genres) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE 
            
            );
            '''
        )
        res = cursor.fetchall()
        superuser()
        #print(res)
    except sqlite3.Error as error:
        print('Error', error)
    finally:
        if(con):
            con.close()
            print('DB close')

#DB CONTROL

def condb():
    db = 'game.db'
    con = sqlite3.connect(db)
    return con

def convertimg(file_name):
    with open(file_name,'rb') as file:
        blob_date = file.read()
    return blob_date

def adddb(obj):
    con = condb()
    cursor = con.cursor()
    table = str(type(obj)).split('.')[1].split("'")[0].lower()
    if table == 'game':
        #print(type(obj.img))
        cursor.execute(f'''
        INSERT INTO {table} VALUES(?,?,?,?,?,?,?,?,?,?,?);
        ''', (None, obj.name.lower(), obj.genres, obj.type.lower(), obj.description.lower(), obj.year, obj.systemrequirements.lower(), obj.cost, obj.likes, obj.img, obj.gamelink))
        con.commit()
    if table == 'genre':
        cursor.execute(f'''
                INSERT INTO {table} VALUES(?,?);
                ''', (
        None, obj.name.lower()))
        con.commit()
    con.close()


def get_all_data_game():
    res = []
    con = condb()
    cursor = con.cursor()
    
    qwery = f'''
    SELECT * FROM game;
    '''
    cursor.execute(qwery)
    record = cursor.fetchall()
    
    for rec in record:
        g = Game(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9],rec[10], id=rec[0])
        res.append(g)
   
    con.close()
    return res 

def get_all_data_genre():
    res = []
    con = condb()
    cursor = con.cursor()
    
    qwery = f'''
    SELECT * FROM genre;
    '''
    cursor.execute(qwery)
    record = cursor.fetchall()
    
    for rec in record:
        g = Genre(rec[1],id=rec[0])
        res.append(g)
    con.close()
    return res

def get_new_game():
    res = []
    con = condb()
    cursor = con.cursor()

    qwery = """
    SELECT * FROM game ORDER BY year DESC;
    """

    cursor.execute(qwery)
    record = cursor.fetchall()
    for rec in record:
        #print('new',rec[0])
        g = Game(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9],rec[10], id=rec[0])
        res.append(g)
    con.close()
    return res

def get_pop_game():
    res = []
    con = condb()
    cursor = con.cursor()

    qwery = """
    SELECT * FROM game ORDER BY likes DESC;
    """

    cursor.execute(qwery)
    record = cursor.fetchall()
    for rec in record:
        g = Game(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9],rec[10], id=rec[0])
        res.append(g)
    con.close()
    return res

def get_all_id():
    ids = []
    con = condb()
    cursor = con.cursor()

    qwery = """
    SELECT id FROM game
    """
    
    cursor.execute(qwery)
    record = cursor.fetchall()

    for rec in record:
        ids.append(rec[0])

    con.close()

    return ids
    
def delete(obj):
    con = condb()
    cursor = con.cursor()
    table = str(type(obj)).split('.')[1].split("'")[0].lower()
    if table == 'game':
        qwery = f'''
        DELETE FROM {table} WHERE id = {obj.id}
        '''
        cursor.execute(qwery)
        con.commit()
    if table == 'genre':
        qwery = f'''
        DELETE FROM {table} WHERE id = {obj.id}
        '''
        cursor.execute(qwery)
        con.commit()
        print('delete id : ', obj.id)
    con.close()



def print_all(arr):
    for item in arr:
        print(item)

def find(find_str):
    res = []
    con = condb()
    cursor = con.cursor()

    qwery = f'''
    SELECT * FROM game WHERE name = "{find_str}";
    '''
    cursor.execute(qwery)
    record = cursor.fetchall()
    for rec in record:
        g = Game(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9],rec[10], id=rec[0])
        res.append(g)
    con.close()
    return record

def findbyid(id):
    con = condb()
    cursor = con.cursor()

    qwery = f'''
    SELECT * FROM game WHERE id = "{id}"
    '''
    cursor.execute(qwery)
    record = cursor.fetchall()
    game = Game(record[0][1], record[0][2], record[0][3],record[0][4],record[0][5],record[0][6],record[0][7],record[0][8],record[0][9],record[0][10], id=record[0][0])
    con.close()
    return game

def update(game, name, type, desc, year, systemrequire, cost, likes, img, gamelink):
    con = condb()
    cursor = con.cursor()

    game.setname(name)
    game.settype(type)
    game.setdescription(desc)
    game.setyear(year)
    game.setsystemrequirements(systemrequire)
    game.setcost(cost)
    game.setlikes(likes)
    game.setimg(img)
    game.setgamelink(gamelink)

    qwery = f'''
    UPDATE game SET likes = {game.getlikes()}, name = "{game.getname()}", type = "{game.gettype()}", description = "{game.getdescription()}", year = {game.getyear()}, systemrequirements = "{game.getsystemrequirements()}", cost = {game.getcost()}, img = "{game.getimg()}", gamelink = "{game.getgamelink()}"  WHERE id = "{game.getid()}"

    '''

    cursor.execute(qwery)
    con.commit()
    con.close()

    

def updatelikes(like,game):
    con = condb()
    cursor = con.cursor()

    old_likes = game.getlikes()
    new_likes = round((old_likes+like)/2, 3)

    qwery = f'''
    UPDATE game SET likes = {new_likes} WHERE id = "{game.getid()}"
    '''
    cursor.execute(qwery)
    con.commit()
    con.close()

def tryenter(login,password):
    con = condb()
    cursor = con.cursor()

    qwery = f'''
    SELECT login,password FROM users;
    '''

    cursor.execute(qwery)
    res = cursor.fetchall()
    if login == res[0][0] and password == res[0][1]: #1 login 2 password
        return True
    else:
        return False

game = Game('Побег за салом', 1,'2D','Игра где главный персонаж бежит за салом\nИ проходит препятствия',2013,'Windows',100, 2.5,'./assets/pobeg_za_salom1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Escape%20for%20lard.txt')#By Purpl3
game2 = Game('Симулятор лампочки', 2, '3D', 'Игра где вам нужно прокачивать свою лампочку',2016,'Windows Linux',1999,0.0,'./assets/simulator_lampochki1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Light%20bulb%20simulator.txt')#By Rawitti
game3 = Game('Собери свою клавиатуру', 3, '2D', 'Игра где вы сделали свой бизнес \nПро продаже клавиатур',2019, 'Android Windows Linux', 25, 0.0,'./assets/soberi_svoy_klaviatyry1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Build%20Your%20Keyboard.txt')#By Rawitti
game4 = Game('Фонарик Vip', 4, '6D', 'Профессиональный фонарик для vip персон \nМожно осветить целую вселенную на минимальной яркости', 2017, 'Android', 39999, 0.0,'./assets/fonarick_vip1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Vip%20Flashlight.txt')#By Rawitti
game5 = Game('Кидание вещей из окна', 5, '3D', 'В этой игре вы будете кидать \nРазные вещи из окна', 2018, 'Android Windows MacOS', 150, 0.0,'./assets/throwing_things_out_the_window1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Throwing%20things%20out%20the%20window.txt')#By Rawitti
game6 = Game('Улучшение стола',6,'2D', 'В этой игре вам нужно улучшать ваш стол', 2020, 'Windows Linux', 365, 0.0,'./assets/table_update1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Table%20upgrade.txt')#By Rawitti
game7 = Game('Симулятор Джима',7,'3D','Тут вы будете тренироваться\nИ прокачивать свои скиллы и пвпхаться на арене',2017,'Windows',133, 0.0, './assets/simulator_gyma1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Gym%20Simulator.txt')#By Rawitti
game8 = Game('Выживание тапка',8,'3D','Вы в пустыне\nИ вы должны выжить, удачи!',2022,'Windows MacOS',150,0.0,'./assets/vishivanie_tapka1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Sneaker%20survival.txt')#By Rawitti
game9 = Game('Крижовые истории',9,'2D','Кринжовые истории\nКоторые вам предстоит прочитать и не заржать',2021,'Android IOS',10,0.0,'./assets/cringe_stories1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Cringe%20Stories.txt')# By Rawitti
game10 = Game('Придумай сам',10,'0D','Описание тоже придумай сам\nМне лень',9999,'Придумай сам',0,0.0,'./assets/pridymai_sam1.png','https://raw.githubusercontent.com/purpl3-yt/lessongames/main/Get%20it%20by%20youself.txt')#By Purpl3



'''
TODO:
[+] Сделать игры
[+] Сделать жандры для них
[+] Сделать картинки для игр и добавить на них текст

+ = сделал
- = не сделал
? = в планах
'''

genre = Genre('Platform') # Game 1 
genre2 = Genre('Simulator') # Game 2
genre3 = Genre('Puzzle') # Game 3
genre4 = Genre('App') # Game 4
genre5 = Genre('Fun') # Game 5
genre6 = Genre('Tycoon') # Game 6
genre7 = Genre('Simulator') # Game 7
genre8 = Genre('Survival') # Game 8
genre9 = Genre('Fun') # Game 9
genre10 = Genre('Fun') # Game 10

def add_games():
    games_list = [game,game2,game3,game4,game5,game6,game7,game8,game9,game10]
    genre_list = [genre,genre2,genre3,genre4,genre5,genre6,genre7,genre8,genre9,genre10]
    for i in games_list:
        adddb(i)
    for x in genre_list:
        adddb(x)
if not os.path.isfile('./game.db'):
    start()
    add_games()




#Utils for gui
def pathtofile(file):
    currect_path = sys.path[0]
    done = str(currect_path+file)
    return done


def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')