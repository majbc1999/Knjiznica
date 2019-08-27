# Najprej dodamo slovar vseh knjig, o katerih bomo lahko glasovali in komentirali. Ta slovar bomo lahko vnaprej še spreminjali.

slovar = {
    'Harry Potter in kamen modrosti': ('J. K. Rowling', '1997', 'Prva knjiga v zbriki o mladem čarovniku, ki je obnorela svet.'),
    'Zločin in kazen': ('F. M. Dostojevski', '1866', 'Psihološki roman, ki obravnava predvsem subjektivna razmišljanja o življenju, zlasti pa o upravičenosti zločina.'),
    'Hobit ali Tja in spet nazaj': ('J.R.R. Tolkien', '1937', 'Fantazijski roman kot predhodnik Gospodarja prstanov.'),
    'Umor na Orient ekspresu': ('A. Christie', '1934', 'Eno najboljših del kraljice kriminalk, nova dogodivščina Hercula Poirota.'),
    'Grimmove pravljice': ('J. in W. Grimm', '1812', 'Zbirka najzabavnejših pravljic, ki vas potopi v svet domišljije.'),
    'Ostržek': ('C.Collodi', '1881', 'Klasika o dogodivščinah lesenega fantka.'),
    'Da Vincijeva koda': ('D. Brown', '2003', 'Misteriozna zgodovinsko obarvana pustolovska drama, ki ne razočara.'),
}

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Tukaj so pomožne funkcije za lepši izgled programa.

def povprecje(seznam):
    if len(seznam) = 0:
        return 0
    else:
        vsota = 0
        for x in seznam:
            vsota += x
        return round(vsota / len(seznam), 1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Definiramo razred "Knjižnica".

class Knjiznica:
    def __init__(self, uporabnik, slovar):
        self.uporabnik = uporabnik
        self.slovar = slovar

    def dodaj_knjigo(self, naslov, avtor, leto_izdaje, opis):
        if naslov in self.slovar:
            return 'Ta knjiga je že v tvoji knjižnici. Poskusi znova!'
        else:
            self.slovar[naslov]: (avtor, str(leto_izdaje), opis)

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