year = int(input("Which year do you want to check? "))

#if year % 4 == 0 and year % 400 == 0:
    #print("Leap Year")
#elif year % 100 == 0:
   # print("Not a Leap Year")
#else:
    #print("Not a Leap Year")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")