from tp2 import *

# Test du second exercice
arr = NDArray([1, 2, np.nan, 4, np.inf, 6])
arr_test = NDArray([5, 1, 9, -5, 0, 3])

print("Tableau de départ : \n", arr)
print("Tableau avec les valeurs manquantes remplacées par la moyenne : \n", arr.filled(strategy="mean"))
print("Tableau avec les valeurs manquantes remplacées par la médiane : \n", arr.filled(strategy="median"))

try:
    print("Tableau avec les valeurs manquantes remplacées par une stratégie inconnue : ")
    arr.filled(strategy="error")
except ValueError as e:
    print(e)


print("La normalisation des données")
print(arr.filled().normalize())

print("La normalisation standard")
print(arr.filled().std_normalized())

print("Le test de Student")
print(arr.filled().ttest(arr_test))

# Test de la surchage des opérateurs
