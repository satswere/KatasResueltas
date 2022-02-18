first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km * 0.621
print(distance_mi)

#Second excersice

first_planet = input('Introduzca la distancia del sol para el primer planeta en KM')
second_planet = input('Introduzca la distancia desde el sol para el segundo planeta en KM')
first_planet = int(first_planet)
second_planet = int(second_planet)
distance_km = second_planet - first_planet
print(distance_km)
distance_mi = distance_km * 0.621
print(abs(distance_mi))