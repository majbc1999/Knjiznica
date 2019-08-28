# Najprej uvozimo vse potrebno v tekstovni vmesnik.
from model import Knjiznica, Knjiga, povprecje

seznam_dejanj = []
# Dodamo nekaj knjig, da ne bo knjižnica na začetku dolgočasna.

Harry_Potter_in_kamen_modrosti = Knjiga('Harry Potter in kamen modrosti', 'J. K. Rowling', '1997', 'Prva knjiga v zbriki o mladem čarovniku, ki je obnorela svet.')
Zlocin_in_kazen = Knjiga('Zločin in kazen', 'F. M. Dostojevski', '1866', 'Psihološki roman, ki obravnava predvsem subjektivna razmišljanja o življenju, zlasti pa o upravičenosti zločina.')
Hobit = Knjiga('Hobit ali Tja in spet nazaj', 'J.R.R. Tolkien', '1937', 'Fantazijski roman kot predhodnik Gospodarja prstanov.')
Umor_na_orient_ekspresu = Knjiga('Umor na Orient ekspresu', 'A. Christie', '1934', 'Eno najboljših del kraljice kriminalk, nova dogodivščina Hercula Poirota.')
Grimmove_pravljice = Knjiga('Grimmove pravljice', 'J. in W. Grimm', '1812', 'Zbirka najzabavnejših pravljic, ki vas potopi v svet domišljije.')
Ostrzek = Knjiga('Ostržek','C.Collodi', '1881', 'Klasika o dogodivščinah lesenega fantka.')
Da_Vincijeva_koda = Knjiga('Da Vincijeva koda', 'D. Brown', '2003', 'Misteriozna zgodovinsko obarvana pustolovska drama, ki ne razočara.')

# Slovar naziva bo pomemben, da s pomočjo naslova knjige dobimo naziv le-te.
slovar_naziva = {
    'Harry Potter in kamen modrosti': Harry_Potter_in_kamen_modrosti,
    'Hobit ali Tja in spet nazaj': Hobit,
    'Zločin in kazen': Zlocin_in_kazen,
    'Umor na Orient ekspresu': Umor_na_orient_ekspresu,
    'Grimmove pravljice': Grimmove_pravljice,
    'Ostržek': Ostrzek,
    'Da Vincijeva koda': Da_Vincijeva_koda
}

# Ustvarimo našo začetno knjižnico.
knjiznica = Knjiznica()
knjiznica.dodaj_knjigo(Harry_Potter_in_kamen_modrosti)
knjiznica.dodaj_knjigo(Hobit)
knjiznica.dodaj_knjigo(Zlocin_in_kazen)
knjiznica.dodaj_knjigo(Umor_na_orient_ekspresu)
knjiznica.dodaj_knjigo(Grimmove_pravljice)
knjiznica.dodaj_knjigo(Ostrzek)
knjiznica.dodaj_knjigo(Da_Vincijeva_koda)

# Tukaj so vse funkcije, ki jih bomo potrebovali
def pozdrav():
    print('POZDRAVLJENI v vaši knjižnici knjig. Tukaj lahko dodajate že prebrane knjige, ter jih nato ocenjujete in jim napišete komentarje.')

def izberi_dejanje():
    print('Napiši številko pred dejanjem, ki ga hočeš izvesti:')
    print(' 1) izberi knjigo')
    print(' 2) oceni knjigo')
    print(' 3) dodaj novo knjigo')
    print(' 4) izbriši knjigo')
    dejanje = input('>')
    seznam_dejanj.append(dejanje)

def dodaj_novo_knjigo(naziv):
    naslov_v_funkciji = input('naslov >')
    avtor = input('avtor >')
    leto_izdaje = input('leto izdaje >')
    opis = input('opis >')
    naziv = Knjiga(naslov_v_funkciji, avtor, leto_izdaje, opis)
    knjiznica.dodaj_knjigo(naziv)
    print('Uspešno ste dodali knjigo!')

def izberi_knjigo():
    print('Za ogled opisa knjige, avtorja ter leta izdaje napiši NATANČEN naslov knjige.')
    for knjiga in knjiznica.seznam_knjig:
        print('  - ' + knjiga.naslov + ' (' + str(knjiga.vrni_povprecno_oceno()) + '/5.0)')
    izbira = input('>')
    if izbira in slovar_naziva:
        return slovar_naziva[izbira]
    else:
        return None

def ali_bomo_dodali_nov_komentar():
    print('Ali želite dodati nov komentar? (Odgovorite z DA ali NE)')
    izbira = input('>')
    if izbira == 'DA':
        return True
    elif izbira == 'NE':
        return False
    else:
        return 'Možna odgovora sta samo DA ali NE'

def besedilo_komentarja(knjiga):
    print('Napišite željen komentar:')
    nov_komentar = input('>')
    knjiga.dodaj_komentar(nov_komentar)
    print('Komentar uspešno dodan')

def odpri_podatke_o_knjigi(knjiga):
    if knjiga in knjiznica.seznam_knjig:
        print('......................................................................................................')
        print('NASLOV:  '+ knjiga.naslov)
        print('AVTOR:  ' + knjiga.avtor)
        print('LETO IZDAJE:  ' + knjiga.leto_izdaje)
        print('OPIS:  ' + knjiga.opis)
        print('............')
        print('KOMENTARJI:')
        if len(knjiga.komentarji) == 0:
            print('   >> Tukaj še ni bilo dodanih nobenih komentarjev!?')
        else:
            for x in knjiga.izpisi_komentarje():
                print('     - ' + str(x))
        if ali_bomo_dodali_nov_komentar():
            besedilo_komentarja(knjiga)
    elif knjiga == None:
        print('Ups, te knjige ni v tvoji knjižnici. Poskusi znova')
        print('--------------------------------------------------------------------------------------------------------')

def izberi_knjigo_za_oceno():
    print('Za dodajanje ocene knjige napiši NATANČEN naslov knjige.')
    for knjiga in knjiznica.seznam_knjig:
        print('  - ' + knjiga.naslov + ' (' + str(knjiga.vrni_povprecno_oceno()) + '/5.0)')
    izbira = input('>')
    if izbira in slovar_naziva:
        return slovar_naziva[izbira]
    else: return None

def oceni(knjiga):
    if knjiga == None:
        print('Ups, te knjige ni v tvoji knjižnici. Poskusi znova')
        print('--------------------------------------------------------------------------------------------------------')
    else:
        print('Podaj oceno za knjigo: {}'.format(knjiga.naslov))
        podana_ocena = input('>')
        if int(podana_ocena) < 0 or int(podana_ocena) > 5:
            print('Neveljavna ocena')
            print('--------------------------------------------------------------------------------------------------------')
        else:
            knjiga.ocene.append(int(podana_ocena))
            print('Ocena je bila uspešno podana.')



# To je funkcija, ki bo zagnala vse ostale funkcije.
def pozeni_knjiznico():
    while True:
        pozdrav()
        izberi_dejanje()
        if seznam_dejanj[-1] == '1':
            odpri_podatke_o_knjigi(izberi_knjigo())
        elif seznam_dejanj[-1] == '2':
            oceni(izberi_knjigo_za_oceno())
        elif seznam_dejanj[-1] == '3':
            pass
        elif seznam_dejanj[-1] == '4':
            pass
        else:
            print('Napačna izbira.')
            print('--------------------------------------------------------------------------------------------------------')

# Knjižnico še poženemo
pozeni_knjiznico()