import os,sys

root = sys.path[0]

all_lines = 300

for path, subdirs, files in os.walk(root):
    for name in files:
        file = os.path.join(path, name)
        if '.py' in os.path.basename(file) and not '.pyc' in os.path.basename(file) and os.path.basename(file)!=os.path.basename(__file__) and not 'django' in file:
            if not 'venv' in file:
                with open(file,'r',encoding='1251',errors='ignore') as python_file:
                    data = python_file.read()
                    all_lines+=len(data.split('\n'))

print(all_lines)
