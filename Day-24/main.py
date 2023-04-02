#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names= open("Day-24\\Input\\Names\\invited_names.txt", "r")

name=names.readlines()
print(name)
letter= open("Day-24\\Input\\Letters\\starting_letter.txt")
mail=letter.read()
for i in name:
    x=i.strip("\n")
    filelocation= f"Day-24/Output/ReadyToSend/letter {x}.txt"
    filename=mail.replace("[name]",x)
    print(filename)
    f= open(filelocation,"w")
    f.write(filename)
        
    
