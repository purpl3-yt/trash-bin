from logs.logs import find_accounts,accounts_social
open('file.txt', 'w').close()
done_search = find_accounts('yandex.ru')
print('Найдено '+str(len(accounts_social))+' Результатов!')
with open('file.txt', 'w',encoding='utf-8',errors='ignore') as f:
        f.write(str(done_search))