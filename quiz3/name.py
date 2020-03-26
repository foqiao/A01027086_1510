class name:

    def __init__(self, first_name, last_name, middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def change_name(self, new_first, new_middle, new_last):
        if new_first != self.first_name:
            self.first_name = new_first
        if new_last != self.last_name:
            self.last_name = new_last
        if new_last != self.middle_name:
            self.middle_name = new_middle
        try:
            new_first = 1
            new_first = 1.12
        except TypeError:
            print("No!")

    def __str__(self):
        print(str(self.first_name.title()) + " " + str(self.middle_name.title()) + " " + str(self.last_name.title()))

    def __repr__(self):
        print("Name(%s %s %s)" % (str(self.first_name.title()), str(self.middle_name.title()),
                                  str(self.last_name.title())))

def main():
    Donald_Trump = name("Donald", "Trump", "John")
    Donald_Trump.__str__()
    Donald_Trump.__repr__()

if __name__ == '__main__':
    main()