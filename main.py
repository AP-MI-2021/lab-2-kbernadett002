def is_palindrom(n):
    '''
    Determina daca un nr este palindrom
    :param n: int, un numar
    :return: True daca este palindrom si False in caz contrar
    '''
    oglindit_n=0
    copie_n=n
    while n!=0:
        oglindit_n=oglindit_n*10+n%10
        n=n//10
    if oglindit_n==copie_n:
        return True
    else:
        return False

def test_is_palindrom():
    assert is_palindrom(232)==True
    assert is_palindrom(2356987) == False
    assert is_palindrom(123321) == True

test_is_palindrom()