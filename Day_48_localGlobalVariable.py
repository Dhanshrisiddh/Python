
x=10       #local Variable
print(x)

def my_function():
    s=20           #global Variable
    print(s)

my_function()
print(x)  # Accessing the local variable outside the function   


# Accessing the global variable inside the function
def another_function():
    global x      # Declare x as global to modify it
    x = 30       # Modify the global variable
    print(x)    

#Basically we can access the global variable inside the function but not the local variable outside the function