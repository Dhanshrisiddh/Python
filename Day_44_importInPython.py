import math
result=math.sqrt(16)
print(result)

# OR
from math import sqrt,pi
result1=sqrt(64)
print(result1)

# OR
from math import sqrt as s
result1 = s(81)
print(result1)

# The dir function
import math
print(dir(math))

# FOllowing gives wrong output use it wisely 
# OR
from math import pi,sqrt as s
result2 = s(4)*pi
print(result2)
  
# OR
import math as m
result4 =m.sqrt(9)*m.pi
print(result4)
