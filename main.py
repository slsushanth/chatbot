#imports
from datetime import datetime
import webbrowser
import tkinter
from tkinter import filedialog
from tkinter import messagebox
import keyboard
import speech_recognition
from pynput.keyboard import Controller,Key
import pyttsx3
import cv2
import wikipedia
import pywhatkit
import pyjokes
import os
import socket
import  threading
import pandas as pd


def poweroff ():
     try:
        conform = messagebox.askquestion("poweroff", "Are you sure?")
        if conform =='no':
            conform.quit()
        else:
            conform == True

        engine = pyttsx3.init()
        text = 'vca is signing off'
        engine.say(text)
        engine.runAndWait()

        os.system("shutdown now -h")
     except:
         engine = pyttsx3.init()
         text = 'command not found'
         engine.say(text)
         engine.runAndWait()
         messagebox.showerror("command", "something went wrong")

def restart ():

    try:
        conform = messagebox.askquestion("restarting", "Are you sure?")
        if conform == 'no':
            conform.quit()
        else:
            conform == True

        engine = pyttsx3.init()
        text = 'restarting'
        engine.say(text)
        engine.runAndWait()

        os.system('systemctl reboot -i')
    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def calculater():
    try:
        engine = pyttsx3.init()
        text = 'opening calculator'
        engine.say(text)
        engine.runAndWait()

        open = os.system('/usr/bin/python3.9 /home/sushanth/PycharmProjects/myproject/calculator.py')

    except FileNotFoundError:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def games ():
     try:
        engine = pyttsx3.init()
        text = 'opening snake game'
        engine.say(text)
        engine.runAndWait()

        open =os.system('/usr/bin/python3.9 /home/sushanth/PycharmProjects/myproject/snakegame.py')
     except:
         engine = pyttsx3.init()
         text = 'command not found'
         engine.say(text)
         engine.runAndWait()
         messagebox.showerror("command", "something went wrong")

def instagram():

    try:
        engine = pyttsx3.init()
        text = 'opening instagram'
        engine.say(text)
        engine.runAndWait()


        open = webbrowser.open('www.instagram.com')
    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()

        messagebox.showerror("command", "something went wrong")

def google():
    try:
        engine = pyttsx3.init()
        text = 'opening google'
        engine.say(text)
        engine.runAndWait()

        webbrowser.open('www.google.com')
    except:

        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def youtube():

    try:
        engine = pyttsx3.init()
        text = 'opening youtube'
        engine.say(text)
        engine.runAndWait()

        open = webbrowser.open('www.youtube.com')
    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def telagram():

    try:
        engine = pyttsx3.init()
        text = 'opening telagram'
        engine.say(text)
        engine.runAndWait()

        open = webbrowser.open('https://web.telegram.org/k/')
    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")


def twitter():

     try:
        engine = pyttsx3.init()
        text = 'opening twitter'
        engine.say(text)
        engine.runAndWait()

        open = webbrowser.open('www.twitter.com')
     except:
         engine = pyttsx3.init()
         text = 'command not found'
         engine.say(text)
         engine.runAndWait()
         messagebox.showerror("command", "something went wrong")

def whatsapp ():

     try:
        engine = pyttsx3.init()
        text = 'opening whatsapp'
        engine.say(text)
        engine.runAndWait()

        os.system('whatsie')

     except:
         engine = pyttsx3.init()
         text = 'command not found'
         engine.say(text)
         engine.runAndWait()
         messagebox.showerror("command", "something went wrong")


def chatgpt():
    try:
        engine = pyttsx3.init()
        text = 'opening chatgpt'
        engine.say(text)
        engine.runAndWait()

        webbrowser.open('https://chat.openai.com/chat')

    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")
