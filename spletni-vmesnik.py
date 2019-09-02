# Najprej uvozimo bottle in model.

import bottle
from model import Knjiznica, Knjiga, povprecje

# Dodamo nekaj knjig v knjižnico, da ne bo prazna.

Harry_Potter_in_kamen_modrosti = Knjiga('Harry Potter in kamen modrosti', 'J. K. Rowling', '1997', 'Prva knjiga v zbriki o mladem čarovniku, ki je obnorela svet.')
Zlocin_in_kazen = Knjiga('Zločin in kazen', 'F. M. Dostojevski', '1866', 'Psihološki roman, ki obravnava predvsem subjektivna razmišljanja o življenju, zlasti pa o upravičenosti zločina.')
Hobit = Knjiga('Hobit ali Tja in spet nazaj', 'J.R.R. Tolkien', '1937', 'Fantazijski roman kot predhodnik Gospodarja prstanov.')
Umor_na_orient_ekspresu = Knjiga('Umor na Orient ekspresu', 'A. Christie', '1934', 'Eno najboljših del kraljice kriminalk, nova dogodivščina Hercula Poirota.')
Grimmove_pravljice = Knjiga('Grimmove pravljice', 'J. in W. Grimm', '1812', 'Zbirka najzabavnejših pravljic, ki vas potopi v svet domišljije.')
Ostrzek = Knjiga('Ostržek','C.Collodi', '1881', 'Klasika o dogodivščinah lesenega fantka.')
Da_Vincijeva_koda = Knjiga('Da Vincijeva koda', 'D. Brown', '2003', 'Misteriozna zgodovinsko obarvana pustolovska drama, ki ne razočara.')

# Ustvarimo slovar naziva.

slovar_naziva = {
    'Harry Potter in kamen modrosti': Harry_Potter_in_kamen_modrosti,
    'Hobit ali Tja in spet nazaj': Hobit,
    'Zločin in kazen': Zlocin_in_kazen,
    'Umor na Orient ekspresu': Umor_na_orient_ekspresu,
    'Grimmove pravljice': Grimmove_pravljice,
    'Ostržek': Ostrzek,
    'Da Vincijeva koda': Da_Vincijeva_koda
}


# Ustvarimo začetno knjižnico.

knjiznica = Knjiznica()
knjiznica.dodaj_knjigo(Harry_Potter_in_kamen_modrosti)
knjiznica.dodaj_knjigo(Hobit)
knjiznica.dodaj_knjigo(Zlocin_in_kazen)
knjiznica.dodaj_knjigo(Umor_na_orient_ekspresu)
knjiznica.dodaj_knjigo(Grimmove_pravljice)
knjiznica.dodaj_knjigo(Ostrzek)
knjiznica.dodaj_knjigo(Da_Vincijeva_koda)

# Tukaj bo naš program dejansko tekel.

@bottle.get("/")
def pozdravna_stran():
    return bottle.template("pozdravna_stran.tpl")

@bottle.get("/vasa_knjiznica/")
def vasa_knjiznica():
    return bottle.template("osnovna_stran.tpl")



# Program še poženemo.

bottle.run(reloader=True, debug=True)