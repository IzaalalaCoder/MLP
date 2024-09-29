class OperationImpossible(Exception):
    """
    Représente une exception d'opération impossible
    """
    pass

class Ville:
    """
    Represente les villes.
    """
    def __init__(self, nom : str, population : int):
        """
        Initialise les champs de la ville.
        """
        self._nom = nom
        self._population = population
        
    @property
    def nom(self):
        """
        Un accesseur du champ nom de la ville.
        """
        return self._nom
        
    @property
    def population(self):
        """
        Un accesseur du champ population de la ville.
        """
        return self._population
                
    def __eq__(self, v):
        """
        Une méthode spécial permettant d'analyser l'égalité entre les deux villes.
        """
        return self._nom == v.nom and self._population == v.population
            
    def __str__(self):
        """
        Une méthode spécial permettant de décrire de façon informelle la ville.
        """
        return "{} ({})".format(self._nom, self._population)
    
class Route:
    """
    Represente les routes.
    """
    
    def __init__(self, v1 : Ville, v2 : Ville, distance):
        """
        Initialise tous les champs qui compose la notion d'une route.
        """
        self._v1 = v1
        self._v2 = v2
        self._distance = distance
        
    @property
    def v1(self):
        """
        Une méthode permettant de retourner la valeur issue de v1.
        """
        return self._v1
    
    @property
    def v2(self):
        """
        Une méthode permettant de retourner la valeur issue de v2.
        """
        return self._v2    
    
    @property
    def distance(self):
        """
        Une méthode permettant de retourner la valeur issue de distance qui sépare v1 de v2.
        """
        return self._distance
    
    def circuit(self):
        """
        Une méthode permettant d'affirmer ou non la présence d'un circuit.
        """
        return self._v1 == self._v2
    
    def __contains__(self, v : Ville):
        """
        Une méthode spécial permettant de savoir si la ville v est contenu dans la route issu de self.
        """
        return self.v1 == v or self._v2 == v
    
    def memes_villes(self, r):
        """
        Une méthode permettant de savoir si la route issu de self et la route issu de r contiennent 
        les mêmes villes.
        """
        if self._v1 == r.v1:
            return self._v2 == r.v2
        elif self._v1 == r.v2:
            return self._v2 == r.v1
        else:
            return False
        
    def suit(self, r):
        """
        Une méthode permettant de savoir s'il existe une suite entre les deux routes.
        """
        return self._v1 in r or self._v2 in r
    
    def __eq__(self, r):
        """
        Une méthode permettant de savoir si la route issu de self et la route issu de r contiennent 
        les mêmes villes et ont la même distance.
        """
        return self.memes_villes(r) and self._distance == r.distance
    
    def __lt__(self, r): 
        """
        Une méthode permettant de savoir si la route issu de self et la route issu de r contiennent 
        les mêmes villes et que la distance appartenant à self est strictement plus petite que celle de r.
        """
        return self.memes_villes(r) and self._distance < r.distance
    
    def __str__(self):
        """
        Une méthode spécial permettant d'afficher une chaine qui décrit la route courante.
        """
        return "{} - {} : {}".format(self._v1, self._v2, self._distance)
    
    def __add__(self, r):
        """
        Une méthode spécial permettant de réaliser l'action d'ajoute de deux routes. Deux cas sont identifiés :
        La première est il faut qu'une ville issue de self soit contenue dans r
        La seconde est représenté par le fait qu'il s'agit de la même route
        """
        if self.memes_villes(r):
            return Route(self._v1, self._v1, self._distance)
        elif self._v1 in r:
            if self._v1 != r.v1:
                return Route(self._v2, r.v1, self._distance + r.distance)
            else:
                return Route(self._v2, r.v2, self._distance + r.distance)
        elif self._v2 in r:
            if self._v2 != r.v1:
                return Route(self._v1, r.v1, self._distance + r.distance)
            else:
                return Route(self._v1, r.v2, self._distance + r.distance)
        else:
            raise OperationImpossible()
        
