<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Orion Indicador - Sinais</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>📊 Orion Indicador</h1>

        <div class="painel">
            <!-- Pares -->
            <div class="par" id="par1"></div>
            <div class="par" id="par2"></div>
            <div class="par" id="par3"></div>
        </div>

        <button onclick="gerarSinal()">🔄 Gerar Sinal</button>

        <h2>🕒 Histórico dos sinais</h2>
        <div id="historico" class="historico"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
