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

def get_newton_sqrt(n,steps):
    '''
    Executa un nr dat de pasi pentru a calcula radicalul unui nr dat prin metoda lui newton
    :param n: float, numarul
    :param steps: float, numarul de pasi
    :return: radicalul numarului
    '''
    xo=2
    for i in range(steps):
        xo=xo-((xo*xo-n)/(2*xo))
    return xo

def test_get_newton():
    assert get_newton_sqrt(56,3)==7.672657176749704
    assert get_newton_sqrt(9,3)==3.000015360039322
    assert get_newton_sqrt(56234,59)==237.13709115193262

test_get_newton()

def invers(n):
    '''
    Returneaza inversul unui numar dat
    :param n: int, numarul nostru
    :return: inversul
    '''
    nr_inv=0
    while n!=0:
        nr_inv=nr_inv*10
        nr_inv+=n%10
        n=n//10
    return nr_inv
def is_antipalindrom(n):
    '''
    Verifica daca nr nostru este antipalindrom
    :param n: int, numarul dat
    :return: True daca numarul este antipalindrom si False in caz contrar
    '''
    inv=invers(n)
    for i in range(len(str(n))//2):
        if inv%10==n%10:
            return False
        n=n//10
        inv=inv//10
    return True

def test_is_antipalindrom():
    assert is_antipalindrom(2783)==True
    assert is_antipalindrom(2773)==False
    assert is_antipalindrom(567423)==True
test_is_antipalindrom()

def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()

