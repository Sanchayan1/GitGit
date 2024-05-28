pbook=[]
res='y'
def add_new_contact():
        nm=input("Enter name:")
        ph=input("Enter phone no:")
        pbook.append(nm)
        pbook.append(ph)
        print("Wissh to continue[Y/N]:")
        res=input("Enter response:")
        if res==Y:
            print("You have chosen to add another new contact.");
            add_new_contact();
        else:
            print("Thank You")
            
def search_contact():
    nm=input("Enter name for searching")
    if nm in pbook:
        x=pbook.index(nm)
        print("Name:",nm,"ph no:",pbook[x+i])
    else:
        print("Name does not exist")
def Remove_name():
    nm=input("Ënter value for detection:")
    if nm in pbook:
        x=pbook.index(nm)
        pbook.pop(x)
        pbook.pop(x)
        print("Contact deleted succesfully")
    else:
        print("Name does not exist")

print("Welcome to phonebook")

while True:
    print("\nMain Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Remove Any Contact")
    choice1 = int(input("Enter the Choice:"))

    if choice1 == 1:
        print("You have chosen to add new contact.");
        add_new_contact();
        break
    elif choice1 == 2:
        print("You have chosen to search any contact.");
        search_contact();
        break
    elif choice1 ==3:
        print("You have chosen to Remove any contact.");
        Remove_name();
        break
    else:
        print("You have entered an invalid choice.")
        
        
        
        
        
        
        
        
