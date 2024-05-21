# tuple is a cannot be change immutable

a = (1,2,3,4,5,6,7,8,9,10,"sachin")

print(a)

print(a[0])


a = [1,2,3,4,5,6,7]

b = tuple(a)
print(b)

for i  in range(len(a)):
    print(a[i])
