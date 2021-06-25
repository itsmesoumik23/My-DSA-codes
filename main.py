from random import randint

print("Enter the length of the desired password(minimum 8)")
l = int(input())

default_set = ["@#$%^&*()_+=!~/.", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
               "1234567890","abcdefghijklmnopqrstuvwxyz"]

password = []
count_array = [2]
x = 0
for i in range(4):
    x += count_array[-1] - 2
    count_array.append(randint(2, l-6-x))
count_array[-1] += (l - (sum(count_array)-2))
count_array.pop(0)

for count, element in enumerate(count_array, 0):
    for j in range(element):
        password.append(default_set[count][randint(0, len(default_set[count])-1)])
for i in range(0, l):
    a, b = randint(0, l-1), randint(0, l-1)
    password[a], password[b] = password[b], password[a]

print("Genarated password: "+"".join(password))