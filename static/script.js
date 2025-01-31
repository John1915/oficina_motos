// Adiciona uma mensagem de sucesso ao cadastrar uma moto
document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('success')) {
        alert('Moto cadastrada com sucesso!');
    }
});