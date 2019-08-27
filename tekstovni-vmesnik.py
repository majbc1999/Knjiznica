from model import Knjiznica, Knjiga, seznam_knjig, slovar_avtorjev, slovar_letnic, slovar_opisov, povprecje

knjiznica = Knjiznica()

def pozdrav():
    print('Pozdravljeni v vaši knjižnici knjig. Tukaj lahko dodajate že prebrane knjige, ter jih nato ocenjujete in jim napišete komentarje.')

def izberi_dejanje():
    print('Napiši številko pred dejanjem, ki ga hočeš izvesti')
    print('1) izberi knjigo')
    print('2) dodaj novo knjigo')
    dejanje = imput('>')
    return dejanje

def dodaj_novo_knjigo():
    naslov = imput('naslov >')
    avtor = imput('avtor >')
    leto_izdaje = imput('leto izdaje >')
    opis = imput('opis >')
    knjiga = Knjiga(naslov, avtor, leto_izdaje, opis)
    Knjiznica.dodaj_knjigo(knjiga)
    print('Uspešno ste dodali knjigo!')

def izberi_knjigo():
    print('Za ogled opisa knjige, avtorja ter leta izdaje napiši NATANČEN naslov knjige.')
    for knjiga in seznam_knjig:
        print(knjiga + ' ' + '(' + knjiga.izpisi_oceno() + '/ 5')
    izbira = imput('>')
    return izbira

def odpri_podatke_o_knjigi(knjiga):
    if knjiga in seznam_knjig:
        print('NASLOV:'+ str(knjiga) + ' ' + '(' + knjiga.izpisi_oceno() + '/ 5')
        print('AVTOR:' slovar_avtorjev[knjiga])
        print('LETO IZDAJE:' slovar_letnic[knjiga])
        print('OPIS:' slovar_opisov[knjiga])
        print('.................................')
        print('komentarji')
        for x in knjiga.izpisi_komentarje():
            print('- ' + str(x))
    else:
        print('Ups, te knjige ni v tvoji knjižnici. Poskusi znova')
        return izberi_knjigo






