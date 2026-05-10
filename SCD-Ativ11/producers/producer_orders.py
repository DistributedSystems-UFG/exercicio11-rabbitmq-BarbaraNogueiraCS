"""Produtor de eventos de pedidos criados."""

from messaging.publisher import publish_event


ORDERS = [
    {
        "pedido_id": 1001,
        "cliente": "Ana Souza",
        "email": "ana.souza@example.com",
        "produto": "Notebook",
        "quantidade": 1,
        "valor_total": 3500.00,
    },
    {
        "pedido_id": 1002,
        "cliente": "Bruno Lima",
        "email": "bruno.lima@example.com",
        "produto": "Mouse sem fio",
        "quantidade": 2,
        "valor_total": 180.00,
    },
    {
        "pedido_id": 1003,
        "cliente": "Carla Mendes",
        "email": "carla.mendes@example.com",
        "produto": "Monitor",
        "quantidade": 1,
        "valor_total": 1200.00,
    },
]


def main() -> None:
    for order in ORDERS:
        publish_event("orders", "PedidoCriado", order)


if __name__ == "__main__":
    main()
