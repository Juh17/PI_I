document.addEventListener('DOMContentLoaded', function () {
  var exibir = document.getElementById('exibirImagem');
  exibir.addEventListener('click', addOption);
});

function addOption() {
  let Selecionar = document.getElementById('selecionar').value;
  let Imagem = document.getElementById('imagem');

  if (Selecionar !== 'default') {
    let img = document.createElement('img');
    img.src = Selecionar;
    img.style.width = '300px'
    Imagem.innerHTML = '';
    Imagem.appendChild(img);
  } else {
    alert('Erro: Selecione uma opção!');
    document.getElementById('imagem').innerHTML =
      '<span style="color:red;">Erro: Selecione uma opção!</span>';
  }
}