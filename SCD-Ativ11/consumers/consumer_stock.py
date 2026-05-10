"""Consumidor da fila de reserva de estoque."""

from messaging.consumer_base import start_consumer


AVAILABLE_STOCK = {
    "Notebook": 3,
    "Mouse sem fio": 10,
    "Monitor": 0,
}


def reserve_stock(event: dict) -> None:
    payload = event["payload"]
    product = payload["produto"]
    requested_quantity = payload["quantidade"]
    available_quantity = AVAILABLE_STOCK.get(product, 0)

    print(f"[ESTOQUE] Solicitação de reserva recebida para o pedido {payload['pedido_id']}.")
    print(f"[ESTOQUE] Produto: {product} - Quantidade solicitada: {requested_quantity}.")
    print(f"[ESTOQUE] Depósito: {payload['deposito']} - Disponível: {available_quantity}.")

    if available_quantity >= requested_quantity:
        AVAILABLE_STOCK[product] = available_quantity - requested_quantity
        print(f"[ESTOQUE] Reserva realizada. Saldo atual: {AVAILABLE_STOCK[product]}.")
    else:
        print("[ESTOQUE] Reserva não realizada. Estoque insuficiente.")


def main() -> None:
    start_consumer("stock", reserve_stock)


if __name__ == "__main__":
    main()
