
print("Enter any integer for number of rows ")
n=int(input())
val=int(input("Choose  0 or 1 for printing pattern\n"))
if val==1:
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()
        
    
else:
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()

