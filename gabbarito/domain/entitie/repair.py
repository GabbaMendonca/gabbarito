class Repair:
    def __init__(
        self,
        cliente,
        ticket,
        circuito,
        uf,
        resumo,
        posto,
        abertura,
        posicionamento,
        prox_acao,
    ):
        self.cliente = cliente
        self.ticket = ticket
        self.circuito = circuito
        self.uf = uf
        self.resumo = resumo
        self.posto = posto
        self.abertura = abertura
        self.posicionamento = posicionamento
        self.prox_acao = prox_acao
        self.ip = None
        self.status = None

    def __str__(self):
        return f"{self.cliente} - {self.ticket} - {self.circuito} - {self.uf} - {self.resumo} - {self.posto} - {self.abertura} - {self.posicionamento} - {self.prox_acao}"

    def __repr__(self):
        return f"Repair(cliente={self.cliente}, ticket={self.ticket}, circuito={self.circuito}, uf={self.uf}, resumo={self.resumo}, posto={self.posto}, abertura={self.abertura}, posicionamento={self.posicionamento}, prox_acao={self.prox_acao})"
