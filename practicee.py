"""
name = "Tanmoy"
print(len(name))
print(name[0:6:2])

l1 =  []
for i in  range  (1,11):
    l1.append(i)

print(l1)

x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))
z = int(input("Enter the value of z "))
n = int(input("Enter the value of n "))

final_list = []
for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if a+b+c !=n:
                final_list.append([a,b,c])
print(final_list)
"""

count = 10

while count > 0:
    print(count)
    count -= 1
