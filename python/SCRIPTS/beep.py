import win32api
for i in range(50, 2000+10, 10):
    win32api.Beep(i,100)
    print(i)