def stockmarket():
    try:
        engine = pyttsx3.init()
        text = 'opening stock market, good day to invest in stocks'
        engine.say(text)
        engine.runAndWait()

        webbrowser.open('www.moneycontrol.com')
    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def pycharm():
    try:
        engine = pyttsx3.init()
        text = 'opening pycharm'
        engine.say(text)
        engine.runAndWait()

        python =os.system('/snap/pycharm-community/252/bin/pycharm.sh')
        messagebox.showinfo("info", "successfully opened")

    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def camara():
    try:
        engine = pyttsx3.init()
        text = 'opening camara'
        engine.say(text)
        engine.runAndWait()


        vid = cv2.VideoCapture(0)

        while True:
            ret, frame = vid.read()
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

        vid.release()
        cv2.destroyAllWindows()
    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def datahistory(searchentrybutton):

    with open('data.csv','r+') as f :
        mydatalist = f.readlines()
        searchlist = []

        for line in mydatalist :
            entry = line.split(',')
            searchlist.append(entry[0])
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
        f.writelines(f'\n{searchentrybutton},{dtstring}')

def speechrecognition():

    recognizer = speech_recognition.Recognizer()
    print('listning...')
    engine = pyttsx3.init()
    text = 'listning...'
    engine.say(text)
    engine.runAndWait()
    while True:
        try:

            with  speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                datahistory(text)
                print(text)


                if 'open notepad' in text:
                    notepad()
                elif 'open google' in text:
                    google()
                elif 'open instagram' in text:
                    instagram()
                elif 'open snakegame' in text:
                    games()
                elif 'power off the computer' in text:
                    poweroff()
                elif 'restart the computer' in text:
                    restart()
                elif 'open youtube' in text:
                    youtube()
                elif 'open telagram' in text:
                    telagram()
                elif 'open twitter' in text:
                    twitter()
                elif 'open whatsapp' in text:
                    whatsapp()
                elif 'open stockmarket'in text:
                    stockmarket()
                elif 'open python' in text:
                    pycharm()
                elif 'open camera' in text:
                    camara()
                elif 'open blender' in text:
                    blender()
                elif 'open remote desktop' in text:
                    remotedesktop()
                elif 'open files' in text:
                    files()
                elif 'open terminal' in text:
                    terminalhot()
                elif 'open calculator' in text:
                    calculater()
                elif 'in wikipedia' in text:
                    try:
                        serach = text.replace('in wikipedia', '')
                        wiki = wikipedia.summary(serach, 5)
                        stuff = wiki

                        top = tkinter.Toplevel()
                        top.geometry('700x400')
                        top.title(serach)

                        text = tkinter.Text(top, height=45, width=120, font=("Helvetica", "16"), bg='black', fg='white')
                        text.pack()
                        text.insert(tkinter.END, stuff)

                        def wikipeedia():

                            webbrowser.open('https://en.wikipedia.org/wiki/%s' % serach)

                        wikibutton = tkinter.Button(top, text='readmore', command=wikipeedia, bg='black', fg='white')
                        wikibutton.place(relx=0.85, rely=0.85)

                        engine = pyttsx3.init()
                        speech = 'searching about %s' % serach
                        engine.say(speech)
                        engine.runAndWait()
                    except:
                        engine = pyttsx3.init()
                        text = 'command not found'
                        engine.say(text)
                        engine.runAndWait()
                        messagebox.showerror("command", "command not found")
                elif 'open weather' in text:
                    try:
                        engine = pyttsx3.init()
                        text = 'opening weather application'
                        engine.say(text)
                        engine.runAndWait()
                        serach = text.replace('weather', '')
                        open = os.system('/usr/bin/python3.9 /home/sushanth/PycharmProjects/myproject/weather.py')

                    except:
                        engine = pyttsx3.init()
                        text = 'command not found'
                        engine.say(text)
                        engine.runAndWait()
                        messagebox.showerror("command", "command not found")
                elif 'in search' in text:
                    try:
                        serach = text.replace('in search', '')
                        pywhatkit.search(serach)
                        engine = pyttsx3.init()
                        text = ('searching about', serach)
                        engine.say(text)
                        engine.runAndWait()
                    except:
                        engine = pyttsx3.init()
                        text = 'command not found'
                        engine.say(text)
                        engine.runAndWait()
                        messagebox.showerror("command", "command not found")

                elif "what's time now" in text:
                    try:
                        time = datetime.now().strftime('%I:%M:%P')
                        print(time)
                        currenttime = time.replace(':', ' ')
                        engine = pyttsx3.init()
                        text = 'the current time is', currenttime
                        engine.say(text)
                        engine.runAndWait()
                        mess = messagebox.showinfo("time", "the current time is %s" % time)
                        thread = threading.Thread(args=time, )
                        thread.start()

                    except:
                        engine = pyttsx3.init()
                        text = 'command not found'
                        engine.say(text)
                        engine.runAndWait()
                        messagebox.showerror("command", "command not found")

                else:
                    engine = pyttsx3.init()
                    speech = text,'is not found'
                    engine.say(speech)
                    engine.runAndWait()
                    messagebox.showerror("error", f"{text} is not found \nPlease speek again")

        except:

            recognizer = speech_recognition.Recognizer()
            continue

