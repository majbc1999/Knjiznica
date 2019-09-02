# Najprej uvozimo bottle in model.

import bottle
from model import Knjiznica, Knjiga, povprecje

# Tukaj bo naš program dejansko tekel.

@bottle.get("/")
def pozdravna_stran():
    return bottle.template("pozdravna_stran.tpl")

@bottle.get("/vasa_knjiznica/")
def vasa_knjiznica():
    return bottle.template("osnovna_stran.tpl")

@bottle.get("/vstopi_v_bazo/")
def vstopi_v_bazo():
    return bottle.template("seznam_knjig.tpl")

@bottle.get("/vstopi_v_bazo/<knjiga>/")
def podatki_o_knjigi(knjiga):
    from zbirka_knjig import slovar_naziva
    naslov = knjiga
    avtor = slovar_naziva[knjiga].avtor
    leto = slovar_naziva[knjiga].leto_izdaje
    opis = slovar_naziva[knjiga].opis
    ocena = slovar_naziva[knjiga].vrni_povprecno_oceno()
    komentarji = slovar_naziva[knjiga].izpisi_komentarje()
    return bottle.template("podatki_o_knjigi.tpl", naslov=naslov, avtor=avtor, leto=leto, opis=opis, ocena=ocena, komentarji=komentarji)


# Program še poženemo.

bottle.run(reloader=True, debug=True)