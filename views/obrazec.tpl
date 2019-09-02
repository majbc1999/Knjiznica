%rebase("base.tpl", title="obrazec")

<form action="/vasa_knjiznica/" method="get">
    <button type="submit"><</button>
</form>

<h1> DODAJANJE NOVE KNJIGE </h1>

<h4> V spodnji obrazec vpiši podatke o novi knjigi in pritisni gumb "dodaj novo knjigo v knjižnico!" </h4>

<form action="/dodaj_novo_knjigo/" method="post">
    naslov: <input name="naslov" type="text"><br>
    .<br>
    avtor: <input name="avtor" type="text"><br>
    .<br>
    leto izdaje: <input name="leto" type="text"><br>
    .<br>
    opis knjige: <input name="opis" type="text"><br>
    .<br>
    <button type="submit">dodaj novo knjigo v knjižnico!</button>
</form>