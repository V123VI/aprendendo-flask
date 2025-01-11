///ajuda do gptptptptpttpfpt

function atualizarHora() {
    var horaAtual = new Date();
    var horas = horaAtual.getHours().toString().padStart(2, '0');
    var minutos = horaAtual.getMinutes().toString().padStart(2, '0');
    var segundos = horaAtual.getSeconds().toString().padStart(2, '0');
    var horaFormatada = horas + ":" + minutos + ":" + segundos;

    // Atualiza o conteúdo do elemento com id "hora"
    document.getElementById("hora").textContent = horaFormatada;
}

// Atualiza a hora a cada segundo
setInterval(atualizarHora, 1000);

// Chama a função uma vez para exibir a hora imediatamente
atualizarHora();


