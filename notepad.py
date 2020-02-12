import win32api

win32api.ShellExecute(0, 'open', 'notepad.exe', '','',1)#打開記事本前臺運行
# win32api.ShellExecute(0, 'open', 'notepad.exe', '','',0)#打開記事本前臺運行