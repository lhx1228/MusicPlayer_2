from subprocess import run
import requests,sys,os

songID = sys.argv[1]

songName = sys.argv[2]

#print('running get_MusicURL.py')

res = requests.get('http://mp3.qqmusic.cc/yq/{}.mp3'.format(songID))

with open('{}.mp3'.format(songName),'wb') as file:
    file.write(res.content)

#print('2')
	
run('python C:/Users/Lhx/Desktop/Python/MusicPlayer/版本2.0/get_lyrics.py {}'.format(songID),shell=True)

