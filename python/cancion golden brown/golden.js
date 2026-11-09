const cancion = [
    { texto: "Golden Brown", espera: 720 },
    { texto: "Texture Like Sun", espera: 2900 },
    { texto: "Lays Me Down", espera: 680 },
    { texto: "With My Mind She Runs", espera: 3100 },
    { texto: "Trougouth the Nigth", espera: 1000 },
    { texto: "No Need To Fight", espera: 2000 },
    { texto: "Never a From", espera: 1700 },
    { texto: "With", espera: 300 },
    { texto: "Golden Brown", espera: 6000 },
    { texto: "Every time Just Like the Last", espera: 3700 },
    { texto: "On Her ship Tied to the Mast", espera: 4000 },
    { texto: "To Distand Lands", espera: 2000 },
    { texto: "Takes Both my Hands", espera: 1080 },
    { texto: "Never a From With", espera: 2190 },
    { texto: "Golden Brown", espera: 23000 },
    { texto: "Golden Brown, Finer Temptress", espera: 4000 },
    { texto: "Trough the Ages She's Hading West", espera: 4000 },
    { texto: "From Far Away", espera: 1800 },
    { texto: "Stays For A Day", espera: 2700 },
    { texto: "Never A From With Golden Brown", espera: 82000 },
    { texto: "NEVER A FROWM", espera: 4000 },
    { texto: "WITH GOLDEN BROWN", espera: 4000 },
    { texto: "NEVER A FROWM", espera: 4000 },
    { texto: "WITH GOLDEN BROWN", espera: 4000 },
    { texto: "NEVER A FROWM", espera: 4000 },
    { texto: "WITH GOLDEN BROWN", espera: 4000 },
    { texto: "NEVER A FROWM", espera: 4000 },
    { texto: "WITH GOLDEN BROWN", espera: 4000 },
    { texto: "NEVER A FROWM", espera: 4000 },
    { texto: "WITH GOLDEN BROWN", espera: 4000 },
    { texto: "NEVER A FROWM", espera: 4000 },
    { texto: "WITH GOLDEN BROWN", espera: 4000 }
];

const letraDiv = document.getElementById("letra");
const watermarkImg = document.querySelector("#watermark img");
const audio = document.getElementById("audio");

const tiempoIntro = 21700; 

let i = 0;

function mostrarLetra() {
    if (i < cancion.length) {

        letraDiv.classList.remove("show");
        letraDiv.textContent = cancion[i].texto;

        // fuerza reflow para reiniciar animación
        void letraDiv.offsetWidth;

        letraDiv.classList.add("show");

        setTimeout(mostrarLetra, cancion[i].espera);
        i++;
    }
}


const duracionTotal = cancion.reduce((total, parte) => {
    return total + parte.espera;
}, 0);

const tiempoCambio = 170870;

const watermarkOscura = "lunamedieval.png";

window.addEventListener("click", () => {

    audio.play();

    watermarkImg.style.animation = "spin 20s linear infinite";

    setTimeout(() => {
        mostrarLetra();
    }, tiempoIntro);

    setTimeout(() => {
        document.body.classList.add("dark-mode");
        watermarkImg.src = watermarkOscura;
        watermarkImg.style.animation = "spin 16s linear infinite";
    }, tiempoCambio);

}, { once: true });
