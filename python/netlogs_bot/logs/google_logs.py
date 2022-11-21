accounts_google = []
def lts(list):
    str1 = ' '
    temp1 = str1.join(list)
    return temp1

def find_accounts_google():
    global accounts_google
    import glob,os
    files = glob.glob('Path_To_RedLine_LOGS//*//Passwords.txt')
    list1 = []
    for i in files:
        if '.txt' in i:
            with open(i,encoding='utf-8') as f:
                temp = f.read()
                data = temp.replace('\n',' ')
                list1.append(data)
                temp = f.closed
    valid_list = []
    #print(list1)
    for i in list1:
        if str(i.find('roblox'))!='-1' or str(i.find('com.google.android'))!='-1':
            valid_list.append(i)

    for x in valid_list:
        line_num = int(x.find('google'))
        line_num2 = int(x[line_num:].find('Application'))
        temp1 = x[line_num:line_num2+line_num]
        temp2 = temp1.find('Username')
        done = temp1[temp2:]
        if done != '':
            accounts_google.append('{'+done+'}')
    for c in valid_list:
        line_num_android = int(c.find('com.google.android'))
        line_num2_android = int(c[line_num_android:].find('Application'))
        temp1_android = c[line_num_android:line_num2_android+line_num_android]
        temp2_android = temp1_android.find('Username')
        done_android = temp1_android[temp2_android:]
        if done_android != '':
            accounts_google.append('{'+done_android+'}')
