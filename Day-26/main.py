

import pandas


dict=pandas.read_csv("Day-26/nato_phonetic_alphabet.csv")

item={row.letter:row.code for (index,row) in dict.iterrows()}
print(item)

 
def generate():
    word=input("Enter a word: ").upper()
    try:
        result=[item[letter] for letter in word]
    except KeyError:
        print("Please enter letters in alphabet only")
        generate()
    else:
        print(result)

generate()