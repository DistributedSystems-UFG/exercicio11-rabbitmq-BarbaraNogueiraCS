"""Produtor de eventos de pagamentos processados."""

from messaging.publisher import publish_event


PAYMENTS = [
    {
        "pagamento_id": "PAG-9001",
        "pedido_id": 1001,
        "status": "aprovado",
        "metodo": "cartao_credito",
        "valor": 3500.00,
    },
    {
        "pagamento_id": "PAG-9002",
        "pedido_id": 1002,
        "status": "aprovado",
        "metodo": "pix",
        "valor": 180.00,
    },
    {
        "pagamento_id": "PAG-9003",
        "pedido_id": 1003,
        "status": "recusado",
        "metodo": "cartao_credito",
        "valor": 1200.00,
        "motivo": "limite insuficiente",
    },
]


def main() -> None:
    for payment in PAYMENTS:
        publish_event("payments", "PagamentoProcessado", payment)


if __name__ == "__main__":
    main()
