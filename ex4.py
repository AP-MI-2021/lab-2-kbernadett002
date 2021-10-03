def get_newton_sqrt(n,steps):
    '''
    Executa un nr dat de pasi pentru a calcula radicalul unui nr dat prin metoda lui newton
    :param n: float, numarul
    :param steps: float, numarul de pasi
    :return: radicalul numarului
    '''
    copie_n=n
    for i in range(2,steps):
        copie_n=copie_n-((copie_n*copie_n-n)/(2*copie_n))
    return copie_n
nr=get_newton_sqrt(56,3)
print(nr)
