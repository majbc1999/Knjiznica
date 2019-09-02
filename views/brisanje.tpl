%rebase("base.tpl", title="brisanje")

<h1> IZBRIŠI KNJIGO IZ KNJIŽNICE </h1>

<h4>Kliknite na gumb zraven knjige, ki jo želite izbrisati!</h4>

<ol>
    %   for knjiga in slovar:
            <li>
                {{knjiga}} ({{slovar[knjiga].vrni_povprecno_oceno()}}/5.0)
                <form action="/dokoncno_izbrisi/{{knjiga}}/" method="post">
                    <button type="submit">></button>
                </form>
            </li>
    %   end
</ol>