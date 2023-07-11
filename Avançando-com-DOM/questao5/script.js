document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('submit');
    button.addEventListener('click', function(event) {
      if (!verificarCheckboxes()) {
        event.preventDefault(); // Impede o envio do formulário
      }
    });
  });
  
  function verificarCheckboxes() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    for (var i = 0; i < checkboxes.length; i++) {
      if (checkboxes[i].checked) {
        alert("Informações gravadas com sucesso!");
        return true;
      }
    }
    alert("É necessário marcar ao menos uma opção.");
    return false;
  }
  