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

def ustvari_novo_knjiznico():
    Harry_Potter_in_kamen_modrosti = Knjiga('Harry Potter in kamen modrosti', 'J. K. Rowling', '1997', 'Prva knjiga v zbriki o mladem čarovniku, ki je obnorela svet.')
    Zlocin_in_kazen = Knjiga('Zločin in kazen', 'F. M. Dostojevski', '1866', 'Psihološki roman, ki obravnava predvsem subjektivna razmišljanja o življenju, zlasti pa o upravičenosti zločina.')
    Hobit = Knjiga('Hobit ali Tja in spet nazaj', 'J.R.R. Tolkien', '1937', 'Fantazijski roman kot predhodnik Gospodarja prstanov.')
    Umor_na_orient_ekspresu = Knjiga('Umor na Orient ekspresu', 'A. Christie', '1934', 'Eno najboljših del kraljice kriminalk, nova dogodivščina Hercula Poirota.')
    Grimmove_pravljice = Knjiga('Grimmove pravljice', 'J. in W. Grimm', '1812', 'Zbirka najzabavnejših pravljic, ki vas potopi v svet domišljije.')
    Ostrzek = Knjiga('Ostržek','C.Collodi', '1881', 'Klasika o dogodivščinah lesenega fantka.')
    Da_Vincijeva_koda = Knjiga('Da Vincijeva koda', 'D. Brown', '2003', 'Misteriozna zgodovinsko obarvana pustolovska drama, ki ne razočara.')
    knjiznica = Knjiznica()
    knjiznica.dodaj_knjigo(Harry_Potter_in_kamen_modrosti)
    knjiznica.dodaj_knjigo(Hobit)
    knjiznica.dodaj_knjigo(Zlocin_in_kazen)
    knjiznica.dodaj_knjigo(Umor_na_orient_ekspresu)
    knjiznica.dodaj_knjigo(Grimmove_pravljice)
    knjiznica.dodaj_knjigo(Ostrzek)
    knjiznica.dodaj_knjigo(Da_Vincijeva_koda)
    return knjiznica

def ustvari_slovar_naziva(knjiznica):
    slovar = {}
    for knjiga in knjiznica.seznam_knjig:
        slovar[knjiga.naslov] = knjiga
    return slovar

def ustvari_ime_za_v_slovar_naziva(niz):
    nov_niz = ''
    for crka in niz:
        if crka != ' ':
            nov_niz += crka
    return nov_niz

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Definiramo razred "Knjižnica".

class Knjiznica:
    def __init__(self):
        self.seznam_knjig = []

    def dodaj_knjigo(self, knjiga):
        self.seznam_knjig.append(knjiga)
    
    def izbrisi_knjigo(self, knjiga):
        self.seznam_knjig.remove(knjiga)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Definiramo razred "Knjiga".

class Knjiga:
    def __init__(self, naslov, avtor, leto_izdaje, opis):
        self.naslov = naslov
        self.avtor = avtor
        self.leto_izdaje = leto_izdaje
        self.opis = opis
        self.ocene = []
        self.komentarji = []
    
    def vrni_povprecno_oceno(self):
        return povprecje(self.ocene)
    
    def dodaj_oceno(self, dodana_ocena):
        self.ocene.append(dodana_ocena)

    def dodaj_komentar(self, nov_komentar):
        self.komentarji.append(nov_komentar)

    def izpisi_komentarje(self):
        return self.komentarji

