function login() {
    let Usuario = document.getElementById("Usuario").value;
    let clave = document.getElementById("Clave").value;

    let UserCorrecto="JOSE"
    let PassCorrecto="gigiyfifi"

    if (Usuario === UserCorrecto && Password === PassCorrecto) {
        document.getElementById("mensaje").style.color = "lightgreen";
        document.getElementById("mensaje").innerHTML.text = "Ingreso exitoso✔️ "

        setTimeout(() => {
            window.location.href="index.html";

        },180.000);
    } else {
        document.getElementById("mensaje").style.color = "red";
        document.getElementById("mensaje").innerHTML.text = "Datos de inicio incorrectos :'("

    }
}