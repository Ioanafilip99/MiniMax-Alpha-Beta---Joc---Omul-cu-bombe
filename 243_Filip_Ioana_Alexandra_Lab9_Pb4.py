import time
from copy import deepcopy

def mutare_stanga(matr, jucator, i, j, protectii, mutare, k, x, y):

    coord_bomba = (x, y)
    matr_noua = []
    # daca este spatiu sau protectie atunci ne putem muta acolo
    if j - 1 > 0 and (matr[i][j - 1] == ' ' or matr[i][j - 1] == 'p'):

        matr_noua = deepcopy(matr)
        matr_noua[i][j - 1] = jucator

        # daca gasim protectie o luam
        if matr[i][j - 1] == 'p':
            protectii = protectii + 1

        # punem o bomba noua din k in k pasi
        if mutare % k == 0:
            # daca am o bomba inactiva, ea se activeaza automat
            if x != -1 and y != -1 and matr_noua[x][y] == 'b':
                matr_noua[x][y] = 'B'

            # punem bomba noua in urma si ii tinem minte indicii pt ca ea este noua bomba inactiva
            matr_noua[i][j] = 'b'
            coord_bomba = (i, j)

        else:
            matr_noua[i][j] = ' '

    return matr_noua, protectii, coord_bomba

def mutare_dreapta(matr, jucator, i, j, protectii, mutare, k, x, y):

    coord_bomba = (x, y)
    matr_noua = []

    if j + 1 < 22 and (matr[i][j + 1] == ' ' or matr[i][j + 1] == 'p'):

        matr_noua = deepcopy(matr)
        matr_noua[i][j + 1] = jucator

        if matr[i][j + 1] == 'p':
            protectii = protectii + 1

        if mutare % k == 0:
            if x != -1 and y != -1 and matr_noua[x][y] == 'b':
                matr_noua[x][y] = 'B'

            matr_noua[i][j] = 'b'
            coord_bomba = (i, j)

        else:
            matr_noua[i][j] = ' '

    return matr_noua, protectii, coord_bomba

def mutare_sus(matr, jucator, i, j, protectii, mutare, k, x, y):

    coord_bomba = (x, y)
    matr_noua = []

    if i - 1 > 0 and (matr[i - 1][j] == ' ' or matr[i - 1][j] == 'p'):

        matr_noua = deepcopy(matr)
        matr_noua[i - 1][j] = jucator

        if matr[i - 1][j] == 'p':
            protectii = protectii + 1

        if mutare % k == 0:
            if x != -1 and y != -1 and matr_noua[x][y] == 'b':
                matr_noua[x][y] = 'B'

            matr_noua[i][j] = 'b'
            coord_bomba = (i, j)

        else:
            matr_noua[i][j] = ' '

    return matr_noua, protectii, coord_bomba

def mutare_jos(matr, jucator, i, j, protectii, mutare, k, x, y):

    coord_bomba = (x, y)
    matr_noua = []

    if i + 1 < 12 and (matr[i + 1][j] == ' ' or matr[i + 1][j] == 'p'):

        matr_noua = deepcopy(matr)
        matr_noua[i + 1][j] = jucator

        if matr[i + 1][j] == 'p':
            protectii = protectii + 1

        if mutare % k == 0:
            if x != -1 and y != -1 and matr_noua[x][y] == 'b':
                matr_noua[x][y] = 'B'

            matr_noua[i][j] = 'b'
            coord_bomba = (i, j)

        else:
            matr_noua[i][j] = ' '

    return matr_noua, protectii, coord_bomba

