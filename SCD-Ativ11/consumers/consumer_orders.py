"""Consumidor da fila de pedidos criados."""

from messaging.consumer_base import start_consumer


def process_order(event: dict) -> None:
    payload = event["payload"]
    print(f"[PEDIDOS] Pedido {payload['pedido_id']} recebido.")
    print(f"[PEDIDOS] Cliente: {payload['cliente']} - Produto: {payload['produto']}.")
    print(f"[PEDIDOS] Validando quantidade {payload['quantidade']} e valor R$ {payload['valor_total']:.2f}...")
    print(f"[PEDIDOS] Pedido {payload['pedido_id']} registrado com sucesso.")


def main() -> None:
    start_consumer("orders", process_order)


if __name__ == "__main__":
    main()
