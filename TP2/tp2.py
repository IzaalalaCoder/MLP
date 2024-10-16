import numpy as np

def exo1():

    # Q1 - Créer un tableau ndarray 4 x 5 de réels sur 4 octets valent tous 1
    a = np.ones((4, 5), dtype = float)
    print("Tableau A")
    print(a)
    print()

    # Q2 - Créer un tableau 4 x 5 de réels sur 4 octets avec quatres lignes dont les valeurs sont 1, 2, 3, 4, 5
    b = np.array([1, 2, 3, 4, 5] * 4, dtype = float).reshape(4, 5)
    print("Tableau B")
    print(b)
    print()

    # Q3 - Concaténer horizontalement, puis verticalement, les deux derniers tableaux
    # --> Horizontalement
    r = np.concatenate((a, b), axis = 0)
    print("Horizontalement")
    print(r)
    print()
    # --> Verticalement
    r = np.concatenate((a, b), axis = 1)
    print("Verticalement")
    print(r)
    print()

    # Q4 - Créer un tableau 4 x 5 de valeurs aléatoires suivant la loi normale avec une moyenne de 0 et un écart type de 3
    print("Affichage d'un tableau contenant des valeurs aléatoire suivant la loi normale dont la moyenne est de 0 et l'écart-type de 3")
    rng = np.random.default_rng(12345)
    r = rng.normal(loc = 0, scale = 3, size = (4, 5))
    print(r)
    print()

    # Q5 - Afficher la dernière ligne, puis la dernière colonne de ce dernier tableau 
    # Affichage de la dernière ligne
    print("Affichage de la dernière ligne")
    print(r[3:])
    print()

    # Affichage de la dernière colonne 
    print("Affichage de la dernière colonne")
    print(r[:,4])
    print()

    # Q6 - Redimensionner ce tableau en 5 x 4
    r.reshape((5, 4))

    # Q7 - Créer à partir de ce tableau, un sous-tableau qui ne contient ni la première ligne, ni la première colonne
    s =  r[1:, 1:]
    print("Affichage du sous-tableau")
    print(s)
    print()

    # Q8 - Créer un tableau à une dimension qui contient les valeurs positives de ce tableau 
    p = s[s > 0]
    print("Affichage du sous-tableau ne contenant uniquement des valeurs postives")
    print(p)
    print()

    # Q9 - Créer un tableau qui contient les valeurs positives du dernier tableau et 0 si les valeurs sont négatives
    n = np.where(s > 0, s, 0)
    print("Affichage du sous-tableau ne contenant uniquement des valeurs postives et 0 en cas de valeurs négatives")
    print(n)
    print()


