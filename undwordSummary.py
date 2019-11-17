import AutoSummary as ausu
import requests
from bs4 import BeautifulSoup as soup



stops=[]
with open('D:/python/stopword_test.txt','r',encoding ='utf-8') as f:
    for line in f.readlines():
        stops.append(line.strip())

urls = []
url = 'https://udn.com/news/breaknews/1'
html = requests.get(url)
sp = soup(html.text,'html.parser')
#data1 = sp.select('#breaknews d1 dt h2 a')
data1 = sp.select('#breaknews_body h2 a')
for d in data1:
    urls.append('https://udn.com' + d.get('href'))

i=1
for url in urls:
    html = requests.get(url)
    sp = soup(html.text,'html.parser')
    data1 = sp.select('#story_body_content p')
    print('處理第 {} 則新聞'.format(i))

    text=''

    for d in data1:
        if d.text.find('延伸閱讀') !=-1:
            break
        if d.text != '':
            text +=d.text
    i+=1



sentences,indexs = ausu.split_sentence(text)
tfidf = ausu.get_tfidf_matrix(sentences,stops)
word_weight = ausu.get_sentence_with_words_weight(tfidf)
posi_weight = ausu.get_sentence_with_position_weight(sentences)

scores=ausu.get_similarity_weight(tfidf)
sort_weight =ausu.ranking_base_on_weigth(word_weight,posi_weight,scores,feature_weight=[1,1,1])
summer=ausu.get_summarization(indexs,sort_weight,topK_ratio=0.3)

print(summer)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
