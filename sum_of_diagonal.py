mylist=[]
for i in range(4):
    mylist.append([])
    for j in range(4):
        n=int(input("Enter any no:"))
        mylist[i].append(n)
        s=0
for i in range (4):
 for j in range(4):
     if i==j:
         s=s + mylist[i][j]
print("sum of diagonal:",s)
