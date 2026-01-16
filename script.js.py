const pares = ["EUR/USD", "GBP/USD", "USD/JPY"];
const direcoes = ["CALL", "PUT"];
const historico = [];

function gerarSinal() {
    // Gerar 3 sinais aleatórios
    for (let i = 1; i <= 3; i++) {
        const par = pares[Math.floor(Math.random() * pares.length)];
        const direcao = direcoes[Math.floor(Math.random() * direcoes.length)];
        const valor = (Math.random() * (1 - 0.1) + 0.1).toFixed(2);
        const hora = new Date().toLocaleTimeString("pt-PT", {hour:'2-digit', minute:'2-digit'});

        // Atualizar painel
        const elemento = document.getElementById(`par${i}`);
        elemento.innerHTML = `
            🔹 Par: ${par} <br>
            🔹 Entrada: <span class="${direcao.toLowerCase()}">${direcao}</span> <br>
            🔹 Tempo: 1 minuto <br>
            🔹 Valor sugerido: $${valor} <br>
            🕒 Hora: ${hora}
        `;

        // Salvar no histórico
        historico.unshift(`${hora} - ${par} - ${direcao} - $${valor}`);
    }

    atualizarHistorico();
}

function atualizarHistorico() {
    const histDiv = document.getElementById("historico");
    histDiv.innerHTML = historico.slice(0, 10).map(item => `• ${item}`).join("<br>");
}

// Atualização automática a cada 10 segundos
setInterval(gerarSinal, 10000);

// Gerar sinais iniciais
gerarSinal();
