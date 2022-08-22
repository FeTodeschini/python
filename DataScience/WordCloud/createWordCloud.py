#this program creates a wordcloud based on the worldcloud.txt file
import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud, STOPWORDS

def getWikiContent(queryString):
    title = wikipedia.search(queryString)[0]
    page = wikipedia.page(title)
    return page.content

querystring = "global warming" 
text = getWikiContent(querystring)
stopwords = STOPWORDS

wc = WordCloud(
    background_color = 'white'
    , stopwords = stopwords
    , max_words=150
    , height = 700
    , width = 500
)

wc.generate(text)

wc.to_file('wordcloud.png')