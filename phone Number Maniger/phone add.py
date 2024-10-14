def nono():
    print("Add Number")
    print("Remove Number")
    print("View All Numbers")
    print("Exit")

nono()

book = {}

while True:
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        name = input("Enter Your Name: ")
        number = int(input("Enter Your Number: "))
        book[name] = number
        print("Number is Added Successfully: ")
    elif choice == 2:
       names =  input("Enter The Name Of You Want To Remove: ")
       if name in book:
        book.pop(names)
        print("Number is deleted Successfully: ")
       else:
        print("This Number is Not in Our Recorde")

    elif choice == 3:
        for key,values in book.items():
            print(f"{key} - {values}")
    elif choice == 4:
        break

print("Done")