# function definition
def find_square(num):
    result = num * num
    return result

square = find_square(3)

print('Square:', square)


print("=====================square=============")
def square(num):
    square=num*num
    print("square is",square)
square(5)

print("======================user input ===============")

def square(num):
    result=num*num
    print("Square is", result)

user_input = int(input("Enter a number: "))
square(user_input)


