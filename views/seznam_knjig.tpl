%rebase("base.tpl", title="vaša knjiznica")
%from model import Knjiznica, Knjiga, povprecje
%from zbirka_knjig import slovar_naziva, knjiznica

<h1>SEZNAM VAŠIH KNJIG<h2>

<h4>Kliknite na gumb zraven knjige, ki si jo želite ogledati!</h4>

<ol>
    %   for knjiga in slovar_naziva :
            <li>
                {{knjiga}}
                <form action="/{{knjiga}}/" method="get">
                    <button type="submit">></button>
                </form>
            </li>
    %   end
</ol>

