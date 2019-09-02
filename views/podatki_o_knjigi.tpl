%rebase("base.tpl", title="podatki o knjigi")
<ul>
    <li>naslov:       <b>{{naslov}}</b></li>
    <li>avtor:        <i>{{avtor}}</i></li>
    <li>leto izdaje:  <i>{{leto}}</i></li>
    <li>opis:         <i>{{opis}}</i></li>
    <li>..............</li>
    <li>
        vaša ocena:   <i>{{ocena}}/5</i>
    </li>
    <li>
        vaši komentarji:
            <i>
                %if len(komentarji) == 0:
                    trenutno nimate dodanih komentarjev.
                %else:
                    <ol>
                        %for komentar in komentarji:
                            <li>
                                {{komentar}}
                            </li>
                        %end
                    </ol>
            </i>
    </li>
</ul>