class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_LINII = 12
    NR_COLOANE = 22
    JMIN = None
    JMAX = None
    GOL = '#'
    harta = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '1', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', '#', '#', '#', ' ', ' ', '#', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', '#', ' ', '#'],
            ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
            ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', 'p', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
            ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 'p', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', 'p', '2', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
    # la fiecare k pasi ambii jucatori pun o bomba
    k = 5

    def __init__(self, tabla=None, protectii = 0, mutare = 0, coord_bomba = (-1, -1)):
        self.matr = tabla or self.harta
        self.protectii_jucator = protectii
        self.index_mutare = mutare
        self.bomba_inactiva = coord_bomba

    def explozie(self, jucator):

        for x in range(0, 12):
            for y in range(0, 22):
                if self.matr[x][y] == jucator:

                    # verific daca am bomba pe coloana y
                    # ma plimb pe linii
                    for i in range(0, 12):
                        if self.matr[i][y] == 'B':
                            perete = 0
                            # verific daca exista perete intre jucator si bomba
                            if i < x:   # bomba e deasupra mea
                                for j in range(i + 1, x):
                                    if self.matr[j][y] == '#':
                                        perete = 1
                                        break
                            else: # bomba e sub mine
                                for j in range(x + 1, i):
                                    if self.matr[j][y] == '#':
                                        perete = 1
                                        break
                            # daca nu exista perete, verific daca am protectie sa o folosesc
                            if perete == 0:
                                return True

                    # verific daca am bomba pe linia x
                    # ma plimb pe coloane
                    for i in range(0, 22):
                        if self.matr[x][i] == 'B':
                            perete = 0
                            if i < y:   # bomba e la stanga
                                for j in range(i + 1, y):
                                    if self.matr[x][j] == '#':
                                        perete = 1
                                        break
                            else:   # bomba e la dreapta
                                for j in range(y + 1, i):
                                    if self.matr[x][j] == '#':
                                        perete = 1
                                        break
                            if perete == 0:
                                return True
        return False

    def final(self):    # jocul se opreste atunci cand jucatorul e in dreptul unei bombe care il va exploda
                        # sau cand calculatoruk nu mai are mutari de facut (el alege doar mutarile care nu il expun la o bomba)

        protectii_JMIN = Joc.protectii_jucator

        if self.explozie(self.JMIN) == True:
            if protectii_JMIN <= 0:
                return self.JMAX
            else:
                Joc.protectii_jucator = protectii_JMIN - 1

        elif len(self.mutari_joc(self.JMAX)) == 0:
            return self.JMIN

        return None

    def mutari_joc(self, jucator):
        """
        Pentru configuratia curenta de joc "self.matr" (de tip lista, cu 9 elemente),
        trebuie sa returnati o lista "l_mutari" cu elemente de tip Joc,
        corespunzatoare tuturor configuratiilor-succesor posibile.

        "jucator" este simbolul jucatorului care face mutarea
        """
        l_mutari = []

        for i in range(0, 12):
            for j in range(0, 22):
                if self.matr[i][j] == jucator:

                    # stanga

                    if j - 1 > 0 and (self.matr[i][j - 1] == ' ' or self.matr[i][j - 1] == 'p'):

                        mutare = self.index_mutare + 1
                        protectii = self.protectii_jucator
                        k = self.k

                        c1 = self.bomba_inactiva[0]
                        c2 = self.bomba_inactiva[1]

                        explodat = 0

                        # verificam daca mutarea ne expune la o bomba
                        for l in range(0, 12):
                            if self.matr[l][j-1] == 'B':
                                perete = 0
                                if l < i:   # daca bomba e deasupra
                                    for x in range(l+1, i):
                                        if self.matr[x][j-1] == '#':
                                            perete = 1
                                            break
                                else:   # daca bomba e sub
                                    for x in range(i+1, l):
                                        if self.matr[x][j-1] == '#':
                                            perete = 1
                                            break
                                if perete == 0:
                                    if self.protectii_jucator > 0:
                                        self.protectii_jucator -= 1
                                    else:
                                        explodat = 1

                        # daca nu dam de o bomba care sa ne arunce in aer
                        # sau daca dam dar avem protectie
                        # atunci facem mutarea
                        if explodat == 0:
                            matr_noua, protectii, coord_bomba = mutare_stanga(self.matr, jucator, i, j, protectii, mutare,
                                                                              k, c1, c2)
                            l_mutari.append(Joc(matr_noua, protectii, mutare, coord_bomba))

                    # dreapta

                    if j + 1 < 22 and (self.matr[i][j + 1] == ' ' or self.matr[i][j + 1] == 'p'):

                        mutare = self.index_mutare + 1
                        protectii = self.protectii_jucator
                        k = self.k
                        coord_bomba = self.bomba_inactiva
                        c1 = coord_bomba[0]
                        c2 = coord_bomba[1]

                        explodat = 0
                        # verificam daca mutarea ne expune la o bomba
                        for l in range(0, 12):
                            if self.matr[l][j + 1] == 'B':
                                perete = 0
                                if l < i:  # daca bomba e deasupra
                                    for x in range(l + 1, i):
                                        if self.matr[x][j + 1] == '#':
                                            perete = 1
                                            break
                                else:  # daca bomba e sub
                                    for x in range(i + 1, l):
                                        if self.matr[x][j + 1] == '#':
                                            perete = 1
                                            break
                                if perete == 0:
                                    if self.protectii_jucator > 0:
                                        self.protectii_jucator -= 1
                                    else:
                                        explodat = 1

                        # daca nu dam de o bomba care sa ne arunce in aer
                        # sau daca dam dar avem protectie
                        # atunci facem mutarea
                        if explodat == 0:
                            matr_noua, protectii, coord_bomba = mutare_dreapta(self.matr, jucator, i, j,
                                                                              protectii, mutare,
                                                                              k, c1, c2)
                            l_mutari.append(Joc(matr_noua, protectii, mutare, coord_bomba))

                    # sus

                    if i - 1 > 0 and (self.matr[i - 1][j] == ' ' or self.matr[i - 1][j] == 'p'):

                        mutare = self.index_mutare + 1
                        protectii = self.protectii_jucator
                        k = self.k
                        coord_bomba = self.bomba_inactiva
                        c1 = coord_bomba[0]
                        c2 = coord_bomba[1]

                        explodat = 0
                        # verificam daca mutarea ne expune la o bomba
                        for l in range(0, 22):
                            if self.matr[i - 1][l] == 'B':
                                perete = 0
                                if l < j:  # daca bomba e la stanga
                                    for x in range(l + 1, j):
                                        if self.matr[i - 1][x] == '#':
                                            perete = 1
                                            break
                                else:  # daca bomba e la dreapta
                                    for x in range(j + 1, l):
                                        if self.matr[i - 1][x] == '#':
                                            perete = 1
                                            break
                                if perete == 0:
                                    if self.protectii_jucator > 0:
                                        self.protectii_jucator -= 1
                                    else:
                                        explodat = 1

                        # daca nu dam de o bomba care sa ne arunce in aer
                        # sau daca dam dar avem protectie
                        # atunci facem mutarea
                        if explodat == 0:
                            matr_noua, protectii, coord_bomba = mutare_sus(self.matr, jucator, i, j,
                                                                              protectii, mutare,
                                                                              k, c1, c2)
                            l_mutari.append(Joc(matr_noua, protectii, mutare, coord_bomba))

                    # jos

                    if i + 1 > 0 and (self.matr[i + 1][j] == ' ' or self.matr[i + 1][j] == 'p'):

                        mutare = self.index_mutare + 1
                        protectii = self.protectii_jucator
                        k = self.k
                        coord_bomba = self.bomba_inactiva
                        c1 = coord_bomba[0]
                        c2 = coord_bomba[1]

                        explodat = 0
                        # verificam daca mutarea ne expune la o bomba
                        for l in range(0, 22):
                            if self.matr[i + 1][l] == 'B':
                                perete = 0
                                if l < j:  # daca bomba e la stanga
                                    for x in range(l + 1, j):
                                        if self.matr[i + 1][x] == '#':
                                            perete = 1
                                            break
                                else:  # daca bomba e la dreapta
                                    for x in range(j + 1, l):
                                        if self.matr[i + 1][x] == '#':
                                            perete = 1
                                            break
                                if perete == 0:
                                    if self.protectii_jucator > 0:
                                        self.protectii_jucator -= 1
                                    else:
                                        explodat = 1

                        # daca nu dam de o bomba care sa ne arunce in aer
                        # sau daca dam dar avem protectie
                        # atunci facem mutarea
                        if explodat == 0:
                            matr_noua, protectii, coord_bomba = mutare_jos(self.matr, jucator, i, j,
                                                                              protectii, mutare,
                                                                              k, c1, c2)
                            l_mutari.append(Joc(matr_noua, protectii, mutare, coord_bomba))

        return l_mutari

    def estimeaza_scor(self, jucator):
        if jucator == self.JMAX:    # nr de protectii ale calculatorului
            return self.protectii_jucator
        else:                       # nr de protecii ale jucatorului
            return Joc.protectii_jucator

    def __str__(self):
        sir = ''
        for j in range(0, 12):
            for i in range(0, 22):
                sir += str(self.matr[j][i])
            sir += '\n'
        return sir


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari_joc() care ofera lista cu
    configuratiile posibile in urma mutarii unui jucator
    """

    ADANCIME_MAX = None

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, scor=None):
        self.tabla_joc = tabla_joc  # un obiect de tip Joc => „tabla_joc.matr”
        self.j_curent = j_curent  # simbolul jucatorului curent

        # adancimea in arborele de stari
        #	(scade cu cate o unitate din „tata” in „fiu”)
        self.adancime = adancime

        # scorul starii (daca e finala, adica frunza a arborelui)
        # sau scorul celei mai bune stari-fiice (pentru jucatorul curent)
        self.scor = scor

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []  # lista va contine obiecte de tip Stare

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def jucator_opus(self):
        if self.j_curent == Joc.JMIN:
            return Joc.JMAX
        else:
            return Joc.JMIN

    def mutari_stare(self):
        l_mutari = self.tabla_joc.mutari_joc(self.j_curent)
        juc_opus = self.jucator_opus()

        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]
        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent:" + self.j_curent + ")\n"
        return sir


""" Algoritmul MinMax """


def min_max(stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.j_curent)
        return stare

    # Altfel, calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari_stare()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutari_scor = [min_max(mutare) for mutare in stare.mutari_posibile]

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu scorul maxim
        stare.stare_aleasa = max(mutari_scor, key=lambda x: x.scor)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu scorul minim
        stare.stare_aleasa = min(mutari_scor, key=lambda x: x.scor)

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    # Daca am ajuns la o frunza a arborelui, adica:
    # - daca am expandat arborele pana la adancimea maxima permisa
    # - sau daca am ajuns intr-o configuratie finala de joc
    if stare.adancime == 0 or stare.tabla_joc.final():
        # calculam scorul frunzei apeland "estimeaza_scor"
        stare.scor = stare.tabla_joc.estimeaza_scor(stare.j_curent)
        return stare

    # Conditia de retezare:
    if alpha >= beta:
        return stare  # este intr-un interval invalid, deci nu o mai procesez

    # Calculez toate mutarile posibile din starea curenta (toti „fiii”)
    stare.mutari_posibile = stare.mutari_stare()

    if stare.j_curent == Joc.JMAX:
        scor_curent = float('-inf')  # scorul „tatalui” de tip MAX

        # pentru fiecare „fiu” de tip MIN:
        for mutare in stare.mutari_posibile:
            # calculeaza scorul fiului curent
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (cresc) scorul si alfa
            # „tatalui” de tip MAX, folosind scorul fiului curent
            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if alpha < stare_noua.scor:
                alpha = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MIN


    elif stare.j_curent == Joc.JMIN:
        scor_curent = float('inf')  # scorul „tatalui” de tip MIN

        # pentru fiecare „fiu” de tip MAX:
        for mutare in stare.mutari_posibile:
            stare_noua = alpha_beta(alpha, beta, mutare)

            # incerc sa imbunatatesc (scad) scorul si beta
            # „tatalui” de tip MIN, folosind scorul fiului curent
            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

            if beta > stare_noua.scor:
                beta = stare_noua.scor
                if alpha >= beta:  # verific conditia de retezare
                    break  # NU se mai extind ceilalti fii de tip MAX

    # actualizez scorul „tatalui” = scorul „fiului” ales
    stare.scor = stare.stare_aleasa.scor

    return stare

def afis_daca_final(stare_curenta):
    final = stare_curenta.tabla_joc.final()
    if (final):
        if (final == "remiza"):
            print("Remiza!")
        else:
            print("A castigat " + final)
        return True
    return False

def main():

    raspuns_valid = False
    tip_algoritm = '1'
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-Beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    raspuns_valid = False
    while not raspuns_valid:
        print("Alege dificultatea")
        print("\t1 = Incepator")
        print("\t2 = Mediu")
        print("\t3 = Avansat")

        dificultate = int(input())

        if dificultate == 1:
            Stare.ADANCIME_MAX = 3
            raspuns_valid = True
        elif dificultate == 2:
            Stare.ADANCIME_MAX = 4
            raspuns_valid = True
        elif dificultate == 3:
            Stare.ADANCIME_MAX = 5
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")

    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu 1 sau cu 2? ")
        if Joc.JMIN in ['1', '2']:
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie 1 sau 2.")

    # inceputul jocului
    start = int(round(time.time() * 1000))

    # initializare jucatori
    if Joc.JMIN == '1':
        pozitie_jucator = (1, 1)   # se afla in stanga sus
        Joc.JMAX = '2'
    else:
        pozitie_jucator = (10, 20)  # se afla in dreapta jos
        Joc.JMAX = '1'
    Joc.protectii_jucator = 0
    Joc.index_mutare = 0
    Joc.bomba_inactiva = (-1, -1)


    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, Joc.JMIN, Stare.ADANCIME_MAX)

    while True:
        if stare_curenta.j_curent == Joc.JMIN:  # jucatorul e JMIN
            inainte = int(round(time.time() * 1000))
            i = pozitie_jucator[0]
            j = pozitie_jucator[1]

            nr_protectii = Joc.protectii_jucator
            Joc.index_mutare += 1
            mutare = Joc.index_mutare
            k = Joc.k
            x = Joc.bomba_inactiva[0]
            y = Joc.bomba_inactiva[1]

            raspuns_valid = False
            while not raspuns_valid:
                try:

                    directie = input("\nAlege mutarea (w,a,s,d) ")

                    if directie == "exit":
                        print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMAX))
                        print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMIN))
                        finish = int(round(time.time() * 1000))
                        print("Jocul a durat ", finish-start)
                        print("Jucatorul ", Joc.JMIN, " a facut ", mutare - 1, " mutari.")
                        print("Jucatorul ", Joc.JMAX, " a facut ", mutare - 1, " mutari.")
                        return

                    if directie in ['w','a','s','d']:

                        matr_n = []
                        coord_b = (-1,-1)

                        if directie == 'a':
                            matr_n, nr_protectii, coord_b = mutare_stanga(stare_curenta.tabla_joc.matr, Joc.JMIN, i, j, nr_protectii, mutare, k, x, y)
                            pozitie_jucator = (i, j - 1)

                        elif directie == 'd':
                            matr_n, nr_protectii, coord_b = mutare_dreapta(stare_curenta.tabla_joc.matr, Joc.JMIN, i, j, nr_protectii, mutare, k, x, y)
                            pozitie_jucator = (i, j + 1)

                        elif directie == 'w':
                            matr_n, nr_protectii, coord_b = mutare_sus(stare_curenta.tabla_joc.matr, Joc.JMIN, i, j, nr_protectii, mutare, k, x, y)
                            pozitie_jucator = (i - 1, j)

                        elif directie == 's':
                            matr_n, nr_protectii, coord_b = mutare_jos(stare_curenta.tabla_joc.matr, Joc.JMIN, i, j, nr_protectii, mutare, k, x, y)
                            pozitie_jucator = (i + 1, j)

                        Joc.protectii_jucator = nr_protectii

                        if coord_b != (-1, -1):
                            Joc.bomba_inactiva = coord_b
                        x = Joc.bomba_inactiva[0]
                        y = Joc.bomba_inactiva[1]


                        if x != -1 and y != -1: # daca avem o bomba inactiva

                            raspuns_valid1 = False
                            while not raspuns_valid1:

                                activare_bomba = input("Vrei sa activezi ultima bomba? (y/n) ")

                                if activare_bomba == "exit":
                                    print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMAX))
                                    print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMIN))
                                    finish = int(round(time.time() * 1000))
                                    print("Jocul a durat ", finish - start)
                                    print("Jucatorul ", Joc.JMIN, " a facut ", mutare - 1, " mutari.")
                                    print("Jucatorul ", Joc.JMAX, " a facut ", mutare - 1, " mutari.")
                                    return

                                elif activare_bomba == 'y':
                                    raspuns_valid1 = True
                                    if matr_n[x][y] == 'b':
                                        matr_n[x][y] = 'B'
                                        x = -1
                                        y = -1
                                        Joc.bomba_inactiva = (x, y)

                                elif activare_bomba == 'n':
                                    raspuns_valid1 = True

                                    raspuns_valid2 = False
                                    while not raspuns_valid2:

                                        bomba_noua = input("Vrei sa pui o bomba noua? (y/n) ")
                                        if bomba_noua == "exit":
                                            print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMAX))
                                            print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMIN))
                                            finish = int(round(time.time() * 1000))
                                            print("Jocul a durat ", finish - start)
                                            print("Jucatorul ", Joc.JMIN, " a facut ", mutare - 1, " mutari.")
                                            print("Jucatorul ", Joc.JMAX, " a facut ", mutare - 1, " mutari.")
                                            return
                                        elif bomba_noua == 'y':
                                            raspuns_valid2 = True
                                            if matr_n[x][y] == 'b':  # inseamna ca am bomba inactiva
                                                matr_n[x][y] = 'B'
                                            matr_n[i][j] = 'b'
                                            x = i
                                            y = j
                                            Joc.bomba_inactiva = (x, y)
                                        elif bomba_noua == 'n':
                                            raspuns_valid2 = True

                        else:

                            if coord_b == (-1,-1) or matr_n[coord_b[0]][coord_b[1]] == 'B': # daca nu avem bomba inactiva

                                raspuns_valid3 = False
                                while not raspuns_valid3:

                                    bomba_noua = input("Vrei sa pui o bomba noua? (y/n) ")
                                    if bomba_noua == "exit":
                                        print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMAX))
                                        print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMIN))
                                        finish = int(round(time.time() * 1000))
                                        print("Jocul a durat ", finish - start)
                                        print("Jucatorul ", Joc.JMIN, " a facut ", mutare - 1, " mutari.")
                                        print("Jucatorul ", Joc.JMAX, " a facut ", mutare - 1, " mutari.")
                                        return
                                    elif bomba_noua == 'y':
                                        raspuns_valid3 = True
                                        if matr_n[x][y] == 'b':  # inseamna ca am bomba inactiva
                                            matr_n[x][y] = 'B'
                                        matr_n[i][j] = 'b'
                                        x = i
                                        y = j
                                        Joc.bomba_inactiva = (x, y)
                                    elif bomba_noua == 'n':
                                        raspuns_valid3 = True

                        Joc.matr = matr_n
                        raspuns_valid = matr_n
                        if not raspuns_valid:
                            print("Mutare imposibila!")

                    else:
                        print("Mutare invalida!")


                except ValueError:
                    print("Trebuie sa alegi din mutarile a, d, w, s! Doriti sa iesiti (y/n)?")
                    exit_func = input()
                    if exit_func == 'y':
                        print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMAX))
                        print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMIN))
                        finish = int(round(time.time() * 1000))
                        print("Jocul a durat ", finish - start)
                        print("Jucatorul ", Joc.JMIN, " a facut ", mutare - 1, " mutari.")
                        print("Jucatorul ", Joc.JMAX, " a facut ", mutare - 1, " mutari.")
                        return

            # dupa while sigur am mutare valida, deci actualizez tabla de joc
            stare_curenta.tabla_joc.matr = raspuns_valid

            # afisarea starii jocului in urma mutarii utilizatorului
            print("Tabla dupa mutarea jucatorului")
            print(str(stare_curenta))
            print("Scor jucator:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMIN))

            dupa = int(round(time.time() * 1000))
            print("Jucatorul a gandit timp de " + str(dupa - inainte) + " milisecunde.\n")

            # daca jocul a ajuns intr-o stare finala
            if afis_daca_final(stare_curenta):
                finish = time.time()
                print("Jocul a durat ", finish - start)
                print("Jucatorul ", Joc.JMIN, " a facut ", mutare, " mutari.")
                print("Jucatorul ", Joc.JMAX, " a facut ", mutare - 1, " mutari.")
                break

            # jucatorul curent devine adversarul
            stare_curenta.j_curent = stare_curenta.jucator_opus()


        else:  # jucatorul e JMAX (calculatorul)

            inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)

            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))
            print("Scor computer:", stare_curenta.tabla_joc.estimeaza_scor(Joc.JMAX))

            dupa = int(round(time.time() * 1000))
            print("Calculatorul a gandit timp de " + str(dupa - inainte) + " milisecunde.")

            if afis_daca_final(stare_curenta):
                finish = time.time()
                print("Jocul a durat ", finish - start)
                print("Jucatorul ", Joc.JMIN, " a facut ", mutare, " mutari.")
                print("Jucatorul ", Joc.JMAX, " a facut ", mutare, " mutari.")
                break

            # jucatorul curent devine adversarul
            stare_curenta.j_curent = stare_curenta.jucator_opus()

if __name__ == "__main__":
    main()