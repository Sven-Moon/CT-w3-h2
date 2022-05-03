# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
def tempsC(locs):
    return list(map(lambda x: (x[0], x[1]*9/5+32), locs))
    
print(tempsC(places))

print ([(x[0], x[1]*9/5+32) for x in places])