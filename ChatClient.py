#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.11
# In conjunction with Tcl version 8.6
#    Mar 15, 2018 04:56:32 PM
__author__ = "Deep Katariya"
import sys


import tkinter.ttk as ttk

from threading import Thread
from ChatFns import *
from PyChatSentimentModule import *




# import unknown_supportTest

'''Starting point when module is the main routine.'''
def ClickAction():
    #Write message to chat window
    EntryText = FilteredMessage(top.ChatMessageBox.get("0.0",END))

    LoadMyEntry(top.ChatLogBox, EntryText)

    #Scroll to the bottom of chat windows
    top.ChatLogBox.yview(END)

    #Erace previous message in Entry Box
    top.ChatMessageBox.delete("0.0",END)

    #Send my mesage to all others
    s.sendall(bytes(EntryText, 'UTF-8'))

def PressAction(event):
    top.ChatMessageBox.config(state=NORMAL)
    ClickAction()

def DisableEntry(event):
    top.ChatMessageBox.config(state=DISABLED)

def updateRating(connStatus, message, RatingChat, RatingMessage, RatingChatColor, RatingMessageColor):
    global messageScore, chatScore

    if connStatus:
        scoreSheet = polarity_score(message)
        print('this is the score now', scoreSheet['compound'])
        messageScore = scoreSheet['compound']
        chatScore += scoreSheet['compound']
        print('THis is the chatscore going on', chatScore)
        RatingMessageColor.configure(state=NORMAL)
        RatingChatColor.configure(state=NORMAL)
        # message score color changer
        if messageScore == 0:
            RatingMessageColor.configure(background="yellow")
        elif 0 < messageScore <=0.5:
            RatingMessageColor.configure(background="green yellow")
        elif messageScore > 0.5:
            RatingMessageColor.configure(background="forest green")
        elif 0 > messageScore >= -0.5:
            RatingMessageColor.configure(background="red")
        elif messageScore < -0.5:
            RatingMessageColor.configure(background="red4")

        # chat score color changer
        if 0.5 >= chatScore >= -0.5:
            print('in 1')
            RatingChatColor.configure(background="yellow")
        elif 1.5 >= chatScore > 0.5:
            print('in 2')
            RatingChatColor.configure(background="green yellow")
        elif chatScore > 1.5:
            print('in 3')
            RatingChatColor.configure(background="forest green")
        elif -1.5 <= chatScore <= -0.5:
            print('in 4')
            RatingChatColor.configure(background="red")
        elif chatScore < -1.5:
            print('in 5')
            RatingChatColor.configure(background="red4")

        RatingMessageColor.configure(state=DISABLED)
        RatingChatColor.configure(state=DISABLED)

    else:
        messageScore, chatScore = 0, 0
        RatingMessageColor.configure(state=NORMAL)
        RatingChatColor.configure(state=NORMAL)

        RatingMessageColor.configure(background="white")
        RatingChatColor.configure(background="white")

        RatingMessageColor.configure(state=DISABLED)
        RatingChatColor.configure(state=DISABLED)

    RatingChat.configure(state=NORMAL)
    RatingChat.delete(1.0, END)
    RatingChat.insert(INSERT, chatScore)
    RatingChat.configure(state=DISABLED)

    RatingMessage.configure(state=NORMAL)
    RatingMessage.delete(1.0, END)
    RatingMessage.insert(INSERT, messageScore)
    RatingMessage.configure(state=DISABLED)



def GetConnected():
    try:
        s.connect((HOST, PORT))
        LoadConnectionInfo(top.ChatLogBox, '[ Succesfully connected ]\n---------------------------------------------------------------')
        SetConnectionInfo(top.UserStatusMessage, top.StatusMessage, HOST)

    except:
        LoadConnectionInfo(top.ChatLogBox, '[ Unable to connect ]')
        return

