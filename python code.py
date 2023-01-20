"""

x="Trading"
def myfunc():
    x="Devops"
    print("I love " +x)
    myfunc()
    print("I love " +x)

    x="Pushpa "
    def myfunc():
        global x
        x="Pushparaj "
    myfunc()
    print(x+ "Flower samje keya fire hai mai")
"""
"""
print("Entre first number")
num1 = input()
print("Entre second number")
num2 =input()
print(int(num1)+int(num2))
"""
"""
d1 = {"banna":"kola","hot-water":"garam-jal","panipuri":"fuchka","chicken":"murgir-mngso"}
print("Enter the word you want to know meaning")
d2=input()
print(d1[d2])

"""
"""
print("Enter your age")
your_age = int(input())
if  your_age>18 :
    print("You can deive")
elif your_age==18:
    print("come in person we will check")
else:
    print("you can not drive")

"""
"""

n=18
number_of_guesses=1
print("numberof gusses is limited to only 9 times: ")
while(number_of_guesses<=9):
    print("Enter the number you are guessing")
    num1 = int(input())

    if num1>n:
        print("your number is greater than original number put less number")
    elif num1<n:
        print("your number is less than original number put grater number ")
    else :
        print("you chose the right number")
        break
    print(9-number_of_guesses,"no.of guesses he took tofinish.")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game over")

"""
"""


while(True):
    num = int(input("Enter a number"))
    if num>100:
        print("you entered the right number")
        break
    else:
        print("Try again!")

"""
"""

def function1(a,b):
    average =(a+b)/2
    return average

v = function1(4,7)
print(v)
"""
        
"""
print("Enter the number")
num1 =input()
print("Enter the number")
num2 = input()

try:
    print("Thye sum of two number is ",int(num1)+int(num2))
except Exception as q:
    print(q)

print("I will succeed")

"""
"""
f = open("check.txt")
content = f.read()
print(content)

f.close()
"""


"""
f = open("check2.txt", "w")
f.write("I am a good boy")
f.close()

"""
"""
import time
intial = time.time()
a=0
while(a<5):
    print("Uh lah! lah!")
    a+=1
print("Timing is",time.time() - intial,"seconds")

"""
"""
print(" Fake Fan Finder \n","--------------------")
fan = input(" What's your favourite Anime? " )
if fan == "One piece":
    faveCharacter = input("Oh really?! Name me any of the character? ")
    if faveCharacter == "Nami":
      choice = input("You got that by pure chance. Okay then, what is her job on the ship? ")
    if choice == "Navigator":
      var1 = input("Hmph! What was her first bounty then? " )
    if var1 == "Ummm...":
      print("See! Fake one piece fan!")
  
else:
  print("See! Fake one piece fan!")
 
"""
"""
import array as arr

var = arr.array('i',[5,8,4,88,45])
print(var,len(var))
"""

"""
import array as arr

var = arr.array('i',[])
ard = int(input("Enter lenth"))
for i in range(ard):
    var1 = int(input("Enter value"))
    var.append(var1)

def findElement(arr, n):
        for i in range(1, n):
            leftSum = sum(arr[0:i])
            rightSum = sum(arr[i+1:n])
            if(leftSum == rightSum):
               
                return arr[i]
              
        return -1
      
print (i-1,findElement(var, len(var)))
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.head = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.nextval


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

   
    linked_list = LinkedList()
    linked_list.head = n1
    linked_list.head.nextval = n2
    n2.nextval = n3
    n3.nextval = None


    linked_list.traverse()    




