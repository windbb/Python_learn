import requests
from bs4 import BeautifulSoup as soup

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud 
import jieba
import numpy as np
from collections import Counter

urls = []
url = 'https://udn.com/news/breaknews/1'
html = requests.get(url)
sp = soup(html.text,'html.parser')
#data1 = sp.select('#breaknews d1 dt h2 a')
data1 = sp.select('#breaknews_body h2 a')
for d in data1:
    urls.append('https://udn.com' + d.get('href'))
    print(len(data1))
text_news = ''
i=1

for url in urls:
    html = requests.get(url)
    sp = soup(html.text,'html.parser')
    data1 = sp.select('#story_body_content p')
    print('處理第 {} 則新聞'.format(i))
    for d in data1:
        if d.text.find('延伸閱讀') !=-1:
            break
        if d.text != '':
            text_news +=d.text
    i +=1

jieba.set_dictionary('D:/python/dict.txt.big.txt')
with open('D:/python/stopword_test.txt','r',encoding='utf-8-sig') as f:
    stops=f.read().split('\n')

terms = []
for t in jieba.cut(text_news,cut_all=False):
    if t not in stops:
        terms.append(t)

diction = Counter(terms)

font = r'D:/python/msyh.ttc'
mask=np.array(Image.open('D:/python/heart.png'))
unicloud = WordCloud(background_color='White',mask = mask,font_path=font)
unicloud.generate_from_frequencies(frequencies=diction)

plt.figure(figsize=(6,6))
plt.imshow(unicloud)
plt.axis('off')
plt.show()

unicloud.to_file('newsunicloud.png')