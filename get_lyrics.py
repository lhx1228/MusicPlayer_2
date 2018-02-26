from bs4 import BeautifulSoup
from tkinter import *
import requests,re,sys

def get_lyrics():

    songID = sys.argv[1]
    #print(songID)

    res = requests.get('http://www.qqmusic.cc/gequlianjie/{}.html'.format(songID))

    #res = requests.get('http://www.qqmusic.cc/gequlianjie/212130609.html')

    soup = BeautifulSoup(res.content,'lxml')

    geci = soup.select('.play_word')

    #geci = geci[0].replace('<br/>','\n')

    geci = str(geci[0])

    geci = geci.replace('<br/>','\n')

    re_res = re.compile('歌词来源：www.qqmusic.cc([^<]*)')

    result = re_res.search(geci)

    with open('lyrics.txt','w') as file:
        file.write(result.group(1))

    
if __name__ == "__main__":
    get_lyrics()
