from glob import glob
import os,sys

os.chdir(sys.path[0])

files = glob('*.py')

rate = 0

rate_table_bad = [
    '== True',
    '==True',
    '== False',
    '==False',
    'while 1:',
]

for file in files:

    if file!='code_quality.py':

        with open(file,'r',encoding='1251',errors='ignore') as py_file:
            data_raw = py_file.read()
            data = data_raw.split('\n')

        for line in data:
            for elem in rate_table_bad:
                if elem in line:
                    rate-=1
                    print('You have bad code at line '+str(data.index(line)+1)+' minus 1 rate')

print('Your score: '+str(rate))