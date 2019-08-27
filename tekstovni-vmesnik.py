from model import Knjiznica, Knjiga, seznam_knjig, povprecje

knjiznica = Knjiznica()

def pozdrav():
    print('Pozdravljeni v vaši knjižnici knjig. Tukaj lahko dodajate že prebrane knjige, ter jih nato ocenjujete in jim napišete komentarje.')

def izberi_dejanje():
    print('Napiši številko pred dejanjem, ki ga hočeš izvesti')
    print('1) izberi knjigo')
    print('2) dodaj novo knjigo')
    print('3) izbriši knjigo')
    dejanje = input('>')
    return dejanje

def dodaj_novo_knjigo():
    naslov = input('naslov >')
    avtor = input('avtor >')
    leto_izdaje = input('leto izdaje >')
    opis = input('opis >')
    knjiga = Knjiga(naslov, avtor, leto_izdaje, opis)
    knjiznica.dodaj_knjigo(knjiga)
    print('Uspešno ste dodali knjigo!')

def izberi_knjigo():
    print('Za ogled opisa knjige, avtorja ter leta izdaje napiši NATANČEN naslov knjige.')
    for knjiga in seznam_knjig:
        print(knjiga.naslov() + ' ' + '(' + knjiga.izpisi_oceno() + '/ 5')
    izbira = input('>')
    return izbira

def odpri_podatke_o_knjigi(knjiga):
    if knjiga in seznam_knjig:
        print('NASLOV:'+ knjiga.naslov() + ' ' + '(' + knjiga.izpisi_oceno() + '/ 5')
        print('AVTOR:' + knjiga.avtor())
        print('LETO IZDAJE:' + knjiga.leto_izdaje())
        print('OPIS:' + knjiga.opis())
        print('.................................')
        print('komentarji')
        for x in knjiga.izpisi_komentarje():
            print('- ' + str(x))
    else:
        print('Ups, te knjige ni v tvoji knjižnici. Poskusi znova')
        return izberi_knjigo()

def pozeni_knjiznico():
    pozdrav()
    if izberi_dejanje() == '1':
        izberi_knjigo()
        odpri_podatke_o_knjigi(izberi_knjigo())
    if izberi_dejanje() == '2':
        pass
    if izberi_dejanje() == '3':
        pass
    else:
        print('Napačna izbira.')


pozeni_knjiznico()
