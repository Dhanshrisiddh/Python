print("==================for string loop======================")
name = 'Abhishek'
for i in name:
  print(i)
  if(i =="b"):
    print("This is something special!")

print("=====================for list loop=====================")  
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
    print(i)

print("==============If you want to print from 0 then=============")
for k in range(5):
  print(k)

print("==============If you want to print from 1 then=============")
for k in range(5):
  print(k+1)

print("==============If you want to print from 1 to 9  then=============") 
for k in range(1, 10):
  print(k)

# 1=start ,12=end,3=step
for k in range(1, 12, 3):
  print(k)