l = ["ali", 2, "c", 0.5, 45, "hello world"]
for i in range(0,len(l)):
    if (type(l[i]) == int) | (type(l[i]) == float):
        print("Numeric value Exist in list at {} position".format(i))
