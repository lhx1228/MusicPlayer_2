from subprocess import run
import requests,json,sys,os

songName = sys.argv[1]

#print('running get_songID.py')

#master.quit()

res = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=37602803789127241&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'.format(songName))

d = res.json()

songID = d['data']['song']['list'][0]['id']

#print(songID,songName)

run('python C:/Users/Lhx/Desktop/Python/MusicPlayer/版本2.0/get_MusicUrl.py {} {}'.format(songID,songName),shell=True)
