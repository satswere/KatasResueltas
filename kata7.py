i=0
new_planet = ''
planets = []
print('Puts "done" if you already finish c:')
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet ')
print('The planet that you insert are:')
for j in planets:
    print(j)