def searchentry(searchentrybutton, server):

    serach = searchentrybutton.get()
    datahistory(serach)

    if '.com'in serach :
        engine = pyttsx3.init()
        text = 'opening', serach
        engine.say(text)
        engine.runAndWait()
        webbrowser.open('www.%s'%serach)

    elif 'camara' in serach:
        camara()
    elif 'chatgpt' in serach:
        chatgpt()
    elif 'snake game'in serach:
        games()
    elif 'pycharm' in serach:
        pycharm()
    elif 'whatsapp'in serach:
        whatsapp()
    elif 'google' in serach:
        google()
    elif 'text files' in serach:
        files()
    elif 'stock market' in serach:
        stockmarket()
    elif 'blender' in serach:
        blender()
    elif 'power off' in serach:
        poweroff()
    elif 'restart' in serach:
        restart()
    elif 'instagram'in serach:
        instagram()
    elif 'twitter' in serach:
        twitter()
    elif 'telagram'in serach:
        telagram()
    elif 'youtube'in serach:
        youtube()

    elif 'calculator' in serach:
        calculater()

    elif '.org' in serach:
        engine = pyttsx3.init()
        text = 'opening', serach
        engine.say(text)
        engine.runAndWait()
        webbrowser.open('www.%s' % serach)

    elif'.wiki' in serach:
        try:
            serach = serach.replace('.wiki', '')
            wiki = wikipedia.summary(serach, 5)
            stuff = wiki

            top = tkinter.Toplevel()
            top.geometry('700x400')
            top.title(serach)

            text= tkinter.Text(top,height=45,width=120,font=("Helvetica", "16"),bg='black',fg='white')
            text.pack()
            text.insert(tkinter.END,stuff)

            def wikipeedia():

                webbrowser.open('https://en.wikipedia.org/wiki/%s'%serach)

            wikibutton = tkinter.Button(top,text='readmore',command=wikipeedia,bg='black',fg='white')
            wikibutton.place(relx=0.85,rely=0.85)

            engine = pyttsx3.init()
            speech = 'searching about %s'%serach
            engine.say(speech)
            engine.runAndWait()
        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

    elif 'tell me a joke' in serach:
        try:
            joke = pyjokes.get_joke()
            print(joke)
            mess =messagebox.showinfo("jokes", joke)
            engine = pyttsx3.init()
            text = 'i know its a, bad joke'
            engine.say(text)
            engine.runAndWait()

            threading.Thread(target=(mess,engine))

        except:

            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

    elif 'database' in serach:
        try:
            engine = pyttsx3.init()
            text = 'opening database'
            engine.say(text)
            engine.runAndWait()

            os.system('libreoffice-calc')
        except:

            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

    elif '.yt' in serach:
        try:
            serach = serach.replace('.yt','')
            pywhatkit.playonyt(serach)
            engine = pyttsx3.init()
            text = 'playing',serach
            engine.say(text)
            engine.runAndWait()

        except:

            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

    elif 'notepad' in serach:

        try:
            engine = pyttsx3.init()
            text = 'opening notepad'
            engine.say(text)
            engine.runAndWait()
            os.system('gnome-text-editor')

        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()

    elif '.search' in serach:
         try:
            serach= serach.replace('.search','')
            pywhatkit.search(serach)

            engine = pyttsx3.init()
            text = ('searching about',serach)
            engine.say(text)
            engine.runAndWait()
         except:
             engine = pyttsx3.init()
             text = 'command not found'
             engine.say(text)
             engine.runAndWait()
             messagebox.showerror("command", "command not found")

    elif 'remmina' in serach:

        try:
            engine = pyttsx3.init()
            text = 'opening remmina'
            engine.say(text)
            engine.runAndWait()
            os.system("remmina")
        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

    elif 'terminal' in serach:

        try:
            engine = pyttsx3.init()
            text = 'opening terminal'
            engine.say(text)
            engine.runAndWait()
            os.system("gnome-terminal -e 'bash -c \"sudo apt-get ; exec bash\"'")
        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

    elif 'weather' in serach:

        try:
            engine = pyttsx3.init()
            text = 'opening weather application'
            engine.say(text)
            engine.runAndWait()
            serach = serach.replace('weather','')
            open =os.system('/usr/bin/python3.9 /home/sushanth/PycharmProjects/myproject/weather.py')

        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

    elif 'time' in serach:
        try:
            time = datetime.now().strftime('%I:%M:%P')
            print(time)
            currenttime = time.replace(':',' ')
            engine = pyttsx3.init()
            text = 'the current time is',currenttime
            engine.say(text)
            engine.runAndWait()
            mess = messagebox.showinfo("time", "the current time is %s"%time)
            thread = threading.Thread(args=time,)
            thread.start()


        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")
    else:

        print('invalid command')
        engine = pyttsx3.init()
        text = 'invalid command'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "command not found")

