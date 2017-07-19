
# coding: utf-8

# In[99]:

import urllib2
import re
from bs4 import BeautifulSoup

response = urllib2.urlopen('https://www.giftcardmall.am/en/?page=1')
htmlcont = response.read()
soup = BeautifulSoup(htmlcont, "html.parser")
data = soup.find("div",  attrs={"class":"cards--four-up"})
cardsData = data.findAll("div", attrs={"class":"card_animate"})

resultData = []

for i in range(0, len(cardsData)):
    sumArray = cardsData[i].find("p", attrs={"class":"card_sum"}).findAll("span")

    cardInfo = {"name":cardsData[i].find("h4").text, "url" :cardsData[i].find("h4").find("a", href=True)['href'], sum:cardsData[i].find("p", attrs={"class":"card_sum"}).text}
    resultData.append(cardInfo)


# In[ ]:



