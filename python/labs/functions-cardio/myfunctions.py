print("Welcome to my Belen's Calculator")

def count_spaces(s):
    return s.count(" ")
def count_vowels(s):
    numA = s.count("a")
    numE = s.count("e")
    numI = s.count("i")
    numO = s.count("o")
    numU = s.count("u")
    numY = s.count("y")
    sumVowels = numA + numE + numO + numI + numU
    return sumVowels
def count_total(s):
    return count_spaces(s) + count_vowels(s)
print(count_spaces("Hello there, you are the best!"))

countNum = count_spaces("Hello there, you are the best!)
print(countNum)