def remotedesktop():
    try:
        engine = pyttsx3.init()
        text = 'opening remmina'
        engine.say(text)
        engine.runAndWait()
        os.system("remmina")
    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "command not found")


def notepad():
        try:
            engine = pyttsx3.init()
            text = 'opening notepad'
            engine.say(text)
            engine.runAndWait()
            os.system('gnome-text-editor')

        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()


def blender ():
    try:
        engine = pyttsx3.init()
        text = 'opening blender'
        engine.say(text)
        engine.runAndWait()
        os.system('blender')


    except:

        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "something went wrong")

def files ():
    try:

        engine = pyttsx3.init()
        text = 'opening files'
        engine.say(text)
        engine.runAndWait()

        root.filename = filedialog.askopenfilename(title='select for files',
                                                   filetypes=(('png files', '*.png'), ('all files', '*.*')))


        text_file= open(root.filename,'r')
        stuff = text_file.read()

        text_file.close()
        top = tkinter.Toplevel()
        top.title('file')
        top.resizable(False,False)
        text = tkinter.Text(top, width=80, height=30,bg='black',fg='white')
        text.pack()
        text.insert(tkinter.END, stuff)

    except:
        engine = pyttsx3.init()
        text = 'command not found'
        engine.say(text)
        engine.runAndWait()
        messagebox.showerror("command", "command not found")

def terminalhot():

        try:
            engine = pyttsx3.init()
            text = 'opening terminal'
            engine.say(text)
            engine.runAndWait()
            os.system("gnome-terminal -e 'bash -c \"sudo apt-get ; exec bash\"'")
        except:
            engine = pyttsx3.init()
            text = 'command not found'
            engine.say(text)
            engine.runAndWait()
            messagebox.showerror("command", "command not found")

