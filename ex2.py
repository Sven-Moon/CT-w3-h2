# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']


def sortByLast(names):
    return sorted(names, key=lambda x: x.split(" ")[-1].lower())

print(sortByLast(author))