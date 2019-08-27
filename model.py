# Najprej dodamo slovarje vseh knjig in seznam le-teh, o katerih bomo lahko glasovali in komentirali. Ta slovar bomo lahko vnaprej še spreminjali.

seznam_knjig = []
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Tukaj so pomožne funkcije za lepši izgled programa.

def povprecje(seznam):
    if len(seznam) == 0:
        return 0
    else:
        vsota = 0
        for x in seznam:
            vsota += x
        return round(vsota / len(seznam), 1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Definiramo razred "Knjižnica".

class Knjiznica:
    def __init__(self):
        self.seznam_knjig = seznam_knjig

    def dodaj_knjigo(self, knjiga):
        seznam_knjig.append(knjiga)
    
    def izbrisi_knjigo(self, knjiga):
        seznam_knjig.remove(knjiga)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Definiramo razred "Knjiga".

class Knjiga:
    def __init__(self, naslov, avtor, leto_izdaje, opis):
        self.naslov = naslov
        self.avtor = avtor
        self.leto_izdaje = leto_izdaje
        self.opis = opis
        self.ocene = []
        self.povprecna_ocena = povprecje(self.ocene)
        self.komentarji = []
    
    def dodaj_oceno(self, dodana_ocena):
        self.ocene.append(dodana_ocena)

    def dodaj_komentar(self, nov_komentar):
        self.komentarji.append(nov_komentar)

    def izpisi_komentarje(self):
        return self.komentarji
    
    def izpisi_oceno(self):
        return self.povprecna_ocena

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# V seznam knjig dodamo nekaj knjig za lažji začetek.

Harry_Potter_in_kamen_modrosti = Knjiga('Harry Potter in kamen modrosti', 'J. K. Rowling', '1997', 'Prva knjiga v zbriki o mladem čarovniku, ki je obnorela svet.')
seznam_knjig.append(Harry_Potter_in_kamen_modrosti)
