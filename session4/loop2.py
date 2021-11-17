data = []  # Empty list
data = [12, 2, 34, 1, 45]  # List with 3 elements
# Size of a list
list_length = len(data)

i = 0
while i < list_length:
    print(data[i])
    i += 1

# Create a list from 1 to 1000
data = list(range(1, 1001, 1))
print(data)

# Create a list from 1 to 1000 Way 2
data = []
for d in range(1, 1001, 1):
    data.append(d)
print(data)

"""
I have fiver cars, the cars are: BMW - 2, Audi - 2, Ford - 1
"""

data = {"BMW": 2, "Audi": 2, "Ford": 1}
# Lets buy another BMW
data['BMW'] += 1
print(data['BMW'])

for key in data:
    print(key,data[key])

# Remove a key from the dictionary
del data['BMW']


print(list(data.values()))
print(list(data.keys()))

print(data.get("Tesla"))
print(data)

