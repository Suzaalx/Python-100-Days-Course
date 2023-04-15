from bs4 import BeautifulSoup
import requests


# response=requests.get("https://news.ycombinator.com/news")

# yc_web_page=response.text

# soup=BeautifulSoup(yc_web_page,"html.parser")

# print(soup.title)

# # print(soup.find(name="span",class_="titlelink").getText())

# title=[]
# upvote=[]
# link=[]
# for new in soup.find_all(name="span",class_="titleline"):
#     title.append(new.getText())
#     link.append(new.find(name="a")["href"])

# for new in soup.find_all(name="span",class_="subline"):
#     if new.find(name="span",class_="score") is None:
#         upvote.append(0)
#     else:
#         upvote.append(new.find(name="span",class_="score").getText())
    
   
# print(len(title))
# print(len(upvote))


# for i in range(len(upvote)):
#     print(title[i])
#     print(upvote[i])
#     print(link[i])
#     print("_________________________________________________")
#scrape the website to find the top 100 movies and store it in a text file
response= requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup=BeautifulSoup(response.text,"html.parser")
print(soup.title)
title_list=[]
movie_title= soup.find_all(name="h3",class_="title")
for title in movie_title:
    title_list.append(title.getText())

title_list.reverse()
print(title_list)

with open("movie.txt","w",encoding="utf-8") as file:
    for title in title_list:
        file.write(f"{title}\n")