planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Neptuno']
print("Hay ", len(planets), " planetas")
for i in planets:
    print(i)

planets.extend(['Plutón'])
print("Pero antes habían ", len(planets), " y el último era ",planets[-1])


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

user = input("Nombre Planeta")

if user in planets:
    indice = planets.index(user)
    print(f"Planetas más cercanos al sol que {planets[indice]}:", planets[0:indice])
    print(f"Planetas más lejanos al sol que {planets[indice]}: ", planets[indice+1:])
else:
    print("El planeta no está en la lista")