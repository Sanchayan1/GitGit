st=input("Enter any string:")
v="aeiouAEIOU"
c=0
for ch in st:
    if ch in v:
        c+=1
        print("No of vowel:",c)
