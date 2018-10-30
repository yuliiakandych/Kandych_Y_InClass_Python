def greetings():
    print("Hello from the greetings function");



# the greetings function just says hello
# invoke or call the function
greetings()

def greetingsWithArgs(msg="a default message"):
    # print the msg variable
    print("now we're saying", msg, "from another function")


greetingsWithArgs()
greetingsWithArgs("somethin completely different")
greetingsWithArgs("running yet again")

# variables and scopes
myNumberVariable = 10


# returning values from functions (very powerful)
def someMath(num1=2, num2=4):
    global myNumberVariable

    myNumberVariable = num1 + num2
    return num1 + num2


sum = someMath()
print("we are doing some math an getting", sum)

sum = someMath(10, 15)
print("another math operation with", sum, "as the result")

