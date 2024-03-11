function IMC() {
    t = document.getElementById("t").value
    m = document.getElementById("m").value
    x = 10000 * m / (t * t)
    document.getElementById("calc").innerHTML = "Votre imc est <i>" + x +"</i>."
    return x
}

function etat() {
    x = IMC()
    if (x < 18.5) {
    document.getElementById("state").innerHTML = "Vous êtes en insuffisance pondérale"
    }
    else if (x < 25)
    {}
   }

