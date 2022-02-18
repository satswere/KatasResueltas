#ejercicio 1
planet = {
    "name": "Mars",
    "moons": 2,
}

print(planet.get("name"),"tiene", planet.get("moons"),"lunas")

planet['circunferencia(km)'] = {
    "polar":2752,
    "equatorial": 6792
}

print(f'{planet["name"]} tiene una circunferncia de {planet["circunferencia(km)"]["polar"]}')

#ejercicio 2

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

values = planet_moons.values()
TotalPlanetas = len(values)
total_moons=0
for value in values:
    total_moons = total_moons + value
print("Lunas promedio",total_moons/TotalPlanetas)