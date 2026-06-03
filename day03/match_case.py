x = int(input("Enter the number: "))
match x:
    case 0:
        print("This is the case")
    case 1:
        print("No, this is the actual case")
    case _ if x >2:
        print(x, "is grater than 2")
    case _ if x<8:
        print(x, "is smaller than 8")
              