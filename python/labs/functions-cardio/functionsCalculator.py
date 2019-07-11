print("Welcome to Belen's Function Calculator!")
num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("Give me another number: "))


def myAddFunction(add1,add2):
     sum = add1 + add2
     return sum

print ("Here is the sum:" +str( myAddFunction(num1, num2)))

#mySubFunction
def mySubFunction(sub1,sub2):
     difr = sub1 - sub2
     return difr

print ("Here is the difference:" +str( mySubFunction(num1, num2)))

#myMultFunction
def myMultFunction(mul1,mul2):
     prod = mul1 * mul2
     return prod

print ("Here is the Product:" +str( myMultFunction(num1, num2)))
