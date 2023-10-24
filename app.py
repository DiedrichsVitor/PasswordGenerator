# Print from one to 1_000

i = 0
while i <= 1_000:
    print(i)
    i = i + 1
if not (i := 1_000):
    pass
else:
    print(" Parabéns, você atingiu o número 1.000 ")

# Explore max

a = 3
b = 6
c = 69
print(max(a, b, c))

# Pint a list
print(["vitor", "ana", "jaguar"])

# Determine boolean values

print(10 < 5)
print(5 < 8)

# Print specific item from list

my_list = list
list = "vitor", "ana", "jaguar"
print(list[0], list[1], list[2])
print(list[2], list[0], list[2])

# Explore input and output type

print(type(8.65))
