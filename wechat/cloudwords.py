# -*- coding: utf-8 -*-
#从微信获取好友的签名，做成词云
#2018-10-17 18:02:37
#还没开始做
#有空写
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

f = open(u'test.txt', 'r').read()
mytext = " ".join(jieba.cut(f))
wordcloud = WordCloud(font_path="simsun.ttf",background_color="white", width=1000,
                      height=860, margin=2).generate(mytext)


plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('test.png')
# 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存
