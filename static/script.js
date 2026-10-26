function enviarAPI(rota) {
    fetch(`/api/${rota}`, { method: "POST" });
}