body {
    font-family: Arial, sans-serif;
    background-color: #0f172a;
    color: white;
    text-align: center;
    margin: 0;
    padding: 50px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: #1e293b;
    padding: 20px;
    border-radius: 10px;
}

.painel {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 20px;
}

.par {
    background: #111827;
    padding: 15px;
    border-radius: 10px;
    font-size: 18px;
    transition: 0.3s;
}

.call {
    color: #16a34a;
    font-weight: bold;
}

.put {
    color: #dc2626;
    font-weight: bold;
}

button {
    padding: 15px 30px;
    font-size: 18px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    background-color: #2563eb;
    color: white;
    margin-bottom: 20px;
}

.historico {
    background: #111827;
    padding: 10px;
    border-radius: 10px;
    max-height: 200px;
    overflow-y: auto;
    text-align: left;
}
