print("hello world")

def chai(n):
    print(n)
    

chai(6)    
    

# 1  if else condition


name = input("enter your name ")
age = int(input("enter you age "))

if age >=18:
    print("you are eligible to vote")
elif age < 18 and age > 0:
    print(f"you are{name} not eligible to vote")
else :
    print(f"you are{name} not eligible to vote")

# 2 

year = int(input("enter you year"))   

if year %4 ==0 and year %100 != 0:
    print("leap year")
elif year %100 == 0 and year %400 == 0:
    print("leap year")
else:
    print("not a leap year")  

# 3

alpha = input("enter a words")  

if alpha in "aeiouAEIOU":
    print(f"{alpha} is a vowel")
else:
    print(f"{alpha} is a consonant")  


# loops 
# 1

n = int(input("enter your no"))

for i in range(1,n+1):
    print(i)


# 2  resvers loops

n = int(input("enter your no"))

for i in range(n,0, -1):
    print(i)

# 3 print tables

n = int(input("enter your no tables"))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")



# 4 sum total no
n = int(input("please tell me no"))

sum = 0
for i in range(1,n+1):
    sum = sum + i
    
print(sum)

# 5 factorial 
n = int(input("please tell me no"))

fact = 1
for i in range(1,n+1):
    fact = fact * i
    
print(fact)



# advance loops question

# 1 factor

n = int(input("tell  me number"))

for i in range(1,n+1):
    if n%i == 0:
        print(i, end = " ")

# 2 perfect number with factorial and strong number

n = int(input("tell your number "))

sum = 0
for i in range(1,n):
    if n%i == 0:
        sum = sum + i

if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")


print(sum) 

# 3 prime number check

n = int(input("tell your number "))

count = 0
for i in range(1,n):
    if n%i == 0:
        count = count + i

if count == 2:
    print(f"{n} prime number")
else:
    print(f"{n} not a prime number")

# 4 separete digit number and new line 

a = int(input("tell your number "))

while a > 0:
    print(a%10)
    a = a//10
    




        












