window.onload = function() {;

    // functie die telkens opnieuw wordt uigevoerd
    // haal data van de server af (/game) en update aantal speelstukken en wie aan de beurt is
    // als de game niet actief is en er is een winner,
    // dan verwijs door naar de win pagina en voeg winner en speeltijd toe aan de parameters
    function updateGame() {
        $.get( "https://michael2222.pythonanywhere.com/status", function( data ) {
            data = JSON.parse(data);
            gate = data["gateStatus"]
            const status = document.getElementById('status');
            if (gate == "closed") {
                status.textContent = "Status: Closed" ;
            }
            if (gate == "opened") {
                status.textContent = "Status: Opened" ;
            }
            
        });
    }
    

    // voer de update functie uit, en herhaal dit elker 100 milliseconde
    updateGame()
    setInterval(function() {
        updateGame();
    }, 100);

    $.get( "https://michael2222.pythonanywhere.com/status", function( data ) {
        data = JSON.parse(data);
        gate = data["gateStatus"]
        const btn = document.getElementById('btn');
        if (gate == "opened") {
            btn.textContent = "Close";
        } else {
            btn.textContent = "Open";
        }
    });

    var wachttijd = 0
    btn.addEventListener('click', function handleClick() {
        if (btn.textContent == "Open") {
            btn.textContent = "Opening..."  ;
            function pollDOM () {
                if (gate == "opened") {
                    btn.textContent = "Close"
                    pywebview.api.passThrough("opened") ;
                } else if (wachttijd > 40000){
                    window.alert("Er is iets foutgegaan, probeer opnieuw.")
                    btn.textContent = "Open"
                    wachttijd = 0
                } else {
                    wachttijd = wachttijd + 100
                    window.setTimeout(pollDOM, 100); // try again in 1000 milliseconds
                }
            }
            pollDOM();
        }
        else if  (btn.textContent == "Close") {
            btn.textContent = "Closing..." ;
            function pollDOM () {
                if (gate == "closed") {
                    btn.textContent = "Open"
                    pywebview.api.passThrough("closed");
                } else if (wachttijd > 40000){
                    window.alert("Er is iets foutgegaan, probeer opnieuw.")
                    btn.textContent = "Close"
                    wachttijd = 0
                } else {
                    wachttijd = wachttijd + 100
                    window.setTimeout(pollDOM, 100); // try again in 1000 milliseconds
                }
            }
            pollDOM();
        }
    });
    const live = document.getElementById('live');
    live.addEventListener('click', function handleClick() {
        window.alert("Open live feed");

    });



}
