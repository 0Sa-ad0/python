#1 
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
sum=a+b
print("sum of", a, "and", a, "is", sum)

#2 
for i in range(5):
    print(i)

#3
for num in range(8):
    print("hello"*num)
    
    
for i in range(2,10):
    print(i)
    
#4
x=6

while x<15:
    print(x)
    x+=1
    
#5 
x=6

while x>=0:
    print("hello" * x)
    x-=1
    
#6
x=6

while x>=0:
    print("*" * x)
    x-=1
    
#7
x=5

while x<15:
    if x%2==0:
        print("even",x)
        #break
    print(x)
    x+=1
    
#8
x=5

while x<15:
    if x%2==0:
        print("even num found")
        break
    print(x)
    x+=2
    
   # else:
      #  print("all are odd")
      
#9
for i in range(3):
    for j in range(2):
        print(i,j)
        
#10
def _sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
        return(sum)
        
        if __name__=="__main__":
            arr=[12,4,3,15]
            n=len(arr)
            ans=_sum(arr)
            print('sum of arr', ans)
            
#11
arr=[12,4,3,15]
ans=sum(arr)
print('sum of arr', ans)

#12 problem
def findArea(r):
    PI=3.1
    return PI*(r*r);
    
    print('area is %.2f' % findarea(5));
    
#13
num1 = 1
num2 = 5
num3 = 7
num4 = 9
num5 = 11

avg = (num1 + num2 + num3 + num4 + num5) / 5

print('The average of numbers = %0.1f' % avg)

#14
a = 7
b = 9
c = 11

s = (a + b + c) / 2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' % area)

#15
num = 24

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")
   
#16
from datetime import datetime

def calculate_age_in_seconds(birthdate):
    current_date = datetime.now()
    age = current_date - birthdate
    age_in_seconds = age.total_seconds()
    return age_in_seconds

birthdate = datetime(2000,1,1) 
age_seconds = calculate_age_in_seconds(birthdate)
print("Age in seconds:", age_seconds)

#17
def is_palindrome(number):
    number_str = str(number)
    return str(number) == reversed(str(number))

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
