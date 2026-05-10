"""Consumidor da fila de pagamentos processados."""

from messaging.consumer_base import start_consumer


def process_payment(event: dict) -> None:
    payload = event["payload"]
    status = payload["status"]

    print(f"[PAGAMENTOS] Pagamento {payload['pagamento_id']} recebido.")
    print(f"[PAGAMENTOS] Pedido: {payload['pedido_id']} - Valor: R$ {payload['valor']:.2f}.")

    if status == "aprovado":
        print(f"[PAGAMENTOS] Pagamento aprovado via {payload['metodo']}.")
        print("[PAGAMENTOS] Pedido liberado para separação no estoque.")
    else:
        reason = payload.get("motivo", "motivo não informado")
        print(f"[PAGAMENTOS] Pagamento recusado. Motivo: {reason}.")
        print("[PAGAMENTOS] Pedido bloqueado até nova tentativa de pagamento.")


def main() -> None:
    start_consumer("payments", process_payment)


if __name__ == "__main__":
    main()
