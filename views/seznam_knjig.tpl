%rebase("base.tpl", title="vaša knjiznica")
%from model import Knjiznica, Knjiga, povprecje
%from zbirka_knjig import slovar_naziva, knjiznica

<h1>SEZNAM VAŠIH KNJIG<h2>

<h4>Kliknite na gumb zraven knjige, ki si jo želite ogledati!</h4>

<ol>
    %   for knjiga in slovar_naziva :
            <li>
                {{knjiga}} ({{slovar_naziva[knjiga].vrni_povprecno_oceno()}}/5)
                <form action="/vstopi_v_bazo/{{knjiga}}/" method="get">
                    <button type="submit">></button>
                </form>
            </li>
    %   end
</ol>

