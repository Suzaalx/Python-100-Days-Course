import pandas
gray=0
Cinnamon=0
black=0
data=pandas.read_csv("Day-25/census.csv")

gray=len(data[data["Primary Fur Color"]=="Gray"])
Cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])
black=len(data[data["Primary Fur Color"]=="Black"])
# elif data[color]=="Black":
#     black+=1
# elif data[color]=="Cinnamon":
#     Cinnamon+=1
data_dictt ={
    "Fur color": ["Gray", "cinnamon", "Black"],
    "count": [gray,Cinnamon,black]
}
data=pandas.DataFrame(data_dictt)
data.to_csv("Day-25/count.csv")
print(f"{gray},{Cinnamon} and {black}")