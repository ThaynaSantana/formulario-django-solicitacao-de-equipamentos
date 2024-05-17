document.getElementById('cliente_outros').addEventListener('change', function() {
    document.getElementById('outro_cliente').classList.remove('d-none');
});

document.querySelectorAll('input[name="cliente"]').forEach(function(element) {
    if (element.id !== 'cliente_outros') {
        element.addEventListener('change', function() {
            document.getElementById('outro_cliente').classList.add('d-none');
        });
    }
});
