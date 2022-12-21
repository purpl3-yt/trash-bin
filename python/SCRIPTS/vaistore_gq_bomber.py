from cloudscraper import create_scraper
from fake_headers import Headers
from bs4 import BeautifulSoup
from threading import Thread
import requests
import string
import random
import random

strings = string.ascii_letters

host = 'https://vaistore.gq/'
with create_scraper() as s:
  scraper = s.get('https://vaistore.gq/').text

soup = BeautifulSoup(scraper, 'lxml')
temp = soup.find_all('a',href=True)
apps = []
for i in temp:
    temp = str(i['href']).find('?AppID=')
    slice = int(temp)+len('?AppID=')
    if '/' not in str(i['href'][slice:]):
        apps.append(str(i['href'][slice:]))

crash_text = requests.get('https://pastebin.com/raw/14yJb4tu').text #text to lag in comments


def get_list_of_errors():
  with create_scraper() as s:
    for i in range(1,10+1):
      scraper = s.get(host+'Pages/ErrorPage.php?Code='+str(i)).text
      soup = BeautifulSoup(scraper, 'lxml')
      error = soup.find_all('div',class_='Error_Text')
      print(str(error[0].text)+'\nCode='+str(i))
get_list_of_errors()#fuction to get all errors

def get_list_of_comments():
  with create_scraper() as s:
    for app in apps:
      req = s.get(host+'Pages/AppPage_Mobile.php?AppID='+app)
      #print(req.text)
      soup = BeautifulSoup(req.text, 'lxml')
      author = soup.find_all('div',class_='Review_NikName')
      for i in author:
        with open('comments.txt','a') as com:
          com.write(i.parent.text+'\n---------'+app)
#get_list_of_comments()

#headers here
def random_header():#get random header
  header = Headers(browser="chrome",os="win",headers=True)
  return header.generate()

def create_akk(save: bool):
    random_nickname = ''.join(random.choices(strings,k=13))
    random_login = ''.join(random.choices(strings,k=13))
    random_pass = ''.join(random.choices(strings,k=13))
    with create_scraper() as s:
      with requests.Session() as sus:
        reqeust = sus.post(host+'Pages/VaiAccount/Create_Account.php',data={
  'nikname':random_nickname,
  'login':random_login,
  'pass':random_pass,
  'login_vacc':'Создать'
      })
        out = ['Account reg: '+str(reqeust.status_code)+' '+random_login+' '+random_pass,[random_login,random_pass]]
        if not save:
          return out
        elif save:
          with open('accounts.txt','a') as f:
            f.write('Account reg: '+str(reqeust.status_code)+' '+random_login+' '+random_pass+'\n')
          return out

print(create_akk(False))

session_id_old = None
php_id_old = None

def enter_account(login,password,save):
  global session_id_old,php_id_old
  with create_scraper() as s:
    with requests.Session() as sus:
      if session_id_old!=None:
        exit = sus.get(host+'Core/VaiAccount_System/Exit.php',cookies={
            'SessionID':session_id_old
        })
      log = sus.post(host+'Pages/VaiAccount/Login.php',data={
            'Login':login,
            'Password':password,
            'Login_Button':'Войти'
        })
      try:
        sessionid = sus.cookies.get_dict()['SessionID']
        phpid = sus.cookies.get_dict()['PHPSESSID']
      except KeyError:
        pass
      else:
        session_id_old = sessionid
        php_id_old = phpid
        out = [sessionid,phpid]
        if not save:
          return out
        elif save:
          with open('accounts.txt','a') as f:
            f.write('-------------\nLogin to account: '+login+' '+password+'\nSessionID: '+sessionid+'\nPHPID: '+phpid+'\n-------------\n')
          return out
          
print(enter_account('1231234', 'AgOkfLOWkGCbU',False))

def sendreviews(sessionid: str,phpid: str):
  for i in apps:
      reqeust123 = requests.post(host+'Pages/AppPage.php?AppID='+i,cookies={
  'PHPSESSID': str(phpid),
  'SessionID':str(sessionid)

      },data={
  'ReviewText':'Security Test',
  'Post_Review':''
      },headers=random_header(),allow_redirects=False)
      print('Send review: '+str(reqeust123.status_code)+' To app: '+i)

for i in range(2):
  sendreviews('9f287e3ab9746f97dd2787802c8d8cf2','boopbfa1ss0lnunq0ur50bkc64')

# **Actions**

for i in range(4):
  reg = create_akk(True)
  print(reg[0])
  login = reg[1][0]
  password = reg[1][1]
  log = enter_account(login,password,False)
  try:
    print('Saved akk: '+log[0],log[1])
  except TypeError:
    quit()
  else:
    with open('drive/MyDrive/accs.txt','a') as acc:
      acc.write(log[0]+':'+log[1]+'\n')


acc = create_akk(False)
log = enter_account(acc[1][0],acc[1][1],False)
print(log)

with open('drive/MyDrive/accs.txt','r') as accs:
  accounts = accs.read()
  accounts = accounts.split('\n')

accs_to_spam = []

sessions_id_to_spam = []

php_id_to_spam = []

for i in accounts:
  accs_to_spam.append(i.split(':'))

for sus in accs_to_spam:
  if sus[0]!='':
    sessions_id_to_spam.append(sus[0])
    php_id_to_spam.append(sus[1])
    
import random
def send_review():
  reqeust123 = requests.post(host+'vai_acc_sys/system/AddReview.php?AppID='+'NULL',cookies={
  'SessionID':random.choice(sessions_id_to_spam),
  'PHPSESSID':random.choice(php_id_to_spam),

  },data={
  'ReviewText':"Хаксто лошара, бож когда будет обнова?",
  'Post_Review':''
  },headers=random_header(),allow_redirects=False)
  print('Send review: '+str(reqeust123.status_code)+' To app: '+'NULL')
for i in range(10):
  send_review()
    


print(accounts)
for i in range(100):
  break
  class GG(Thread):
    def run(self):
      create_akk(True)
      sendreviews('c04379e3a209b2ae8118e63234332057','boopbfa1ss0lnunq0ur50bkc64')
  gg = GG()
  gg.start()

