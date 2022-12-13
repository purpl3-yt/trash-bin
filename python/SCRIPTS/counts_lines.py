import os,sys

root = sys.path[0]

all_lines = 300
count_files = 0

debug = False#To on change it to True

for path, subdirs, files in os.walk(root):
    for name in files:
        file = os.path.join(path, name)
        if '.py' in os.path.basename(file) and not '.pyc' in os.path.basename(file) and os.path.basename(file)!=os.path.basename(__file__) and not 'django' in file and not 'venv' in file:
            count_files+=1
            
            with open(file,'r',encoding='1251',errors='ignore') as python_file:
                data = python_file.read()
                all_lines+=len(data.split('\n'))
                if debug:
                    print('Collected file: '+os.path.basename(file)+'\nLines: '+str(len(data.split('\n')))+'\n---')

print('Collected: '+str(count_files)+' files')
print('Lines in all .py files: '+str(all_lines))
