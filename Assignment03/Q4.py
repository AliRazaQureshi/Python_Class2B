l = ["ali", 2, "c", 0.5, 45, "hello world"]
sum = 0
for i in range(0,len(l)):
    if (type(l[i]) == int) | (type(l[i]) == float):
       sum = sum + l[i]
print("Sum of all Numeric items in list is: ",sum) 
