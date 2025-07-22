employee ={
    "name":"Dhanshree",
    "age":20,
    "PRN":2203045,
    "vote":"True"
}
print(employee)
employee.update({"id":100})
employee.update({"salary":1000})
print(employee)

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1) 