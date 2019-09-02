%rebase("base.tpl", title="oceni knjigo")
%from model import Knjiznica, Knjiga, povprecje

<h1>SEZNAM VAŠIH KNJIG</h1>

<h4>Kliknite na oceno zraven knjige, ali v okno pod njo vpišite željen komentar, ter pritisnite "enter".</h4>

<ol>
    %   for knjiga in slovar:
            <li>
                {{knjiga}} ({{slovar[knjiga].vrni_povprecno_oceno()}}/5.0) <br>
                <i>oceni:</i>
                <form action="/oceni_knjigo/oceni/{{knjiga}}/1/" method="post">
                    <button type="submit">1</button>
                </form>
                <form action="/oceni_knjigo/oceni/{{knjiga}}/2/" method="post">
                    <button type="submit">2</button>
                </form>
                <form action="/oceni_knjigo/oceni/{{knjiga}}/3/" method="post">
                    <button type="submit">3</button>
                </form>
                <form action="/oceni_knjigo/oceni/{{knjiga}}/4/" method="post">
                    <button type="submit">4</button> 
                </form>              
                <form action="/oceni_knjigo/oceni/{{knjiga}}/5/" method="post">
                    <button type="submit">5</button>
                </form>
                <i>komentiraj:</i>
                <form action="/oceni_knjigo/dodaj_komentar/{{knjiga}}/" method="post">
                    <input name="komentar" type="text">
                </form>
                ...
            </li>
    %   end
</ol>