def userinterface():

    root = tkinter.Tk()


    root.geometry('600x500')
    root.title('VC Assistant')
    root.resizable(False,False)
    C = tkinter.Canvas(root, bg="blue", height=250, width=300)
    filename = tkinter.PhotoImage(file = "background vca1.png")
    background_label = tkinter.Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    C.pack()

    #hotkeys

    root.bind('<Return>',lambda event:threading.Thread(target=searchentry(searchentrybutton,server)).start())
    root.bind('<Control-f>',lambda event:threading.Thread(target=files).start())
    root.bind('<Tab>',lambda event:threading.Thread(target=speechrecognition).start())
    root.bind('<Control-i>',lambda event:threading.Thread(target=instagram).start())
    root.bind('<Control-c>',lambda event:threading.Thread(target=camara).start())
    root.bind('<Control-g>',lambda event:threading.Thread(target=google).start())
    root.bind('<Control-w>',lambda event:threading.Thread(target=whatsapp).start())
    root.bind('<Control-t>',lambda event:threading.Thread(target=terminalhot).start())
    root.bind('<Control-y>',lambda event:threading.Thread(target=youtube).start())
    root.bind('<Control-l>',lambda event:threading.Thread(target=calculater).start())
    root.bind('<Control-s>',lambda event:threading.Thread(target=games).start())
    root.bind('<Control-p>',lambda event:threading.Thread(target=poweroff()).start())
    root.bind('<Control-r>',lambda event:threading.Thread(target=restart()).start())
    root.bind('<Control-b>',lambda event:threading.Thread(target=blender).start())
    root.bind('<Control-m>',lambda event:threading.Thread(target=pycharm).start())
    root.bind('<Control-e>',lambda event:threading.Thread(target=telagram).start())
    root.bind('<Control-n>',lambda event:threading.Thread(target=notepad).start())

    instabutton = tkinter.Button(root,text='instagram',command=lambda :threading.Thread(target=instagram).start()
                                 ,bg='sky blue',height= 1,width=8)
    instabutton.place(relx=0.1,rely=0.5)

    cambutton =  tkinter.Button(root,text='camara',command=lambda :threading.Thread(target=camara).start()
                                ,bg='sky blue',height= 1,width=8)
    cambutton.place(relx=0.3,rely=0.5)

    telegrambutton = tkinter.Button(root,text='telegram',command=lambda:threading.Thread(target=telagram).start()
                                    ,bg='sky blue',height=1,width=8)
    telegrambutton.place(relx=0.7,rely=0.7)

    searchentrybutton = tkinter.Entry(root,width=23,font=("Helvetica", "20"))
    searchentrybutton.place(relx=0.1,rely=0.4)

    #speechrecognitionbutton = tkinter.Button(root,text='!',height=1,width=1
     #                                        ,command=lambda :threading.Thread(target=speechrecognition).start())
    #speechrecognitionbutton.place(relx=0.63,rely=0.4)

    commandbutton = tkinter.Button(root,text='command',height=1,width=10
                                   ,command=lambda :threading.Thread(target=searchentry(searchentrybutton,server)).start())
    commandbutton.place(relx=0.7,rely=0.4)

    goobutton = tkinter.Button(root,text='  google  ',command=lambda:threading.Thread(target=google).start()
                               ,bg='skyblue',height= 1,width=8)
    goobutton.place(relx=0.1,rely=0.6)

    snakebutton = tkinter.Button(root,text='snake game',command=lambda:threading.Thread(target=games).start()
                                 ,bg= 'skyblue',height= 1,width=8)
    snakebutton.place(relx=0.3,rely=0.7)

    calculatorbutton = tkinter.Button(root,text='calculator',command=lambda:threading.Thread(target=calculater).start()
                                      ,bg='skyblue',height= 1,width=8)
    calculatorbutton.place(relx=0.1,rely=0.7)

    powerbutton = tkinter.Button(root,text='power off',command=lambda:threading.Thread(target=poweroff).start()
                                 ,bg='red',height= 1,width=8)
    powerbutton.place(relx=0.01,rely=0.9)

    restartbutton = tkinter.Button(root,text='restart',command=lambda:threading.Thread(target=restart).start()
                                   ,bg='red',height= 1,width=8)
    restartbutton.place(relx=0.83,rely=0.9)

    filebutton = tkinter.Button(root, text='text files', command=lambda :threading.Thread(target=files).start()
                                , bg='skyblue',height= 1,width=8)
    filebutton.place(relx=0.7, rely=0.6)

    pycharmbutton = tkinter.Button(root,text='pycharm',command=lambda:threading.Thread(target=pycharm).start()
                                   ,bg='skyblue',height= 1,width=8)
    pycharmbutton.place(relx=0.5,rely=0.7)

    youbutton = tkinter.Button(root,text='youtube',command=lambda:threading.Thread(target=youtube).start()
                               ,bg='skyblue',height= 1,width=8)
    youbutton.place(relx=0.3,rely=0.6)

    twitterbutton = tkinter.Button(root,text='twitter',command=lambda :threading.Thread(target=twitter).start()
                                   ,bg='skyblue',height= 1,width=8)
    twitterbutton.place(relx=0.5,rely=0.6)

    #weblable = tkinter.Label(root,text='click this button for instagram')
    #weblable.place(relx=0.1,rely=0.3)
    #camlable = tkinter.Label(root,text='click this button for camara\n(q-quit)')
    #camlable.place(relx=0.5,rely=0.3)

    whatsappbutton = tkinter.Button(root,text='whatsapp',command=lambda :threading.Thread(target=whatsapp).start()
                                    ,bg='sky blue',height= 1,width=8)

    whatsappbutton.place(relx=0.5,rely=0.5)

    blenderbutton = tkinter.Button(root,text='blender',command=lambda:threading.Thread(target=blender).start()
                                   , bg='sky blue',height= 1,width=8)
    blenderbutton.place(relx=0.7,rely=0.5)

    tittle = tkinter.Label(root,text= 'VCA',font=("Helvetica", "35"),bg='skyblue')
    tittle.place(relx=0.42,rely=0.01)


    root.mainloop()

