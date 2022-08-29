function build_lyrics(lyrics) {
    ret = $(`<p>
    <h4> Lyrics for ${lyrics.name} </h4>
    <h5> <small class="text-muted">${lyrics.artist.name}</small> </h5>
</p>
<p>
    ${lyrics.lyrics}
</p>`)

    return ret;
}

function main() {
    console.log("Hello world! I am loaded!");
    $("a.songlink").click(function (ev) {
        console.log(ev.target.href);
        $("div.lyrics").text("Loading ... ");
        $.ajax({url : ev.target.href,
                dataType: 'json',
                success: function(data, textStatus, jqXHR) {
                    $("div.lyrics").html(build_lyrics(data.song));
                    // var text = ev.target.innerText;
                    // console.log("The a text is ", text);
                    // var parent = ev.target.parentNode;
                    // ev.target.remove();
                    // $(parent).html(text);
                }
            });
        ev.preventDefault();
        });
}

$(main);