class Reseau:
    """
    Represente les réseaux routiers.
    """
    
    def __init__(self):
        """
        Initialise les champs routier. Par défaut il n'existe pas de routes donc la liste est vide.
        """
        self._routes = list()
    
    @property
    def routes(self):
        """
        Retourne la liste des routes existant dans le réseau routier.
        """
        return self._routes
    
    def __getitem__(self, i : int):
        """
        Permet de retourner la ième route parmi la liste des routes.
        """
        if i < 0 or i >= len(self._routes):
            raise IndexError
        else:
            return self._routes[i]
        
    def __len__(self):
        """
        Retourne le nombre de routes du réseau.
        """
        return len(self._routes)
    
    def __iter__(self):
        """
        Retourne l'itérateur associé à la liste des routes qui se trouve dans le réseau.
        """
        return iter(self._routes)
    
    def __contains__(self, r : Route):
        """
        Vérifie la présence de la route r dans le réseau routier.
        """
        for rt in self._routes:
            if r == rt:
                return True 
        return False
    
    def ajoute(self, r : Route): 
        """
        Permet l'ajout d'une route dans le réseau routier.
        """
        self._routes.append(r)
        return self
    
    def __iadd__(self, res):
        """
        Permet l'ajout de toutes les routes issu de res dans le réseau routier appartenant à self.
        """
        for r in res: 
            self.ajoute(r)
        return self
    
    def __str__(self):
        """
        Permet l'affichage de toutes les routes se trouvant dans le réseau routier issu de self.
        """
        string = ""
        for r in self._routes:
            string += r.__str__() + "\n"
        
        return string
    
    def bonne_route(self, r : Route):
        """
        Permet de vérifier si r est une bonne route.
        """
        if not r.circuit():
            for rt in self._routes:
                if rt < r: 
                    return False
            return True
        else:
            return False
        
    def bonnes_routes(self):
        """
        Permet de créer un réseau ne contenant uniquement de bonnes routes.
        """
        res = Reseau()
        for r in self._routes:
            if self.bonne_route(r) and not (r in res):
                res.ajoute(r)
        return res
    
    def __or__(self, res):
        """
        Permet de créer un réseau ne contenant uniquement de bonnes routes issus de self ou de res.
        """
        reseau = Reseau()
        reseau += res
        reseau += self
        return reseau.bonnes_routes()

    def __mul__(self, res):
        """
        Permet de créer un réseau ne contenant uniquement de bonnes routes issu de la multiplication des routes issus de self et de res.
        """
        reseau = Reseau()

        for i in self._routes:
            for j in res.routes:
                reseau.ajoute(i + j)
        
        return reseau.bonnes_routes()

    def meilleurs_routes3(self):
        """
        Permet de créer un réseau ne contenant uniquement des routes combiné jusqu'à trois fois et qui sont de bonnes routes.
        """
        res = Reseau()
        res += self

        for r1 in self._routes:
            for r2 in self._routes:
                try:
                    route = r1 + r2
                    if res.bonne_route(route):
                        res.ajoute(route)
                except OperationImpossible:
                    continue

        for r1 in self._routes:
            for r2 in self._routes:
                for r3 in self._routes:
                    try:
                        route = (r1 + r2) + r3
                        if res.bonne_route(route):
                            res.ajoute(route)
                    except OperationImpossible:
                        continue
        
        return res.bonnes_routes()

    def meilleurs_routes(self):
        """
        Retourne le réseau des routes les plus courtes possibles en traversant autant de routes que désiré.
        """
        res = Reseau()
        res += self
        taille_initiale = 0

        while taille_initiale != len(res.routes):
            taille_initiale = len(res.routes)
            for r1 in res.routes:
                for r2 in self.routes:
                    try:
                        route = r1 + r2
                        if res.bonne_route(route) and route not in res:
                            res.ajoute(route)
                    except OperationImpossible:
                        continue
        return res.bonnes_routes()