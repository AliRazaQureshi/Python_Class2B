l = [1, '2', 3, 'hello', 5, 6, 'world']
Sum = 0
for i in range(0, len(l)):
    if type(l[i]) == int or type(l[i]) == float:
        Sum = Sum + l[i]
print("Sum of {} is {}".format(l, Sum))
