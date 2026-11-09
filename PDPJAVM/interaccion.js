function = registrar () {

    const user = document.getElementById("userReg").value;
    const pass = document.getElementById("passReg").valuer;


    if (user === "" || pass ==="") {
    document.getElementsById("msgRed").textContent="Completa todos los campos.";
    return;
    }

    const userData ={
    usuario: user,
    contraseña: pass
    };
      localStorage.setItem ("usuarioRegistrado".JSON.stringify(userData));

       document.getElementById("msgReg").textContent = "Usuario registrado exitosamente.";

}