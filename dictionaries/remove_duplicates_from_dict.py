
my_dict = {'1': 1, '2': 2, '3': 2, '4': 2, '5': 5}

for value in my_dict.values():
    print(value)

print("-" * 70)

# use a "set" to de-dupe dictionary values 
for value in set(my_dict.values()):
    print(value)
