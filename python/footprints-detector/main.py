from urllib.parse import urlparse
import googlesearch
import os,sys

os.chdir(sys.path[0])

log_file = 'log.txt'

def generate_google(text: str):#unused
    return 'https://www.google.com/search?q='+text

def check_log(query: str):
    with open(log_file,'r') as log:
        data = log.read()
        if query in data:
            return True
        elif not query in data:
            return False
def save_result(site: str,url: str):
    str_to_save = 'Found '+site+' url: '+url

    if not check_log(str_to_save):
        with open(log_file,'a') as log:
            log.write(str_to_save+'\n')

while True:
    nickname = input('Enter an nickname (2 clear log): ')
    #nickname = 'PLNT'
    #results = input('Enter an count of results (int): ')
    results = 100
    search = googlesearch.search(nickname,results)

    if nickname=='2':
        try:
            with open('log.txt','w') as log:
                log.write('')
        except FileNotFoundError:
            pass
    else:
        if nickname!='':
            break
        else:
            print('Enter Nickname!')

for result in search:

    print(f'Found an {urlparse(result).hostname}, url: '+result)
    
    save_result(urlparse(result).hostname,result)