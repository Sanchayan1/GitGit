list1=[]
num=int(input("Enter no of elements:"))
for i in range(1,num+1):
    ele=int(input("Enter elements :"))
    list1.append(ele)
    list1.sort(reverse=True)
    for j in range(1,num+1):
        if list1[j]!=list1[0]:
            print("Second largest:",list1[j])
            return
        print("There is no secong largest element")    
