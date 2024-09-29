from routes import *

# Les villes

paris = Ville("Paris", 10784830)
arras = Ville("Arras", 131047)
lyon = Ville("Lyon", 1659001)
nantes = Ville("Nantes", 650081)
strasbourg = Ville("Strasbourg", 467438)
marseille = Ville("Marseille", 1590867)
montpellier = Ville("Montpellier", 440896)
poitiers = Ville("Poitiers", 131499)
brest = Ville("Brest", 201741)
bordeaux = Ville("Bordeaux", 927445)

reseau = Reseau()

reseau.ajoute(Route(paris, arras, 185))
reseau.ajoute(Route(paris, lyon, 465))
reseau.ajoute(Route(paris, poitiers, 338))
reseau.ajoute(Route(paris, brest, 593))
reseau.ajoute(Route(paris, nantes, 386))
reseau.ajoute(Route(arras, nantes, 561))
reseau.ajoute(Route(arras, strasbourg, 522))
reseau.ajoute(Route(nantes, brest, 298))
reseau.ajoute(Route(strasbourg, lyon, 494))
reseau.ajoute(Route(strasbourg, marseille, 809))
reseau.ajoute(Route(strasbourg, montpellier, 797))
reseau.ajoute(Route(lyon, marseille, 315))
reseau.ajoute(Route(lyon, montpellier, 303))
reseau.ajoute(Route(marseille, montpellier, 171))
reseau.ajoute(Route(montpellier, poitiers, 557))
reseau.ajoute(Route(poitiers, bordeaux, 237))
reseau.ajoute(Route(bordeaux, nantes, 334))

print(reseau.meilleurs_routes())