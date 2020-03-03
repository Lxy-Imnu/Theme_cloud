from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import jieba

jieba.load_userdict("userdict.txt")

def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result;


with open("dome.txt",'r',encoding='UTF-8') as fp:
    text = fp.read()
    text  = trans_CN(text)
    mask = np.array(image.open("outline\\6.jpg"))
    wordcloud = WordCloud(
        mask=mask,
        font_path = "C:\\Windows\\Fonts\\msyh.ttc"
    ).generate(text)
    image_produce = wordcloud.to_image()
    wordcloud.to_file('dome1.png')