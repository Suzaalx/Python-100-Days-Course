from bs4 import BeautifulSoup
import requests


response=requests.get("https://news.ycombinator.com/news")

yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")

print(soup.title)

# print(soup.find(name="span",class_="titlelink").getText())

title=[]
upvote=[]
link=[]
for new in soup.find_all(name="span",class_="titleline"):
    title.append(new.getText())
    link.append(new.find(name="a")["href"])

for new in soup.find_all(name="span",class_="subline"):
    if new.find(name="span",class_="score") is None:
        upvote.append(0)
    else:
        upvote.append(new.find(name="span",class_="score").getText())
    
   
print(len(title))
print(len(upvote))


for i in range(len(upvote)):
    print(title[i])
    print(upvote[i])
    print(link[i])
    print("_________________________________________________")