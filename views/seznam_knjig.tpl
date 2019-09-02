%rebase("base.tpl", title="seznam knjig")
%from model import Knjiznica, Knjiga, povprecje


<h1>SEZNAM VAŠIH KNJIG</h1>

<h4>Kliknite na gumb zraven knjige, ki si jo želite ogledati!</h4>

<ol>
    %   for knjiga in slovar:
            <li>
                {{knjiga}} ({{slovar[knjiga].vrni_povprecno_oceno()}}/5.0)
                <form action="/vstopi_v_bazo/{{knjiga}}/" method="get">
                    <button type="submit">></button>
                </form>
            </li>
    %   end
</ol>

