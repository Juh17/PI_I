const visualizar = document.getElementById('visualizar')
const carregar = document.getElementById('imagemCarregada')

visualizar.addEventListener('click', function() {
    const nome = document.getElementById('imagem').value;
    const img = document.createElement("img");
    img.src = "Imagens/" + nome
    img.style.width = '300px'
    carregar.appendChild(img);
})