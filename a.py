# print(5//3, "\"", end="\n")
# print(min(1, 2, 4, 5), max(2, 10))
# print(pow(5, 3))
# print(round(5 / 3))

####### Lesson #4 
# x = 5

# del x

# y = 1.3
# print(y)

# b = True
# b = False
# print(b)

####### Conditional Statements (if elif else)
# x = 1
# y = 2

# if x == 1 and y == 2 or x == 1 and y == 3:
#     print("yes")

# elif x == 1:
#     print("yes")

# else:
#     print("no")

# a = 5 if x ==1 else 0 #this is a ternary operator
# print(a)

####### Loops and operators in them

for i in range(0, 10, 3):
    print(i)

isCar = True

while isCar:
    if input("Enter text: ") == "Stop":
        isCar = False

count = 0
for i in "hello":
    if i == "l":
        count+=1
print(count) 

found = None
for i in "hello":
    if i == "l":
        found = True
        break
    else:
        found = False
        
print(found)