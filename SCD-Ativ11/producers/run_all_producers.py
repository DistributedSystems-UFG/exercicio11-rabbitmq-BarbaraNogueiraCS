"""Executa todos os produtores para gerar uma massa de mensagens de teste."""

from producers import (
    producer_notifications,
    producer_orders,
    producer_payments,
    producer_stock,
)


def main() -> None:
    producer_orders.main()
    producer_payments.main()
    producer_stock.main()
    producer_notifications.main()


if __name__ == "__main__":
    main()
