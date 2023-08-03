// als de pagina is geladen, haal np1, np2, cp1 en cp2 uit de url
// zet de namen in de juiste elementen en voeg de juiste class toe aan de hand van de kleur
window.onload = function() {;

    // haal de huidige tijd op en start een timer interval die elke seconde de timer waarde update
    // var gameTime
    // var startTime = Date.now()
    // var delta = Date.now() - startTime; 
    // var seconds = Math.floor(delta / 1000)
    // gameTime = new Date(seconds * 1000).toISOString().substring(14, 19)
    // setInterval(function timerFunction() {
    //     var delta = Date.now() - startTime; 
    //     var seconds = Math.floor(delta / 1000)
    //     gameTime = new Date(seconds * 1000).toISOString().substring(14, 19)
    //     $(".timer").text(gameTime)
    // }, 1000);
 
    // als er 1x op stop wordt geklikt, vraag voor en confirmatie
    // als er nog eens wordt gedrukt, voer de stop functie van de api uit een ga terug naar het begin scherm
    // anders zet de stop knop weer terug op normaal

    
    // if (status.textContent == "Status: Closed") status.textContent = "Status: Opened" ;
    //     else status.textContent = "Status: Closed"

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

    const btn = document.getElementById('btn');
    var wachttijd = 0
    btn.addEventListener('click', function handleClick() {
        if (btn.textContent == "Open") {
            btn.textContent = "Opening..."  ;
            // pywebview.api.passThrough("opened") ;
            function pollDOM () {
                if (gate == "opened") {
                    btn.textContent = "Close"
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
            // pywebview.api.passThrough("closed");
            function pollDOM () {
                if (gate == "closed") {
                    btn.textContent = "Open"
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
}

