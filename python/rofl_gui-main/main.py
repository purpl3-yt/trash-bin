import wx
import pyautogui
import os
import string
import webbrowser
import subprocess
from screeninfo import get_monitors
from random import randint,choices
from time import sleep as wait

pyautogui.FAILSAFE = False
random_symbols = string.printable
exit_count = 0
class Frame(wx.Frame):
    def __init__(self, *args, **kw):
        super(Frame, self).__init__(*args, **kw)
        self.SetTitle('...')

        pnl = wx.Panel(self)

        st = wx.StaticText(pnl, label='Что ты тут забыл?')
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        scaryt = wx.StaticText(pnl, label=''.join(choices(random_symbols,k=70)))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 70))
        pnl.SetSizer(sizer)


        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText('Зачем это читать?')


    def makeMenuBar(self):

        fileMenu = wx.Menu()

        unusedItem = fileMenu.Append(-1, '&Не ну эт кринж',
                'ДА БОЖЕ ЗАЧЕМ ТЫ ЭТО ЧИТАЕШЬ БОТИК ПОПУЩЕННЫЙ')
        fileMenu.AppendSeparator()

        exitItem = fileMenu.Append(wx.ID_EXIT,'Выйти из этого кринжа\tAlt-F4',
        'Да, давай, нажми эту кнопку, и прекрати этот кринж')

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(1923,'Если нажмешь взорвется все','Не ну рил, я не шучу')
        virusItem = helpMenu.Append(666,'99.9% вирус')

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&Что это?')
        menuBar.Append(helpMenu, '&Зач?')

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnUnused, unusedItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnCrash, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnVirus, virusItem)
        self.Bind(wx.EVT_CLOSE,self.OnExit)


    def OnExit(self, event):
        global exit_count
        exit_count += 1
        count = 2
        if exit_count<count:
            wx.MessageBox('''
Ну что? выйти не можешь :)''')
        elif exit_count>=count:
            self.Destroy()


    def OnUnused(self, event):
        wx.MessageBox('чтотчточотччтоточточот','НУ И ЗАЧЕМ ТЫ НАЖАЛ БОЖЕ ВЫЙДИ ОТ СЮДА')

    def OnVirus(self, event):
        wx.MessageBox('бан','Зач нажал? написано что вирус же')
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def OnCrash(self, event):
        for i in range(30):#change to 30
            random_x = randint(10,int(get_monitors()[0].width))#get monitor width
            random_y = randint(10,int(get_monitors()[0].height))#get monitor height
            pyautogui.moveTo(random_x,random_y,0.1)#move mouse at random position

            random_x_win = randint(10,int(get_monitors()[0].width))#get monitor width
            random_y_win = randint(10,int(get_monitors()[0].height))#get monitor height
            frm.SetPosition((random_x_win,random_y_win))
        
        os.system('TASKKILL /F /IM explorer.exe')
        wait(2)
        wx.MessageBox('''
И что? 
Чем ты этим добился?
Ничем?
Ровным счетом н и ч е г о
И ты серьезно думаешь это все?''')
        wait(1)
        wx.MessageBox(''.join(choices(random_symbols,k=100)))
        subprocess.Popen('explorer')
        self.Destroy()
if __name__ == '__main__':
    app = wx.App()
    frm = Frame(None)
    frm.Show()
    app.MainLoop()