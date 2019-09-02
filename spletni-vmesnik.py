# Najprej uvozimo bottle in model.

import bottle
from model import Knjiznica, Knjiga, povprecje, ustvari_novo_knjiznico, ustvari_slovar_naziva, ustvari_ime_za_v_slovar_naziva

nasa_knjiznica = ustvari_novo_knjiznico()
slovar_naziva = ustvari_slovar_naziva(nasa_knjiznica)

# Tukaj bo naš program dejansko tekel.

@bottle.get("/")
def pozdravna_stran():
    return bottle.template("pozdravna_stran.tpl")

@bottle.get("/vasa_knjiznica/")
def vasa_knjiznica():
    return bottle.template("osnovna_stran.tpl")

@bottle.get("/vstopi_v_bazo/")
def vstopi_v_bazo():
    knjiznica = nasa_knjiznica
    slovar = slovar_naziva
    return bottle.template("seznam_knjig.tpl", knjiznica=knjiznica, slovar=slovar)

@bottle.get("/vstopi_v_bazo/<knjiga>/")
def podatki_o_knjigi(knjiga):
    naslov = knjiga
    avtor = slovar_naziva[knjiga].avtor
    leto = slovar_naziva[knjiga].leto_izdaje
    opis = slovar_naziva[knjiga].opis
    ocena = slovar_naziva[knjiga].vrni_povprecno_oceno()
    komentarji = slovar_naziva[knjiga].izpisi_komentarje()
    return bottle.template("podatki_o_knjigi.tpl", naslov=naslov, avtor=avtor, leto=leto, opis=opis, ocena=ocena, komentarji=komentarji)

@bottle.get("/oceni_knjigo/")
def dodaj_oceno_ali_komentar():
    knjiznica = nasa_knjiznica
    slovar = slovar_naziva
    return bottle.template("oceni.tpl", knjiznica=knjiznica, slovar=slovar)

@bottle.post("/oceni_knjigo/oceni/<knjiga>/<ocena>/")
def dodaj_oceno(knjiga, ocena):
    if ocena == '1':
        slovar_naziva[knjiga].dodaj_oceno(1)
    elif ocena == '2':
        slovar_naziva[knjiga].dodaj_oceno(2)
    elif ocena == '3':
        slovar_naziva[knjiga].dodaj_oceno(3)
    elif ocena == '4':
        slovar_naziva[knjiga].dodaj_oceno(4)
    elif ocena == '5':
        slovar_naziva[knjiga].dodaj_oceno(5)
    bottle.redirect("/vasa_knjiznica/")

@bottle.post("/oceni_knjigo/dodaj_komentar/<knjiga>/")
def dodaj_komentar(knjiga):
    komentar = bottle.request.forms.getunicode("komentar")
    slovar_naziva[knjiga].dodaj_komentar(komentar)
    bottle.redirect("/vasa_knjiznica/")

@bottle.post("/obrazec_za_knjigo/")
def obrazec():
    return bottle.template("obrazec.tpl")

@bottle.post("/dodaj_novo_knjigo/")
def dodaj_novo_knjigo():
    naslov = bottle.request.forms.getunicode("naslov")
    naziv_knjige = ustvari_ime_za_v_slovar_naziva(naslov)
    avtor = bottle.request.forms.getunicode("avtor")
    leto = bottle.request.forms.getunicode("leto")
    opis = bottle.request.forms.getunicode("opis")
    naziv_knjige = Knjiga(naslov, avtor, leto, opis)
    nasa_knjiznica.dodaj_knjigo(naziv_knjige)
    slovar_naziva[naslov] = naziv_knjige
    bottle.redirect("/vasa_knjiznica/")

@bottle.post("/izbrisi_knjigo/")
def izbira_za_izbris():
    knjiznica = nasa_knjiznica
    slovar = slovar_naziva
    return bottle.template("brisanje.tpl", knjiznica=knjiznica, slovar=slovar)

@bottle.post("/dokoncno_izbrisi/<knjiga>/")
def dokoncno_izbrisi(knjiga):
    nasa_knjiznica.izbrisi_knjigo(slovar_naziva[knjiga])
    del slovar_naziva[knjiga]
    bottle.redirect("/vasa_knjiznica/")

# Program še poženemo.

bottle.run(reloader=True, debug=True)