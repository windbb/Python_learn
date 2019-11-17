import jieba

jieba.set_dictionary('D:/python/dict.txt.big.txt')
jieba.load_userdict('D:/python/user_dict_test.txt')
with open('D:/python/stopword_test.txt','r',encoding='utf-8-sig') as f:
    stops=f.read().split('\n')
#sentence = '我今天要到台北松山機場出差!'

sentence = '今天是元旦，總統蔡英文發表了元旦文告。'

breakword= jieba.cut(sentence,cut_all=False)
words =[]
for word in breakword:
    if word not in stops:
        words.append(word)
print('|'.join(words))

#print('精準模式:'+ '|'.join(breakword))

#breakword = jieba.cut(sentence,cut_all=True)
#print('全文模式:'+ '|'.join(breakword))

#breakword = jieba.cut_for_search(sentence)
#print('搜尋引擎模式:'+ '|'.join(breakword))
