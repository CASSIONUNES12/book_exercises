### 1

def f(x):
    """ Returns x ** 2
     :param x: int.
     :return:  int. x ao quadrado
     """
    return x ** 2
print(f(8))


### 2

def cassio(boca_juniors):
    """ Get a string as a paramter and show it. 
    :param boca_juniors: str.
    """
    print(boca_juniors)

cassio("DALE BOOO")

### 3

def f(a, b, c, x=12, y=20):
    """ Returns the sum from int.
    :param a: int. obrigatório
    :param b: int. obrigatório
    :param c: int. obrigatório
    :param x=12: int. opcional
    :param y=20: int. opcional
    :return: int.
    """
    return a + b + c + x + y
print(f(5, 4, 1))


### 4

def ff(a):
    """ Returns the division of an int
    :param a: int.
Untitled-1.txt
    
    """

    return a / 2

def sf(b):
    """ Returns the multiplication of an int
    :param b: int.
    :return: int.
    
    """
    return b * 4

x = ff(10)
y = sf(x)

print(y)

### 5

def cas(string):
    """Converts a string to int
       :param string: str.
       :return: string converted to int
    """
    return float(string)
try:
    print(cas(abc))
except (ValueError,NameError):
    print("Invalid input.")

