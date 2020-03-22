class Country:
    def __init__(self, name, population, size):
        """
        store the three different information about a country
        :param name: country's name
        :param population: country's population
        :param size: country's size
        >>>Canada = Country("Canada", 37950000, 998500)
        >>>Canada
        ("Canada", 37950000, 998500)
        """
        self.name = name
        self.population = population
        self.size = population

    def is_larger(self, country):
        """
        compare the initialized country and country in the parameter about their population masses
        :param country: compared country
        :return: which country is larger in population
        >>>Canada.is_larger(Denmark)
        False
        """
        if self.population > country.population:
            return True
        else:
            return False

    def __str__(self):
        """
        :return: return a string contains the initialized country's population and size
        """
        return "The population density is " + self.population + " and " + self.size

    def __repr__(self):
        """
        :return: return the country's information input at __init__ method
        """
        return self