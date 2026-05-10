"""Consumidor da fila de notificações."""

from messaging.consumer_base import start_consumer


def send_notification(event: dict) -> None:
    payload = event["payload"]
    print(f"[NOTIFICAÇÕES] Preparando notificação do pedido {payload['pedido_id']}.")
    print(f"[NOTIFICAÇÕES] Canal: {payload['canal']}.")
    print(f"[NOTIFICAÇÕES] Destinatário: {payload['destinatario']}.")
    print(f"[NOTIFICAÇÕES] Mensagem: {payload['mensagem']}")
    print("[NOTIFICAÇÕES] Envio simulado com sucesso.")


def main() -> None:
    start_consumer("notifications", send_notification)


if __name__ == "__main__":
    main()
