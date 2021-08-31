import os
import codecs
from wordcloud import WordCloud
import arabic_reshaper
from bidi.algorithm import get_display
from random import randrange

# sample : https://github.com/amueller/word_cloud/blob/master/examples/masked.py

def wordcloud_conventor(fileLocation='related_search.txt'):

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    # f = codecs.open(os.path.join(d, 'Recommended_Results.txt'), 'r', 'utf-8')
    f = codecs.open(os.path.join(d, fileLocation), 'r', 'utf-8')

    # Make text readable for a non-Arabic library like wordcloud
    text = arabic_reshaper.reshape(f.read())
    text = get_display(text)

    # Generate a word cloud image
    wordcloud = WordCloud(font_path='iran/Vazir-Light.ttf', width=1000, height=860, margin=2,max_words=1000).generate(text)

    # Export to an image
    wordcloudFileName = str(randrange(100))+".png"
    res = wordcloud.to_file(wordcloudFileName)
    return wordcloudFileName

# wordcloud_conventor()