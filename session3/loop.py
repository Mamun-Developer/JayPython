# While loop that print s out the numbers from 1 to 5
print("Printing 1 to 5 using while loop")
i = 1
while i <= 5:
    print(i)
    i += 1
print("FINISHED")

# While loop that print s out the numbers from 5 to 1
print("Printing 5 to 1 using while loop")
i = 5
while i >= 1:
    print(i)
    i = i - 1
print("FINISHED")

# For loop that prints out the numbers from 1 to 5
print("Printing 1 to 5 using for loop")
# 2 - 1 = 1
for d in range(1, 6, 1):
    print(d)
print("FINISHED")

# For loop that prints out the numbers from 5 to 1
print("Printing 5 to 1 using for loop")
# 4 - 5 = -1
for d in range(5, 0, -1):
    print(d)
print("FINISHED")

# For loop that stops printing when the number is 5
for num in range(1, 10):
    if num == 5:
        break
    print(num)
print("FINISHED")

# Nested loop
for i in range(2, 0, -1):
    for j in range(2, 0, -1):
        # f string
        print(f"{i} * {j} = {i * j}")
