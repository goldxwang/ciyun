#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#原文：https://blog.csdn.net/qq_30262201/article/details/78801367

'''
wordcloud包的基本用法：
 class wordcloud.WordCloud(font_path=None, width=400, height=200, margin=2, ranks_only=None, prefer_horizontal=0.9,mask=None, scale=1, color_func=None, max_words=200,min_font_size=4,stopwords=None,random_state=None,background_color='black', max_font_size=None, font_step=1, mode='RGB', relative_scaling=0.5, regexp=None, collocations=True,colormap=None, normalize_plurals=True)

wordcloud的所有参数:
font_path : string  //字体路径，需要展现什么字体就把该字体路径+后缀名写上，如：font_path = '黑体.ttf'
width : int (default=400)  //输出的画布宽度，默认为400像素
height : int (default=200)  //输出的画布高度，默认为200像素
prefer_horizontal : float (default=0.90) //词语水平方向排版出现的频率，默认 0.9 （所以词语垂直方向排版出现频率为 0.1 ）
mask : nd-array or None (default=None) //如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮罩形状被 mask 取代。除全白（#FFFFFF）的部分将不会绘制，其余部分会用于绘制词云。如：bg_pic = imread('读取一张图片.png')，背景图片的画布一定要设置为白色（#FFFFFF），然后显示的形状为不是白色的其他颜色。可以用ps工具将自己要显示的形状复制到一个纯白色的画布上再保存，就ok了。
scale : float (default=1) //按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍。
min_font_size : int (default=4) //显示的最小的字体大小
font_step : int (default=1) //字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差。
max_words : number (default=200) //要显示的词的最大个数
stopwords : set of strings or None //设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
background_color : color value (default=”black”) //背景颜色，如background_color='white',背景颜色为白色。
max_font_size : int or None (default=None) //显示的最大的字体大小
mode : string (default=”RGB”) //当参数为“RGBA”并且background_color不为空时，背景为透明。
relative_scaling : float (default=.5) //词频和字体大小的关联性
color_func : callable, default=None //生成新颜色的函数，如果为空，则使用 self.color_func
regexp : string or None (optional) //使用正则表达式分隔输入的文本
collocations : bool, default=True //是否包括两个词的搭配
colormap : string or matplotlib colormap, default=”viridis” //给每个单词随机分配颜色，若指定color_func，则忽略该方法。
fit_words(frequencies) //根据词频生成词云
generate(text) //根据文本生成词云
generate_from_frequencies(frequencies[, ...]) //根据词频生成词云
generate_from_text(text) //根据文本生成词云
process_text(text) //将长文本分词并去除屏蔽词（此处指英语，中文分词还是需要自己用别的库先行实现，使用上面的 fit_words(frequencies) ）
recolor([random_state, color_func, colormap]) //对现有输出重新着色。重新上色会比重新生成整个词云快很多。
to_array() //转化为 numpy array
to_file(filename) //输出到文件
'''
"""
# 导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
# 读取一个txt文件
text = open('test1.txt','r').read()
# 读入背景图片
bg_pic = imread('3.png')
# 生成词云
wordcloud = WordCloud(mask=bg_pic,background_color='white',scale=1.5).generate(text)
# image_colors = ImageColorGenerator(bg_pic)
# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
"""
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
from scipy.misc import imread

#1.1 读取本地文本和背景图片
d = path.dirname(__file__)
text = open(path.join(d, 'alice.txt')).read()   # 读取整个文本.
alice_pic= np.array(Image.open(path.join(d, "alice_mask.png"))) #读取图片

#1.2 直接读取一个txt文件和背景图片
text_1 = open('text_1.txt','r').read()  # 读取一个txt文件
text_pic = imread('text_mask.png') # 读入背景图片

#2 设置停用词典
stopwords = set(STOPWORDS)
stopwords.add("said")

#3.1 设置词云的一些属性及生成词云
wc = WordCloud(background_color="white", max_words=2000, mask=alice_pic,stopwords=stopwords)#设置词云的一些属性
wc.generate(text) #生成词云

#3.2 生成词云
wc01 = WordCloud(background_color='white',mask=text_pic,scale=1.5).generate(text_1)
image_colors = ImageColorGenerator(text_pic) #取背景图颜色

#4.1 保存到本地
wc.to_file(path.join(d, "alice.png"))

#4.2 保存到本地
wc01.to_file(path.join(d, "text_1.png"))

#5.1 显示词云图片
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()

#5.2 显示词云图片
#plt.imshow(wc01)
plt.imshow(wc01.recolor(color_func=image_colors))
plt.axis('off')
plt.show()

