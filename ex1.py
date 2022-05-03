# Filter out all of the empty strings from the list below
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

def filterEmpty(p):
    return list(filter(lambda x: x.strip() != "",p))

print(filterEmpty(places))