
function main() {
    console.log("Hello world! I am loaded!");
    $("a.songlink").click(function (ev) {
        console.log(ev.target.href);
        $("div.lyrics").text("Loading ... ");
        url = ev.target.href.replace("/song/","/lyrics/");
        console.log(url);
        $.ajax({url : url,
                success: function(data, textStatus, jqXHR) {
                    $("div.lyrics").html(data);
                }
            });
        ev.preventDefault();
        });
}

$(main);

