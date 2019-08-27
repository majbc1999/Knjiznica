# Najprej dodamo slovarje vseh knjig in seznam le-teh, o katerih bomo lahko glasovali in komentirali. Ta slovar bomo lahko vnaprej še spreminjali.

seznam_knjig = [
    'Harry Potter in kamen modrosti', 
    'Zločin in kazen', 
    'Hobit ali Tja in spet nazaj', 
    'Umor na Orient ekspresu', 
    'Grimmove pravljice', 
    'Ostržek',
    'Da Vincijeva koda'
]

slovar_avtorjev = {
    'Harry Potter in kamen modrosti': 'J. K. Rowling',
    'Zločin in kazen': 'F. M. Dostojevski',
    'Hobit ali Tja in spet nazaj': 'J.R.R. Tolkien',
    'Umor na Orient ekspresu': 'A. Christie',
    'Grimmove pravljice': 'J. in W. Grimm',
    'Ostržek': 'C.Collodi',
    'Da Vincijeva koda': 'D. Brown'
}

slovar_letnic = {
    'Harry Potter in kamen modrosti': '1997',
    'Zločin in kazen': '1866', 
    'Umor na Orient ekspresu': '1934',
    'Grimmove pravljice': '1812',
    'Ostržek': '1881',
    'Da Vincijeva koda': '2003'
}

slovar_opisov = {
    'Harry Potter in kamen modrosti': 'Prva knjiga v zbriki o mladem čarovniku, ki je obnorela svet.',
    'Zločin in kazen': 'Psihološki roman, ki obravnava predvsem subjektivna razmišljanja o življenju, zlasti pa o upravičenosti zločina.',
    'Hobit ali Tja in spet nazaj': 'Fantazijski roman kot predhodnik Gospodarja prstanov.',
    'Umor na Orient ekspresu': 'Eno najboljših del kraljice kriminalk, nova dogodivščina Hercula Poirota.',
    'Grimmove pravljice': 'Zbirka najzabavnejših pravljic, ki vas potopi v svet domišljije.',
    'Ostržek': 'Klasika o dogodivščinah lesenega fantka.',
    'Da Vincijeva koda': 'Misteriozna zgodovinsko obarvana pustolovska drama, ki ne razočara.'
}

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
        seznam_knjig.append(knjiga.naslov())
        slovar_avtorjev[knjiga.naslov()] = knjiga.avtor()
        slovar_letnic[knjiga.naslov()] = knjiga.leto_izdaje()
        slovar_opisov[knjiga.naslov()] = knjiga.opis()
    
    def izbrisi_knjigo(self, naslov):
        seznam_knjig.remove(naslov)
        del slovar_avtorjev[naslov]
        del slovar_letnic[naslov]
        del slovar_opisov[naslov]

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