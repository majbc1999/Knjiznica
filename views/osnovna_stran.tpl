%rebase("base.tpl", title="vaša knjiznica")

<h1>KNJIŽNICA</h1>

<h4>Kaj želite storiti?</h4>
<p>
    <ul>
        <li>
            <form action="/vstopi_v_bazo/" method="get">
                <button type="submit">Vstopi v svojo bazo knjig in raziskuj.</button>
            </form>
        </li>

        <li>
            <form action="/oceni_knjigo/" method="post">
                <button type="submit">Oceni svojo knjigo.</button>
            </form>
        </li>

        <li>
            <form action="/dodaj_novo_knjigo/" method="post">
                <button type="submit">Dodaj novo knjigo.</button>
            </form>
        </li>

        <li>
            <form action="/izbrisi_knjigo/" method="post">
                <button type="submit">Izbriši svojo obstoječo knjigo.</button>
            </form>
        </li>
    </ul>
</p>