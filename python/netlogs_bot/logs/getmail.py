import glob
accounts_social = []
files = glob.glob('Path_To_RedLine_LOGS/*/*')
list1 = []
for i in files:
    if '.txt' in i:
        with open(i,'r',encoding='utf-8',errors='ignore') as f:
            temp = f.read()
            data = temp.replace('\n',' ')
            list1.append(data)
            temp = f.closed
valid_list = []
for i in list1:
    if str(i.find(''))!='-1':
        valid_list.append(i)
for x in valid_list:
    line_num = int(x.find('MAIL'))
    line_num2 = int(x[line_num:].find('Username'))
    temp1 = x[line_num:line_num2+line_num]
    temp2 = temp1.find('Username')
    done = temp1[temp2:]
    if done !=' ':
        accounts_social.append('{'+done+'}'+'\n')
print(accounts_social)