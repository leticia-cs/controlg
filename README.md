# controlg

Python, Flask, JS, HTML, JSON

---

## Como usar

### Configurando
ANTES DE TUDO. Descubra o endereço IP da sua televisão LG. Guarde essa informação.

1. Baixe o repositório no seu computador
2. Vá ao novo diretório e descompacte (.zip --> pasta normal)
3. Vá em `tv_ip.py` e adicione o endereço IP da sua TV ao array. Salve o arquivo e feche-o.

### Rodando

ANTES DE PROSSEGUIR: Confira que o computador está conectado à mesma rede da televisão.

1. Abra uma janela de terminal no diretório descompactado e digite o seguinte: `flask run`
2. Isso mostrará um endereço web com números. Clique nele para acessar a interface do controle.
3. Pronto. Qualquer telefone também conseguirá acessar o controle.

Durante essa etapa, se for a primeira vez que roda, é provável que a televisão peça uma confirmação. Só aceitar.

---

## Q&A

### 1. Não estou vendo a confirmação da televisão
Veja se o seguinte está ATIVADO:
`Configurações > Rede > LG Connect Apps`

--> ou `LG Connect IP`

### 2. Como acho o IP da TV?
- Conecte com a internet. Não funciona com a TV sem conexão.
- Vá em informações do sistema ou busque no próprio site do roteador por dispositivos conectados
