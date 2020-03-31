import self


class Country:
    def __init__(self, name, population, size):
        """
        store the three different information about a country
        :param name: country's name
        :param population: country's population
        :param size: country's size
        >>> Canada = Country("Canada", 37950000, 998500)
        """
        self.__name = name
        self.__population = population
        self.__size = size

    def is_larger(self, country):
        """
        compare the initialized country and country in the parameter about their population masses
        :param country: compared country
        :return: which country is larger in population
        >>> country = Denmark
        >>> Country.is_larger()
        """
        if self.__population > country.__population:
            return True
        else:
            return False

    def __str__(self):
        """
        :return: return a string contains the initialized country's population and size
        """
        return "The population density is " + self.__population + " and " + self.__size

    def population_density(self):
        """
        calculate the density of the population in a specific country
        :return: return population density
        """
        density = self.__population / self.__size
        return density

    def __repr__(self):
        """
        return the string represent the object of the self parameter
        :return: return the string represent the object
        """
        return "%s has a population of %d and is %d square kilometer" % (self.__name, self.__population, self.__size)

def main():
    # Canada = Country("Canada", 37950000, 998500)
    # Denmark = Country("Denmark", 300000, 40000)
    # Canada = Country.__population
    # Denmark = Country.__population
    # Canada.is_larger(Denmark)
    # Canada.population_density(Canada)
    # Canada.__repr__(Canada)
    # Canada.__str__(Canada)
    Canada = Country("Canada", 37950000, 998500)
    Denmark = Country("Denmark", 300000, 40000)
    print(Canada.is_larger(Denmark))
    print(Canada.population_density())
    print(Canada.__repr__())
    print(Canada.__str__())



if __name__ == '__main__':
    main()