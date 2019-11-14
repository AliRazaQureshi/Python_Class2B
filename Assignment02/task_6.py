l = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Sum = 0
for i in range(0,len(l)):
    if l[i] < 5:
        Sum = Sum + l[i]
print("Sum of elements less than 5 in list {} is {}".format(l,Sum))