import tkinter
import os
import pygame
from subprocess import run
from tkinter import *
from tkinter import filedialog
from pygame import *

flag = 0
ly_flag = 0
textLyric = ''
e1 = ''


def MP3towav():
    run('ffmpeg -i "{}.mp3" "{}.wav"'.format(e1.get(), e1.get()), shell=True)

    run('attrib "{}.wav" +s +h'.format(e1.get()), shell=True)

    os.remove('{}.mp3'.format(e1.get()))
    playMusic()
    adjust()


def run_songID():
    global ly_flag
    ly_flag = 1
    # print(e1.get())
    run('python C:/Users/Lhx/Desktop/Python/MusicPlayer/版本2.0/get_songID.py {}'.format(e1.get()), shell=True)
    if os.path.exists('{}.wav'.format(e1.get())):
        playMusic()
    else:
        MP3towav()


def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load('{}.wav'.format(e1.get()))
    pygame.mixer.music.play()


def pause_music():
    global flag
    if flag == 0:
        pygame.mixer.music.pause()
        flag = 1
    elif flag == 1:
        pygame.mixer.music.unpause()
        flag = 0


def Input_songName():
    global e1
    frame = tkinter.Frame(master)
    frame.pack(side=tkinter.LEFT, fill=tkinter.Y)
    lv = tkinter.StringVar()
    listBox = tkinter.Listbox(frame, selectmode=tkinter.BROWSE,
                              width=30, height=30, bg="#FFFFFF", listvariable=lv)
    listBox.pack()
    e1 = Entry(frame, bg='#FFFFFF')
    # e1.grid()
    e1.place(x=50, y=150)
    songName = e1.get()
    tkinter.Label(master, text="搜索", fg='#000000',
                  bg="#FFFFFF").place(x=10, y=148)
    Button(master, text='播放', command=run_songID).place(x=50, y=180)
    Button(master, text='暂停', command=pause_music).place(x=140, y=180)
    # adjust()


def adjust():
    if ly_flag == 0:
        lyrics = '''
        \n\n\n\n\n\n\n\n                    使用说明：
                            如果想要在线播放音乐，请在
                        左侧输入框中输入歌名,点击播放.
                        如果想播放本地音乐,请点击左上
                        角的文件浏览文件播放(仅限.wav)

        '''
    elif ly_flag == 1:
        with open('C:/Users/Lhx/Desktop/Python/MusicPlayer/版本2.0/lyrics.txt', 'r') as file:
            lyrics_text = file.read()
        lyrics = '''
        {}
        '''.format(lyrics_text)
        textLyric.delete(0.0, END)  # Text清空

    textLyric.insert(END, lyrics)


def Init():
    global textLyric
    frame = tkinter.Frame(master)
    frame.pack(side=tkinter.TOP, fill=tkinter.Y)
    S = tkinter.Scrollbar(frame)
    textLyric = tkinter.Text(frame, bg="#FFFFFF", height=50)
    S.pack(side=RIGHT, fill=Y)
    textLyric.pack(side=LEFT, fill=Y)
    S.config(command=textLyric.yview)
    textLyric.config(yscrollcommand=S.set)
    adjust()
    menu()


def print_lyrics():
    frame = tkinter.Frame(master)
    frame.pack(side=tkinter.TOP, fill=tkinter.Y)
    S = tkinter.Scrollbar(frame)
    textLyric = tkinter.Text(frame, bg="#FFFFFF", height=50)
    S.pack(side=RIGHT, fill=Y)
    textLyric.pack(side=LEFT, fill=Y)
    S.config(command=textLyric.yview)
    textLyric.config(yscrollcommand=S.set)
    with open('C:/Users/Lhx/Desktop/Python/MusicPlayer/版本2.0/lyrics.txt', 'r') as file:
        lyrics_text = file.read()
    lyrics = '''
    {}
    '''.format(lyrics_text)

    textLyric.insert(END, lyrics)


def OpenFile():
    f = filedialog.askopenfilename(title='打开文件', filetypes=[
                                   ('Music', '*.wav'), ('All Files', '*')])
    # print(f)
    pygame.mixer.init()
    pygame.mixer.music.load('{}'.format(f))
    pygame.mixer.music.play()


def menu():
    menubar = Menu(master)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=OpenFile)
    # filemenu.add_separator()#分割线
    menubar.add_cascade(label="File", menu=filemenu)
    master.config(menu=menubar)

    # mainloop()


if __name__ == '__main__':
    os.chdir('C:/Users/Lhx/Desktop/Python/MusicPlayer/版本2.0/')
    try:
        run('attrib *.wav -s -h', shell=True)
        run('del *.wav', shell=True)
    except:
        pass
    master = tkinter.Tk()
    master.title('Music Player')
    master.geometry("700x500+200+100")
    Input_songName()
    Init()
    master.mainloop()
