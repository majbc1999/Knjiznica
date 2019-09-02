%rebase("base.tpl", title="vaša knjiznica")

<h1>KNJIŽNICA</h1>

<h4>Kaj želite storiti?</h4>
<p>
    <ul>
        <li>
            Vstopi v svojo bazo knjig in raziskuj.
            <form action="/vstopi_v_bazo/" method="get">
                <button type="submit">></button>
            </form>
        </li>

        <li>
            Oceni svojo knjigo ali komentiraj.
            <form action="/oceni_knjigo/" method="get">
                <button type="submit">></button>
            </form>
        </li>

        <li>
            Dodaj novo knjigo.
            <form action="/obrazec_za_knjigo/" method="post">
                <button type="submit">></button>
            </form>
        </li>

        <li>
            Izbriši svojo obstoječo knjigo.
            <form action="/izbrisi_knjigo/" method="post">
                <button type="submit">></button>
            </form>
        </li>
    </ul>
</p>