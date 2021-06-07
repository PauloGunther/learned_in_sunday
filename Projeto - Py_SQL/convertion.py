# FUNCOES DE CONVERSAO


# Converter decimal para octal
def to_octal(a):
    """
    Converte decimal para base octal
    :param a: valor a ser convertido
    :return: valor convertido
    """
    decimal = a
    octal = 0
    cont = 0
    aux = decimal
    
    while(aux > 0):
        octal += ((aux%8)*(10**cont))
        aux = int(aux/8)      
        cont += 1

    return octal


# Converter decimal para hexadecimal
def to_hex(a):
    """
    Converte decimal para base hexadecimal
    :param a: valor a ser convertido
    :return: valor convertido
    """
    dighex = "0123456789ABCDEF"
    x = (a % 16)
    resto = a // 16
    if (resto == 0):
        return dighex[x]
    return to_hex(resto) + dighex[x]


# Converter decimal para binariio  
def to_bin(a):
    """
    Converte decimal para base binario
    :param a: valor a ser convertido
    :return: valor convertido
    """
    x = a
    y = str(a%2)
    while x > 2:
        x = x // 2
        resto = x % 2
        y = str(resto) + y
    return y


# Converter binario em complemento de 1
def to_com1(a):
    """
    Converte decimal para complemente do binario
    :param a: valor a ser convertido
    :return: valor convertido
    """
    y = ''
    for dig in to_bin(a):
        if dig == '1':
            dig = '0'
        else:
            dig = '1'
        y = y + dig
    return y
