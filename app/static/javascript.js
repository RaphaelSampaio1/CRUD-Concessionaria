(function(win, doc){
    'use strict';

    // Verifica se o usuário quer deletar
    if (doc.querySelector('.btnDel')) {
        let btnDel = doc.querySelectorAll('.btnDel');
        for (let i = 0; i < btnDel.length; i++) {
            btnDel[i].addEventListener('click', function(event) {
                if (confirm('Tem certeza que deseja excluir?')) {
                    return true;
                } else {
                    event.preventDefault();
                }
            });
        }
    }

    // AJAX DO FORM
    if (doc.querySelector('#form')) {
        let form = doc.querySelector('#form');

        function sendForm(event) {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelector('input[name="csrfmiddlewaretoken"]').value; // Ajuste o seletor se necessário

            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN', token);
            ajax.onreadystatechange = function() {
                if (ajax.readyState === 4) {
                    if (ajax.status === 200) {
                        let result = doc.querySelector('#result');
                        result.innerHTML = 'Operação realizada com sucesso!';
                        result.classList.add('alert');
                        result.classList.add('alert-success');
                    } else {
                        // Em caso de erro, exiba uma mensagem apropriada
                        let result = doc.querySelector('#result');
                        result.innerHTML = 'Ocorreu um erro ao realizar a operação.';
                        result.classList.add('alert');
                        result.classList.add('alert-danger');
                    }
                }
            };
            ajax.send(data);
            form.reset();
        }

        form.addEventListener('submit', sendForm, false);
    }
})(window, document);