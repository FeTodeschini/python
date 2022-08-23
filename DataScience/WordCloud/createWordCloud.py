#this program creates a wordcloud based on the worldcloud.txt file
from turtle import isvisible
import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud, STOPWORDS

def getWikiContent(queryString):
    title = wikipedia.search(queryString)[0]
    page = wikipedia.page(title)
    return page.content

stopwords = STOPWORDS

wc = WordCloud(
    background_color = 'white'
    , stopwords = stopwords
    , max_words=150
    , height = 700
    , width = 500
)

isValidContent = False

while isValidContent != True:
    querystring = input('For which subject do you want to see a WordCloud?')
    if querystring != '':
        isValidContent = True
        
text = getWikiContent(querystring)


wc.generate(text)

#Saves WordCloud to a file in the same folder as the .py program file
wc.to_file('wordcloud.png')