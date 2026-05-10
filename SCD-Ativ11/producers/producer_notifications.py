"""Produtor de eventos de notificação a clientes."""

from messaging.publisher import publish_event


NOTIFICATIONS = [
    {
        "pedido_id": 1001,
        "destinatario": "ana.souza@example.com",
        "canal": "email",
        "mensagem": "Seu pedido 1001 foi recebido e está em processamento.",
    },
    {
        "pedido_id": 1002,
        "destinatario": "bruno.lima@example.com",
        "canal": "email",
        "mensagem": "O pagamento do pedido 1002 foi aprovado.",
    },
    {
        "pedido_id": 1003,
        "destinatario": "carla.mendes@example.com",
        "canal": "email",
        "mensagem": "O pagamento do pedido 1003 foi recusado.",
    },
]


def main() -> None:
    for notification in NOTIFICATIONS:
        publish_event("notifications", "NotificacaoSolicitada", notification)


if __name__ == "__main__":
    main()
