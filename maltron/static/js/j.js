
    document.querySelector('form').addEventListener('submit', function(event) {
        let nombre = document.querySelector('[name="nombre"]').value;
        let email = document.querySelector('[name="email"]').value;
        let mensaje = document.querySelector('[name="mensaje"]').value;

        if (!nombre || !email || !mensaje) {
            event.preventDefault();
            alert('Todos los campos son obligatorios.');
        }
    });

