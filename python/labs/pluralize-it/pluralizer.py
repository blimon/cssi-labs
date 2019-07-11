print("Welcome to Belen's Pluralizer!")
word1 = raw_input("Enter first word here: ")
num = int(raw_input("Enter a number: "))
if num == 0:
     print(str(num)+ " " + word1 + "s")
elif num > 1:
     print(str(num)+ " " + word1 + "s")
else:
     print(str(num)+ " " + word1)
    
