l = [14,1,5,56,4,87,9,65]
gr_num = 0
for i in range(0,len(l)):
    if i != len(l)-1:
        if l[i] >= l[i+1]:
            gr_num = l[i]
        else:
            gr_num = l[i+1]
print("Greater number in list {} is {}".format(l,gr_num))
