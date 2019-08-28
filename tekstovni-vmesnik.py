# Najprej uvozimo vse potrebno v tekstovni vmesnik.
from model import Knjiznica, Knjiga, povprecje

# Dodamo nekaj knjig, da nebo knjižnica na začetku dolgočasna.

Harry_Potter_in_kamen_modrosti = Knjiga('Harry Potter in kamen modrosti', 'J. K. Rowling', '1997', 'Prva knjiga v zbriki o mladem čarovniku, ki je obnorela svet.')

# Slovar naziva bo pomemben, da s pomočjo naslova knjige dobimo naziv le-te.
slovar_naziva = {
    'Harry Potter in kamen modrosti': Harry_Potter_in_kamen_modrosti
}

# Ustvarimo našo začetno knjižnico.
knjiznica = Knjiznica()
knjiznica.dodaj_knjigo(Harry_Potter_in_kamen_modrosti)

# Tukaj so vse funkcije, ki jih bomo potrebovali
def pozdrav():
    print('POZDRAVLJENI v vaši knjižnici knjig. Tukaj lahko dodajate že prebrane knjige, ter jih nato ocenjujete in jim napišete komentarje.')

def izberi_dejanje():
    print('Napiši številko pred dejanjem, ki ga hočeš izvesti:')
    print(' 1) izberi knjigo')
    print(' 2) dodaj novo knjigo')
    print(' 3) izbriši knjigo')
    dejanje = input('>')
    return dejanje

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
        print('  - ' + knjiga.naslov)
    izbira = input('>')
    return slovar_naziva[izbira]

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
        elif not ali_bomo_dodali_nov_komentar():
            pass
    else:
        print('Ups, te knjige ni v tvoji knjižnici. Poskusi znova')
        return izberi_knjigo()


# To je funkcija, ki bo zagnala vse ostale funkcije.
def pozeni_knjiznico():
    pozdrav()
    if izberi_dejanje() == '1':
        odpri_podatke_o_knjigi(izberi_knjigo())
    if izberi_dejanje() == '2':
        pass
    if izberi_dejanje() == '3':
        pass
    if izberi_dejanje() == '4':
        pass
    else:
        print('Napačna izbira.')

# Knjižnico še poženemo
pozeni_knjiznico()