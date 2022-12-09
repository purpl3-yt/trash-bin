import win32api
for i in range(50, 2000+10, 10):
    print(i)
    win32api.Beep(i,100)