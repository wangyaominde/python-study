# -*- coding: utf-8 -*-
# 从test.txt中抓取所有文字，做成词云
# 2018-10-17 18:02:37
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

f = open(u'test.txt', 'r', encoding='UTF-8').read()
mytext = " ".join(jieba.cut(f))
wordcloud = WordCloud(font_path="simsun.ttf",background_color="white",max_font_size=100,max_words=2000, width=1600,
                      height=1200, margin=2).generate(mytext)


plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('test.png')
# 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存
