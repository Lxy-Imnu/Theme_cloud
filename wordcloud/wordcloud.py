from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import jieba

def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result;

with open("dome.txt",encoding='utf-8') as fp:
    text = fp.read()
    # print(text)
    image = image.open("outline\\2.jpg")
    graph = np.array(image)
    wordcloud = WordCloud(
        mask=graph,
        font_path = "C:\\Windows\\Fonts\\msyh.ttc"
    ).generate(text)
    wordcloud.to_file('dome1.png')
    image_produce = wordcloud.to_image()
    image_produce.show()