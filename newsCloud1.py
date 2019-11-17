from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud 
import jieba
import numpy as np
from collections import Counter

text =open('D:/python/news_1.txt','r',encoding='utf-8').read()
jieba.set_dictionary('D:/python/dict.txt.big.txt')
jieba.load_userdict('D:/python/user_dict_test.txt')
with open('D:/python/stopword_test.txt','r',encoding='utf-8-sig') as f:
    stops=f.read().split('\n')

terms = []

for t in jieba.cut(text,cut_all=False):
    if t not in stops:
        terms.append(t)
        
diction = Counter(terms)

font = 'D:/python/msyh.ttc'

#wordcloud = WordCloud(font_path=font)
mask=np.array(Image.open('D:/python/heart.png'))
wordcloud = WordCloud(background_color='white',mask=mask,font_path=font)
wordcloud.generate_from_frequencies(frequencies=diction)

plt.figure(figsize=(6,6))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('news_wordcloud.png')