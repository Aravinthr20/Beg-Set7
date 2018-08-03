A=str(input("Numbers:"))
a=len(A)
b=[]
for i in range(0,a):
    x=A[i]
    b.append(x)
    b.sort()
print(min(b))