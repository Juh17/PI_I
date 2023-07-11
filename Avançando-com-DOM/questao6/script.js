document.addEventListener('DOMContentLoaded', function () {
    var exibir = document.getElementById('converter');
    exibir.addEventListener('click', converter);
});

function converter() {
    let campoTexto = document.getElementById('campoTexto').value;
    let opcoes = document.getElementById('opcoes').value;

    if(opcoes == "maiuscula"){
        document.getElementById('cont').innerHTML = campoTexto.toUpperCase();
    }else{
        document.getElementById('cont').innerHTML = campoTexto.toLowerCase();
    }
}f