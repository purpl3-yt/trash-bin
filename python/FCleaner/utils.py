import os,shutil

clean_folders = {#folders to can be deleted
    'prefetch':['C:\\Windows\\Prefetch','It delete program cache!'],
    'temp':[str(os.getenv('temp')),'It delete temp files!'],
    'discord':[os.getenv('APPDATA')+'\\Roaming\\discord\\Cache','It delete discord cache files!'],
    'recent':[os.getenv('APPDATA')+'\\Microsoft\\Windows\\Recent','It delete recent folder!'],
    'downloads':[os.getenv('USERPROFILE')+'\\Downloads','It delete all files in Download folder!']
}


def deletefiles(folder):#Delete files
    total = len(os.listdir(folder))#total files
    deleted = 0#deleted files
    for filename in os.listdir(folder):#for every file in dir
        file_path = os.path.join(folder, filename)#file_path
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):#if file exist
                deleted+=1#+1 deleted file
                os.unlink(file_path)#delete file? idk what this
            elif os.path.isdir(file_path):#if dir
                shutil.rmtree(file_path)#delete it
        except Exception as e:#if failed to delete file
            print('Error delete: %s. Reason: %s' % (file_path, e))#return exception
    return f'Deleted: {deleted} files of {total}'#return how much files delete and total

def fill_rows(layout,sg):#Add button to layout (check main.py)
    def addbutton(sg,layout,ind,i):#add button
        layout[ind].append(sg.Button('Clean '+i,key=i,size=(27,3),font='Bahnschrift'))#add button to row
    ind = 4#row in layout
    for i in clean_folders.keys(): #add buttons
        if len(layout[ind])<3:#if buttons in row lower than 3
            addbutton(sg,layout,ind,'\n'.join(i.split(' ')))

        elif len(layout[ind])==3:#if buttons in row = 3
            ind+=1#change row
            addbutton(sg,layout,ind,i)