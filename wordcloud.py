from wordcloud import STOPWORDS,WordCloud
import numpy as np
import wikipedia as wp
from PIL import Image
import sys
data = input("enter the topic on which you want to generate wordcloud : ")

title = wp.search(data)[0]
page = wp.page(title)
text=page.content

stop = set(STOPWORDS)
back = np.array(Image.open("indiamask.png"))   #indiamask is the background image for making the wordcloud. you can also use other image also.
wc = WordCloud(background_color="white",mask=back,stopwords=stop,max_words=200)

wc.generate(text)
wc.to_file("indiaarmed.png")  #indiaarmed is the output file name.you can give other name for output file also. 