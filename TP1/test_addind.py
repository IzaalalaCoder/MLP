from routes import Ville, Route

paris = Ville("Paris", 10784830)
arras = Ville("Arras", 131047)
lyon = Ville("Lyon", 1659001)
paris_arras = Route(paris, arras, 185)
paris_lyon = Route(paris, lyon, 465)
print(paris_arras + paris_lyon)