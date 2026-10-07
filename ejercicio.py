x = lambda a: a*2
y = lambda a: a.upper()

def mayusculas(frase: str)->str:
    """ Pone en mayusculas un string
    Args:
        frase (str): String a capitalizar
    Returns:
        str: String capitalizado
    """
    return frase.upper()

def doblar(num: int | float)->int | float:
    """ Doble de un numero
    Args:
        num (int | float): Numero a doblar
    Returns:
        int | float: Doble del numero
    """
    return num*2

# Lambdas
# Duplicar
print(f"{x(5)} {doblar(5)}")
print(f"{x(10.2)} {doblar(10.2)}")
print(f"{x('e')} {doblar('e')}")


# Capitalizar
print(f"{y("hola CARACOLA")} {mayusculas("hola CARACOLA")}")
print(f"{y("hola")} {mayusculas("hola")}")
print(f"{y("1")} {mayusculas("1")}")
print(f"{y(1)} {mayusculas(1)}")