def StartReceiving():
    while 1:
        try:
            data = s.recv(1024)
            data = data.decode('utf-8')
        except:
            data = ''
            updateRating(False, data, top.RatingChat, top.RatingMessage, top.RatingChatColor, top.RatingMessageColor)
            LoadConnectionInfo(top.ChatLogBox, '\n [ Your partner has disconnected ] \n')
            UnsetConnectionInfo(top.UserStatusMessage, top.StatusMessage)
            break
        if data != '':
            updateRating(True, data, top.RatingChat, top.RatingMessage, top.RatingChatColor, top.RatingMessageColor)
            LoadOtherEntry(top.ChatLogBox, data)

            if root.focus_get() == None:
                pass
                # FlashMyWindow(WindowTitle)
                # playsound('notif.wav')
        else:
            LoadConnectionInfo(top.ChatLogBox, '\n [ Your partner has disconnected ] \n')
            break



def create_PyChat_Mood_Detector(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = PyChat_Mood_Detector (w)
    # unknown_supportTest.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_PyChat_Mood_Detector():
    global w
    w.destroy()
    w = None


class PyChat_Mood_Detector:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("488x536+867+195")
        top.title("PyChat Client")
        top.configure(background="#d2d2d2")

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.04, relheight=0.94, relwidth=0.95)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#dfdfdf")
        self.Frame1.configure(width=465)

        self.SendButton = ttk.Button(self.Frame1)
        self.SendButton.place(relx=0.73, rely=0.71, height=130, width=118)
        self.SendButton.configure(takefocus="")
        self.SendButton.configure(text='Send')
        self.SendButton.configure(width=118)
        self.SendButton.configure(command=ClickAction)

        self.ChatLogBox = Text(self.Frame1)
        self.ChatLogBox.place(relx=0.02, rely=0.22, relheight=0.46
                , relwidth=0.95)
        self.ChatLogBox.configure(background="white")
        self.ChatLogBox.configure(font="TkTextFont")
        self.ChatLogBox.configure(foreground="black")
        self.ChatLogBox.configure(highlightbackground="#d9d9d9")
        self.ChatLogBox.configure(highlightcolor="black")
        self.ChatLogBox.configure(insertbackground="black")
        self.ChatLogBox.configure(relief=GROOVE)
        self.ChatLogBox.configure(selectbackground="#c4c4c4")
        self.ChatLogBox.configure(selectforeground="black")
        self.ChatLogBox.configure(width=444)
        self.ChatLogBox.configure(wrap=WORD)

        # self.Label1 = Label(self.Frame1)
        # self.Label1.place(relx=0.04, rely=0.02, height=36, width=62)
        # self.Label1.configure(background="#d9d9d9")
        # self.Label1.configure(disabledforeground="#a3a3a3")
        # self.Label1.configure(foreground="#000000")
        # self.Label1.configure(text='''Label''')
        # self.Label1.configure(width=62)

        self.StatusLabel = Label(self.Frame1)
        self.StatusLabel.place(relx=0.04, rely=0.02, height=36, width=62)
        self.StatusLabel.configure(activebackground="#f9f9f9")
        self.StatusLabel.configure(activeforeground="black")
        self.StatusLabel.configure(background="#d9d9d9")
        self.StatusLabel.configure(disabledforeground="#a3a3a3")
        self.StatusLabel.configure(foreground="#000000")
        self.StatusLabel.configure(highlightbackground="#d9d9d9")
        self.StatusLabel.configure(highlightcolor="black")
        self.StatusLabel.configure(highlightthickness="1")
        self.StatusLabel.configure(relief=GROOVE)
        self.StatusLabel.configure(text='''Status''')

        self.UserNameLabel = Label(self.Frame1)
        self.UserNameLabel.place(relx=0.04, rely=0.12, height=36, width=62)
        self.UserNameLabel.configure(background="#d9d9d9")
        self.UserNameLabel.configure(disabledforeground="#a3a3a3")
        self.UserNameLabel.configure(foreground="#000000")
        self.UserNameLabel.configure(relief=GROOVE)
        self.UserNameLabel.configure(text='''User''')
        self.UserNameLabel.configure(width=62)

        self.StatusMessage = Text(self.Frame1)
        self.StatusMessage.place(relx=0.22, rely=0.02, relheight=0.07
                , relwidth=0.18)
        self.StatusMessage.configure(background="white")
        self.StatusMessage.configure(font="TkTextFont")
        self.StatusMessage.configure(foreground="black")
        self.StatusMessage.configure(highlightbackground="#d9d9d9")
        self.StatusMessage.configure(highlightcolor="black")
        self.StatusMessage.configure(insertbackground="black")
        self.StatusMessage.configure(relief=GROOVE)
        self.StatusMessage.configure(selectbackground="#c4c4c4")
        self.StatusMessage.configure(selectforeground="black")
        self.StatusMessage.configure(width=84)
        self.StatusMessage.configure(wrap=WORD)
        self.StatusMessage.insert(INSERT, "Disconnected")
        self.StatusMessage.configure(state=DISABLED)

        self.UserStatusMessage = Text(self.Frame1)
        self.UserStatusMessage.place(relx=0.22, rely=0.12, relheight=0.07
                , relwidth=0.18)
        self.UserStatusMessage.configure(background="white")
        self.UserStatusMessage.configure(font="TkTextFont")
        self.UserStatusMessage.configure(foreground="black")
        self.UserStatusMessage.configure(highlightbackground="#d9d9d9")
        self.UserStatusMessage.configure(highlightcolor="black")
        self.UserStatusMessage.configure(insertbackground="black")
        self.UserStatusMessage.configure(relief=GROOVE)
        self.UserStatusMessage.configure(selectbackground="#c4c4c4")
        self.UserStatusMessage.configure(selectforeground="black")
        self.UserStatusMessage.configure(width=84)
        self.UserStatusMessage.configure(wrap=WORD)
        self.UserStatusMessage.insert(INSERT, "No user")
        # self.UserStatusMessage.delete(1.0, END)
        # self.UserStatusMessage.insert(INSERT, "It changed")
        self.UserStatusMessage.configure(state=DISABLED)



        self.MessageRatingLabel = Label(self.Frame1)
        self.MessageRatingLabel.place(relx=0.47, rely=0.02, height=36, width=82)
        self.MessageRatingLabel.configure(background="#d9d9d9")
        self.MessageRatingLabel.configure(disabledforeground="#a3a3a3")
        self.MessageRatingLabel.configure(foreground="#000000")
        self.MessageRatingLabel.configure(relief=GROOVE)
        self.MessageRatingLabel.configure(text='''Message''')
        self.MessageRatingLabel.configure(width=82)

        self.ChatRatingLabel = Label(self.Frame1)
        self.ChatRatingLabel.place(relx=0.47, rely=0.12, height=36, width=82)
        self.ChatRatingLabel.configure(background="#d9d9d9")
        self.ChatRatingLabel.configure(disabledforeground="#a3a3a3")
        self.ChatRatingLabel.configure(foreground="#000000")
        self.ChatRatingLabel.configure(relief=GROOVE)
        self.ChatRatingLabel.configure(text='''Chat''')
        self.ChatRatingLabel.configure(width=82)

        self.RatingMessage = Text(self.Frame1)
        self.RatingMessage.place(relx=0.69, rely=0.02, relheight=0.07
                , relwidth=0.26)
        self.RatingMessage.configure(background="white")
        self.RatingMessage.configure(font="TkTextFont")
        self.RatingMessage.configure(foreground="black")
        self.RatingMessage.configure(highlightbackground="#d9d9d9")
        self.RatingMessage.configure(highlightcolor="black")
        self.RatingMessage.configure(insertbackground="black")
        self.RatingMessage.configure(relief=GROOVE)
        self.RatingMessage.configure(selectbackground="#c4c4c4")
        self.RatingMessage.configure(selectforeground="black")
        self.RatingMessage.configure(width=122)
        self.RatingMessage.configure(wrap=WORD)
        self.RatingMessage.configure(state=DISABLED)

        self.RatingChat = Text(self.Frame1)
        self.RatingChat.place(relx=0.69, rely=0.12, relheight=0.07
                , relwidth=0.27)
        self.RatingChat.configure(background="white")
        self.RatingChat.configure(font="TkTextFont")
        self.RatingChat.configure(foreground="black")
        self.RatingChat.configure(highlightbackground="#d9d9d9")
        self.RatingChat.configure(highlightcolor="black")
        self.RatingChat.configure(insertbackground="black")
        self.RatingChat.configure(relief=GROOVE)
        self.RatingChat.configure(selectbackground="#c4c4c4")
        self.RatingChat.configure(selectforeground="black")
        self.RatingChat.configure(width=124)
        self.RatingChat.configure(wrap=WORD)
        self.RatingChat.configure(state=DISABLED)

        self.ChatMessageBox = Text(self.Frame1)
        self.ChatMessageBox.place(relx=0.02, rely=0.71, relheight=0.27
                , relwidth=0.7)
        self.ChatMessageBox.configure(background="white")
        self.ChatMessageBox.configure(font="TkTextFont")
        self.ChatMessageBox.configure(foreground="black")
        self.ChatMessageBox.configure(highlightbackground="#d9d9d9")
        self.ChatMessageBox.configure(highlightcolor="black")
        self.ChatMessageBox.configure(insertbackground="black")
        self.ChatMessageBox.configure(selectbackground="#c4c4c4")
        self.ChatMessageBox.configure(selectforeground="black")
        self.ChatMessageBox.configure(width=324)
        self.ChatMessageBox.configure(wrap=WORD)
        self.ChatMessageBox.bind("<Return>", DisableEntry)
        self.ChatMessageBox.bind("<KeyRelease-Return>", PressAction)
        print('scrollbar setting')
        scrollbar = Scrollbar(self.Frame1, command=self.ChatLogBox.yview)
        self.ChatLogBox['yscrollcommand'] = scrollbar.set
        print('scrollbar set!')


        self.RatingMessageColor = Text(self.Frame1)
        self.RatingMessageColor.place(relx=0.9, rely=0.02, relheight=0.07
                , relwidth=0.07)
        self.RatingMessageColor.configure(background="white")
        self.RatingMessageColor.configure(font="TkTextFont")
        self.RatingMessageColor.configure(foreground="black")
        self.RatingMessageColor.configure(highlightbackground="#d9d9d9")
        self.RatingMessageColor.configure(highlightcolor="black")
        self.RatingMessageColor.configure(insertbackground="black")
        self.RatingMessageColor.configure(selectbackground="#c4c4c4")
        self.RatingMessageColor.configure(selectforeground="black")
        self.RatingMessageColor.configure(width=34)
        self.RatingMessageColor.configure(wrap=WORD)
        self.RatingMessageColor.configure(state=DISABLED)

        self.RatingChatColor = Text(self.Frame1)
        self.RatingChatColor.place(relx=0.9, rely=0.12, relheight=0.07
                , relwidth=0.07)
        self.RatingChatColor.configure(background="white")
        self.RatingChatColor.configure(font="TkTextFont")
        self.RatingChatColor.configure(foreground="black")
        self.RatingChatColor.configure(highlightbackground="#d9d9d9")
        self.RatingChatColor.configure(highlightcolor="black")
        self.RatingChatColor.configure(insertbackground="black")
        self.RatingChatColor.configure(selectbackground="#c4c4c4")
        self.RatingChatColor.configure(selectforeground="black")
        self.RatingChatColor.configure(width=34)
        self.RatingChatColor.configure(wrap=WORD)
        self.RatingChatColor.configure(state=DISABLED)


global val, w, root, top, s, HOST, PORT
root = Tk()
root.resizable(width=FALSE, height=FALSE)
top = PyChat_Mood_Detector (root)
w = None
messageScore, chatScore = 0, 0

PORT = 8011
s = socket(AF_INET, SOCK_STREAM)
HOST = gethostbyname(gethostname())



GetConnected()
thread = Thread(target = StartReceiving, args = ())
thread.daemon  = True
thread.start()
root.mainloop()

# ReceiveDataThread = threading.Thread(target=ReceiveData, args=[])
# RunMainLoopThread = threading.Thread(target=runMainLoop, args=[])
# ReceiveDataThread.start()
# RunMainLoopThread.start()

# root.after(1000,Thread(target = ReceiveData(), args = ()).start())
# root.mainloop()





# if __name__ == '__main__':
#     vp_start_gui()


