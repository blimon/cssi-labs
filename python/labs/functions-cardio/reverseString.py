print("Welcome to Reverse String!")
word = raw_input("Give me a word: ")

def reverse_string(s1):
    print(s1[-1:-len(s1)])

reverse_string(word)
