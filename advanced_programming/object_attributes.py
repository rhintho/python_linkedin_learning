# Beispiel für Attributfunktionen von Instanzen

class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    def __getattr__(self, item):
        if item == "rgbcolor":
            return self.red, self.green, self.blue
        elif item == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key == "rgbcolor":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            super().__setattr__(key, value)

    def __dir__(self):
        return ("rgbcolor", "hexcolor")


def main():
    cls1 = MyColor()

    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    print(cls1.red)
    print(dir(cls1))


if __name__ == "__main__":
    main()
