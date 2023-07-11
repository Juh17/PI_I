document.addEventListener('DOMContentLoaded', function () {
    var botaoExibir = document.getElementById('botao');
    botaoExibir.addEventListener('click', converterTexto);
});

function converterTexto() {
    let num1 = document.getElementById('caixa1').value;
    let num2 = document.getElementById('caixa2').value;
    let Resultado = document.getElementById("resultado");

    if (isNaN(num1) || isNaN(num2)) {
        Resultado.classList.add("exibir");
        alert("Erro: Os campos devem ser preenchidos com um número!");
        Resultado.innerHTML = 'Operação inválida';
    } else {
        if (num1 && num2) {
            let resultado = num1 * num2;
            Resultado.innerHTML = `${num1} * ${num2} = ${resultado}`;
            Resultado.classList.add("exibir");
        } else {
            Resultado.classList.remove("exibir");
            alert("Erro: Preencha os campos para prosseguir.");
            document.getElementById('texto').innerHTML = '<span style="color:red;">Erro: Preencha os campos para prosseguir!</span>';
        }
    }

}
