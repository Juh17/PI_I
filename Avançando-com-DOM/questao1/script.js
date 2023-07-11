document.addEventListener('DOMContentLoaded', function () {
    var botaoExibir = document.getElementById('botaoExibir');
    botaoExibir.addEventListener('click', exibirConteudo);
});

function exibirConteudo() {
    let texto = document.getElementById('caixaDeTexto').value;
    if(texto === '') {
        alert("Campo Vazio! Insira um texto para exibir.")
    }
    
    document.getElementById('texto').innerHTML = conteudo;
    
}