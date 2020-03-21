class Country:
    def __init__(self, name, population, size):
        self.name = name
        self.population = population
        self.size = population

    def is_larger(self, country):
        if self.population > country.population:
            return True
        else:
            return False

    def __str__(self):
        return "The population density is " + self.population + " and " + self.size

    def __repr__(self):
        return self