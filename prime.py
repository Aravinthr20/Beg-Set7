x=int(input("Number:"))
if x > 1:
    for i in range(2, x):
        if (x%i)== 0:
            print("No")
            break
    else:
        print("yes")
else:
    print("No")