import AutoSummary as ausu
content = 'D:/python/news_1.txt'

with open (content,'r',encoding = 'utf-8') as f:
    text = f.read()


stops=[]
with open('D:/python/stopword_test.txt','r',encoding ='utf-8') as f:
    for line in f.readlines():
        stops.append(line.strip())

sentences,indexs = ausu.split_sentence(text)
tfidf = ausu.get_tfidf_matrix(sentences,stops)
word_weight = ausu.get_sentence_with_words_weight(tfidf)
posi_weight = ausu.get_sentence_with_position_weight(sentences)

scores=ausu.get_similarity_weight(tfidf)
sort_weight =ausu.ranking_base_on_weigth(word_weight,posi_weight,scores,feature_weight=[1,1,1])
summer=ausu.get_summarization(indexs,sort_weight,topK_ratio=0.1)

print('原文:\n',text)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('摘要:\n',summer)
