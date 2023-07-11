const campo = document.getElementById("texto")
const select = document.getElementById("select")
const inserir = document.getElementById("inserir")

inserir.addEventListener('click', () => {
    const texto = campo.value

    const option = document.createElement('option')
    option.text = texto
    select.appendChild(option)
})