def voice():
    engine = pyttsx3.init()
    text = 'Hello iam VCA, i am your voice command assistant '
    engine.say(text)
    engine.runAndWait()

def server():
    try:
        headder = 64
        port = 5050
        root = socket.gethostbyname(socket.gethostname())
        addr = (root,port)
        format = 'utf-8'
        disconnect_message = 'disconnect'

        root = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        root.bind(addr)

        def handle_client(conn,addr):
            print(f'[active connection]{addr} connected')
            messagebox.showinfo('New Connection',f'{addr} has been connected to the server')
            connected = True
            while connected:
                msg_length = conn.recv(headder).decode(format)
                if msg_length:
                   msg_length = int(msg_length)
                   msg_length = conn.recv(msg_length).decode(format)
                   if msg_length == disconnect_message:
                      connected = False
                   print(f'[{addr}] {msg_length}')
            conn.close()

        def start():
            root.listen()
            print(f'[listing] serer is listing on {root}')
            while True:
               conn,addr =root.accept()
               thread =threading.Thread(target=handle_client,args= (conn,addr))
               thread.start()
               print(f'[active connection]{threading.activeCount() -1}')

        print('server started')
        start()

    except:
        print('server did not connected')




userinterfacethread = threading.Thread(target=userinterface)
serverthread = threading.Thread(target=server)
voicethread = threading.Thread(target=voice)

voicethread.start()
userinterfacethread.start()
serverthread.start()

userinterfacethread.join()
serverthread.join()
voicethread.join()
