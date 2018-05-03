
function comprobarEmail(campo, size) {
    var pat = /^(\w+)@(\w+)(\.(\w+)){1,2}$/i;       //Patrón que vale para email de tipo x@x.x y x@x.x.x

    if ((campo.value.length > size)) {              //Comprueba si el contenido del campo es mayor que size
        alert("Email muy grande. Por favor introduzca otro que tenga menos de" + size + " caracteres");
        campo.style.backgroundColor = "red";                               //Colorea ese campo de amarillo
        return false;

    }
    if (!(campo.value.match(pat))) {                    //Comprueba si el valor del campo coincide con el patrón
        alert("El email introducido no tiene el formato correcto");
        campo.style.backgroundColor = "red";                               //Colorea ese campo de amarillo
        return false;

    }
    campo.style.backgroundColor = "green";
    return true;
}


function comprobarArchivo(campo) {
    var val = campo.value;                                              //Valor del campo sobre el que se aplica la función
    var archpermitidos = new Array("jpg", "png", "jpeg");        //Un array con las extensiones permitidas por la aplicación
    var extension = val.split('.').pop().toLowerCase();                 //Variable en la que se almacena la extensión del archivo

    for (var i = 0; i <= archpermitidos.length; i++) {                  //Recorre las extensiones permitidas y las compara con la extensión
        if (archpermitidos[i] == extension) {
            campo.style.backgroundColor = "green";
            return true;
        }
    }
    alert("Tipo de archivo no permitido");
    campo.style.backgroundColor = "red";                               //Colorea ese campo de amarillo
    return false;
}


function comprobarTelf(campo) {
    var pat = /^[0-9]{0,2}[0-9]{9}$/;									//Patrón de un número telefónico. 0034 opcional
    if (!(campo.value.match(pat))) {									//Comprueba si el valor del campo es un teléfono
        alert("El telefono es incorrecto");
        campo.style.backgroundColor = "red";                               //Colorea ese campo de amarillo
        return false;

    }
    campo.style.backgroundColor = "green";
    return true;

}

function comprobarAlfabetico(campo, size) {
    var pat = /^[a-zñáéíóúü]+((\s[a-zñáéíóúü]+)*)$/i;    //Patrón para palabras alfabéticas en Español
    var nul = /^([Nn][Uu][Ll][Ll])$/i;                                  //Patrón para null

    if (campo.value.length > size) {                                        //Comprueba si el contenido del campo es mayor que size
        alert("El valor introducido es mayor que el máximo permitido: " + size);
        campo.style.backgroundColor = "red";                               //Colorea ese campo de amarillo
        return false;
    }

    if (!(campo.value.match(pat))) {                                        //Si no coincide con el patrón pat, return false
        alert("El campo tiene valores no permitidos");
        campo.style.backgroundColor = "red";                               //Colorea ese campo de amarillo
        return false;
    }

    if ((campo.value.trim()).match(nul)) {                              //trim elimina espacios y comprueba si el campo tiene el valor null.
        alert("NULL no es un nombre válido");                      //match devuelve null si no encuentra el patrón
        campo.style.backgroundColor = "red";                               //Colorea ese campo de amarillo
        return false;
    }
    campo.style.backgroundColor = "green";
    return true;
}

function comprobarTexto(element, size) {
    if (element.value) {
        if (element.value.length > size) {
            alert('Longitud incorrecta. El atributo ' + element.name + ' debe ser maximo ' + size + ' y es ' + element.value.length);
            campo.style.backgroundColor = "red";
            return false;
        }
    }
    campo.style.backgroundColor = "green";
    return true;
}
