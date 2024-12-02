ANSI_PREFIX = "\u001b"
RESET = f"{ANSI_PREFIX}[0m"

class Color:
    """Mostly stolen from https://github.com/DanielTheFletch/color50/tree/main"""

    @classmethod
    def red(cls):
        return Color(255,0,0)

    @classmethod
    def green(cls):
        return Color(0,255,0)

    @classmethod
    def blue(cls):
        return Color(0,0,255)

    @classmethod
    def clear(cls):
        return  "\u001b[0m"

    def __init__(self, r, g, b, style=None):
        if not 0 <= r <= 255:
            raise ValueError("r %d not in range [0, 255]" % (r))
        if not 0 <= g <= 255:
            raise ValueError("r %d not in range [0, 255]" % (g))
        if not 0 <= b <= 255:
            raise ValueError("r %d not in range [0, 255]" % (b))

        self.r = r
        self.g = g
        self.b = b
        self.style = style
        self.tmpstring = ''

    def __str__(self) -> str:
        tmp = self.fg() if not self.tmpstring else self.tmpstring + self.fg()
        self.tmpstring = "" # you get one shot, one opportunity
        return tmp

    def __add__(self, string: str) -> str:
        """ color + 'hello' """
        if isinstance(string, str):
            return str(self) + string
        else:
            raise TypeError("Unsupported type for addition {}".format(other))

    def __radd__(self, other) -> str:
        """ 'hello' + color """
        if isinstance(other, str):
            self.tmpstring = other
            return self
        else:
            raise TypeError("Unsupported type for r-addition {}".format(other))

    def __call__(self, other) -> str:
            return self.fg() + other + RESET

    def fg(self) -> str:
        rgb = f"{self.r};{self.g};{self.b}"
        return f"{ANSI_PREFIX}[38;2;{rgb}m"
    
    # def bg(self) -> str:
    #     rgb = f"{self.r};{self.g};{self.b}"
    #     return f"{ANSI_PREFIX}[48;2;{rgb}m"


def example():
    c = Color(255,255,255)
    c2 = Color(255,0,255)
    c3 = Color.red()
    print(c + 'hello')
    print(c + 'hello' + c2 + 'hello2' + c3 + 'asdf' + 'asdffdsa' + Color.blue() + 'fffff')
    print('hello' + c) # will retain color, because 
    print('hello' + c + Color.clear() + 'mello' + c)
    print(Color.clear())
    print(Color.blue()('yello') + 'bitches')

