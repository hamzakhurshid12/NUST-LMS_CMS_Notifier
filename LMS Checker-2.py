import requests, urllib
from bs4 import BeautifulSoup
from urllib.parse import unquote
from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
 
class WindowsBalloonTip:
    def __init__(self, title, msg):
        message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
        }
        # Register the Window class.
        wc = WNDCLASS()
        hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        classAtom = RegisterClass(wc)
        # Create the Window.
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = CreateWindow( classAtom, "Taskbar", style, \
                0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, \
                0, 0, hinst, None)
        UpdateWindow(self.hwnd)
        iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
           hicon = LoadImage(hinst, iconPathName, \
                    win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
          hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER+20, hicon, "tooltip")
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, \
                         (self.hwnd, 0, NIF_INFO, win32con.WM_USER+20,\
                          hicon, "Balloon  tooltip",title,200,msg))
        # self.show_balloon(title, msg)
        time.sleep(10)
        DestroyWindow(self.hwnd)
    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0) # Terminate the app.

def balloon_tip(title, msg):
    w=WindowsBalloonTip(msg, title)
    time.sleep(2) ##To avoid overlapping ballon-tips


session=requests.Session()
def getBsObj(url):
    params = {'username': 'hkhurshid.bese16seecs', 'password': 'potustor'}
    r = session.post("https://lms.nust.edu.pk/portal/login/index.php", params)
    se = session.get(url)
    return BeautifulSoup(se.text, "html.parser")
    
def main():
    params = {'username': 'hkhurshid.bese16seecs', 'password': 'potustor'}
    r = session.post("https://lms.nust.edu.pk/portal/login/index.php", params)
    print(r.cookies.get_dict())
    #Getting list of availabe subjects:
    allSub = session.get("https://lms.nust.edu.pk/portal/my/")
    allObj=BeautifulSoup(allSub.text, "html.parser")
    allObj=allObj.find('div',{'id':'course_list'})
    subjects_tags=allObj.findAll('h2')
    subject_names=[]
    subject_links=[]
    for subject in subjects_tags:
        subject_names.append(subject.get_text())
        subject_links.append(subject.find('a')['href'])
    return (subject_names,subject_links)

def get_teacher(contents):
    for x in contents:
        print(x)
        if "First Student Feedback" in x:
            return x[23:-1]
    return "Not Found"

def downloadFile(path, url):
    params = {'username': 'hkhurshid.bese16seecs', 'password': 'potustor'}
    r = session.post("https://lms.nust.edu.pk/portal/login/index.php", params)
    r = session.get(url, stream=True)
    if not os.path.exists(path):
        os.makedirs(path)
    name=unquote(r.url.split('/')[-1])
    name=os.path.join(path,name)
    print(name)
    if not os.path.exists(name)
        chunk_size=2000
        with open(name, 'wb+') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)
    
def addToDownloaded()


def getResource(contents, subNo):
    for x in contents:
        done=False
        #while not done: ##Trying again with help of try except
            #try: 2
        img=x.find('img')['src']
        link=x.find('a')['href']
        if '/resource/view.php' in link:
            if 'pdf-24' in img:  
                bsObj=getBsObj(link)
                dataTag=bsObj.find('object',{'id':'resourceobject'})
                print(dataTag['data'])
            else:
                if '/resource/view.php' in link:
                    print(link)
                    downloadFile(folderPath+names[subNo],link)
                #done=True
            #except:
            #    continue

def check_subject(subNo):
    params = {'username': 'hkhurshid.bese16seecs', 'password': 'potustor'}
    r = session.post("http://lms.nust.edu.pk/portal/login/index.php", params)
    print("Cookie is set to:")
    print(r.cookies.get_dict())
    print("Going to subject page...")
    #Getting Specific Course
    #for x in links:
    #    print(x)
    #    print()
    se = session.get(links[subNo])
    seObj=BeautifulSoup(se.text, "html.parser")
    allWeeksTable=seObj.find('ul',{'class':'weeks'})
    #print(allWeeksTable)
    seContent=allWeeksTable.findAll('li',{'class':'section'})
    seItems=[]
    #Adding content tags into the list
    for content in seContent:
        contents=content.findAll('li')
        for x in contents:
            seItems.append(x)
    print(names[subNo])
    contents=[]
    for x in seItems:
        try:
            #print (x.get_text())
            contents.append(x)
        except:
            continue
        #print(x.get_text())
    getResource(contents,subNo)
    #print(get_teacher(contents))

folderPath="D:\\temp"
names,links=main()
subject=1
done=False
##while not done:
##    try:
check_subject(subject)
done=True
##    except:
##        print('Error')
