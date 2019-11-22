l = [2,5,6,15,2,4,6,5,2,6]
dup = []
for i in range(len(l)):
    k = i + 1
    for j in range(k,len(l)):
        if (l[i] == l[j]) and (l[i] not in dup):
            dup.append(l[i])
print("Duplicate items in given list {} is {}".format(l, dup))