#tuples are imutable
my_info = ('Sam', 24, 'Teacher')
t = ["si", 1, 2]
print(my_info)

print(my_info[0])

#how to unpack a tuple

name, age, occupation = my_info
w, s, d = t
print(age, occupation)
print(w)