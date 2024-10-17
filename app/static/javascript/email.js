// Inicializa o EmailJS com sua chave pública
(function() {
  emailjs.init('ghsQxeOnMzQjby9yi'); // Substitua pelo seu User ID
})();

// Substituindo window.onload por DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Envia o formulário usando o EmailJS
    emailjs.sendForm('service_cwl8b0b', 'template_gqinv13', this) // Substitua pelos seus IDs
    .then(() => {
      console.log('Email enviado com sucesso!');
      alert('Mensagem enviada com sucesso!');
      // Limpa o formulário após o envio
      document.getElementById('contact-form').reset();
    }, (error) => {
      console.log('Falha ao enviar: ', error);
      alert('Falha ao enviar a mensagem.');
    });
  });
});
