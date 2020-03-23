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
        return name.__init__(self)

    def length(self):
        return len(self)