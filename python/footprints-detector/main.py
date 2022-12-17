from urllib.parse import urlparse
import googlesearch
import os,sys
import base64

os.chdir(sys.path[0])

log_file = 'log.txt'

def print_result(result):
    print(f'Found an {urlparse(result).hostname}, url: '+result)

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

nsfw = False

nsfw_strings = ['cG9ybg==','c2V4','cG9ybm8=','eHZpZGVv']#18+ words
decoded_nsfw_strings = []
for nsfw_string in nsfw_strings:
    decoded_nsfw_strings.append(bytes(base64.b64decode(nsfw_string)).decode('utf-8'))


def check_nsfw(result,nsfw,nsfw_count):
    for string in decoded_nsfw_strings:
        if string in result:
            if not nsfw:
                print('Nsfw url found!')
            if nsfw:
                print('Nsfw url found: '+result)
            nsfw_count+=1
            return True

while True:
    nickname = input('Enter an nickname ("2" clear log, "3" enable nsfw results): ')
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
    
    elif nickname=='3':
        if nsfw:
            nsfw=False
            print('Disable nsfw')
        elif not nsfw:
            nsfw=True
            print('Enable nsfw')


    else:
        if nickname!='':
            break
        else:
            print('Enter Nickname!')

count = 0
nsfw_count = 0

for result in search:

    if check_nsfw(result,nsfw,nsfw_count):
        nsfw_count+=1

    elif not check_nsfw(result,nsfw,nsfw_count):
        print_result(result)

        count+=1

        save_result(urlparse(result).hostname,result)

print('With request: '+str(nickname)+' founded '+str(count)+' sites of which '+str(nsfw_count)+' nsfw')