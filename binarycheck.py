A=str(input("Binary Number:"))
a=len(A)
num=0
for i in range(0,a):
    x=A[i]
    if (int(x)<=1):
        num=num
    else:
        num=num+1
if (num<=0):
    print("Yes")
else:
    print("No")
print(num)