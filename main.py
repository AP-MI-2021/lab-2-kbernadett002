def is_palindrome(n):
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

def test_is_palindrome():
    assert is_palindrome(232)==True
    assert is_palindrome(2356987) == False
    assert is_palindrome(123321) == True

test_is_palindrome()

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

def test_get_newton_sqrt():
    assert get_newton_sqrt(56,3)==7.672657176749704
    assert get_newton_sqrt(9,3)==3.000015360039322
    assert get_newton_sqrt(56234,59)==237.13709115193262

test_get_newton_sqrt()


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
def is_antipalindrome(n):
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

def test_is_antipalindrome():
    assert is_antipalindrome(2783)==True
    assert is_antipalindrome(2773)==False
    assert is_antipalindrome(567423)==True
test_is_antipalindrome()

def main():
  x=input('''1-is_palindrom 2-get_newtom_sqrt 3-is_antipalindrome 4-final''')
  while x!='4':
      if x=='1':
          test_is_palindrome()
      elif x=='2':
          test_get_newton_sqrt()
      elif x=='3':
          test_is_antipalindrome()


if __name__ == '__main__':
  main()

