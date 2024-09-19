class Ville:
    def __init__(self, nom : str, population : int):
        self.__nom = nom
        self.__population = population
        
    def get_nom(self):
        return self.__nom
        
    def get_population(self):
        return self.__population
    
    def set_nom(self, nom : str):
        self.__nom = nom
        
    def set_population(self, population : int):
        self.__population = population
                
    def __eq__(self, v):
        return self.__nom == v.get_nom() and self.__population == v.get_population()
            
    def __str__(self):
        return "{} ({})".format(self.__nom, self.__population)
            
            