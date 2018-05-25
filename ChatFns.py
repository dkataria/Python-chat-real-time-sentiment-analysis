from tkinter import *
from socket import *
import urllib
import re

__author__ = "Deep Katariya"
def GetExternalIP():
    url = "http://checkip.dyndns.org"
    request = urllib.urlopen(url).read()
    return str(re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request))

def GetInternalIP():
    return str(gethostbyname(getfqdn()))

def FilteredMessage(EntryText):
    """
    Filter out all useless white lines at the end of a string,
    returns a new, beautifully filtered string.
    """
    EndFiltered = ''
    for i in range(len(EntryText)-1,-1,-1):
        if EntryText[i]!='\n':
            EndFiltered = EntryText[0:i+1]
            break
    for i in range(0,len(EndFiltered), 1):
            if EndFiltered[i] != "\n":
                    return EndFiltered[i:]+'\n'
    return ''





def LoadConnectionInfo(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            ChatLog.insert(END, EntryText+'\n')
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

def LoadMyEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            LineNumber = float(ChatLog.index('end'))-1.0
            ChatLog.insert(END, "You: " + EntryText)
            ChatLog.tag_add("You", LineNumber, LineNumber+0.4)
            ChatLog.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


def LoadOtherEntry(ChatLog, EntryText):
    if EntryText != '':
        ChatLog.config(state=NORMAL)
        if ChatLog.index('end') != None:
            try:
                LineNumber = float(ChatLog.index('end'))-1.0
            except:
                pass
            ChatLog.insert(END, "Other: " + EntryText)
            ChatLog.tag_add("Other", LineNumber, LineNumber+0.6)
            ChatLog.tag_config("Other", foreground="#04B404", font=("Arial", 12, "bold"))
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

def SetConnectionInfo(UserStatusMessage, StatusMessage, HOST):

    UserStatusMessage.configure(state=NORMAL)
    UserStatusMessage.delete(1.0, END)
    UserStatusMessage.insert(INSERT, HOST)
    UserStatusMessage.configure(state=DISABLED)

    StatusMessage.configure(state=NORMAL)
    StatusMessage.delete(1.0, END)
    StatusMessage.insert(INSERT, 'Connected')
    StatusMessage.configure(state=DISABLED)

def UnsetConnectionInfo(UserStatusMessage, StatusMessage):

    UserStatusMessage.config(state=NORMAL)
    UserStatusMessage.delete(1.0, END)
    UserStatusMessage.insert(INSERT, 'No user')
    UserStatusMessage.configure(state=DISABLED)

    StatusMessage.config(state=NORMAL)
    StatusMessage.delete(1.0, END)
    StatusMessage.insert(INSERT, 'Disconnected')
    StatusMessage.configure(state=DISABLED)
