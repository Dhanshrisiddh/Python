# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a + b + c) / 2
print("Perimeter is:",s)

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is :",area)


#=========================User Input====================

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2
print("Perimeter is:",s)

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is:",area)