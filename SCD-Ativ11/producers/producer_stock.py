"""Produtor de eventos de reserva de estoque."""

from messaging.publisher import publish_event


STOCK_RESERVATIONS = [
    {
        "pedido_id": 1001,
        "produto": "Notebook",
        "quantidade": 1,
        "deposito": "GO-01",
    },
    {
        "pedido_id": 1002,
        "produto": "Mouse sem fio",
        "quantidade": 2,
        "deposito": "GO-01",
    },
    {
        "pedido_id": 1003,
        "produto": "Monitor",
        "quantidade": 1,
        "deposito": "GO-02",
    },
]


def main() -> None:
    for reservation in STOCK_RESERVATIONS:
        publish_event("stock", "ReservaEstoqueSolicitada", reservation)


if __name__ == "__main__":
    main()
