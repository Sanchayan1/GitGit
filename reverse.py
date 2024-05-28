st=input("Enter any string")
rev=""
s=st.split()
x= len(s)
for i in range(-1,-(x+1),-1):
 rev=rev+st[i]
j="".join(rev)
print(j)
