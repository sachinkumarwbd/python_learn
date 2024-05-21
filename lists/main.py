a =[12,34,5,6,5,5,4,4,"sachin"]

print(a)

a[4] = "kumar"
print(a)


#methods

print(a[2:6]) #slicing
print(len(a)) #length
print(a.count(5)) #count
print(a.index("sachin")) #index
print(a.reverse()) #reverse
print(a.pop()) #pop
print(a.remove(5)) #remove
print(a.clear()) #clear
print(a.copy()) #copy

a.append(200) #append
print(a)
a.insert(2,5) #insert
print(a)

