from bs4 import BeautifulSoup
import lxml
with open("Day-45/website.html",encoding="utf-8") as file:
    contents = file.read()
soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
    
    
# heading = soup.findAll(name="p")
# for n in heading:
#     print(n.getText())
#     print(n.get("class"))

companny_url = soup.select_one(selector="p a")
print(companny_url)

heading=soup.select(selector=".heading")
print(heading)