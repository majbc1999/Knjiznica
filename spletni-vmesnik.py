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

@bottle.get("/vstopi_v_bazo/<naslov>/")
def podatki_o_knjigi(naslov):
    return bottle.get("/podatki.tpl/", naslov = naslov)


# Program še poženemo.

bottle.run(reloader=True, debug=True)