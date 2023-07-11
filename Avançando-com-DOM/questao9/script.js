const campo = document.getElementById("texto")
const select = document.getElementById("select")
const inserir = document.getElementById("inserir")

inserir.addEventListener('click', () => {
    const texto = campo.value

    if(select.options.length >= 5) {
        alert("O máximo de palavras permitidas é 5")
        return
    }
    
    for(let i = 0; i < select.options.length; i++) {
        if(select.options[i].value == texto) {
            alert('Não é possível repetir. Insira um outro texto!')
            return
        }
    }
    if( texto == '') {
        alert('Campo vazio! Insira um texto para prosseguir.')
        return
    }

    const option = document.createElement('option')
    option.text = texto

    select.appendChild(option)
})

remover.addEventListener('click', () => {
    if(select.options.length > 0) {
        select.removeChild(select.options[0])
    }
})
