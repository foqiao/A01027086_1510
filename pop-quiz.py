class name:
    def __init__(self, first, last="", middle=""):
        self.first = first
        self.middle = middle
        self.last = last

    def __str__(self):
        cap = self.first.title()
        cap1 = self.middle.title()
        cap2 = self.last.title()
        return "%s %s %s" % (cap, cap1, cap2)

    def __repr__(self):
        return self.__init__(self)

    def length(self):
        name_length = str(self.first) + str(self.middle) + str(self.last)
        return len(name_length)

def main():
    Donald_Trump = name("Donald", "Trump")
    Donald_Trump.__str__()
    Donald_Trump.__repr__()
    Donald_Trump.length()

if __name__ == '__main__':
    main()