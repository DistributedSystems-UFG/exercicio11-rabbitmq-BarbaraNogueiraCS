"""Base reutilizável para criação de consumidores."""

from __future__ import annotations

import json
import time
from typing import Any, Callable, Dict

import rabbitpy

from messaging.connection import create_connection
from messaging.topology import QUEUES, declare_topology


Handler = Callable[[Dict[str, Any]], None]


def _decode_message(message: rabbitpy.Message) -> Dict[str, Any]:
    raw_body = message.body
    if isinstance(raw_body, bytes):
        raw_body = raw_body.decode("utf-8")
    return json.loads(raw_body)


def start_consumer(queue_key: str, handler: Handler) -> None:
    """Inicia um consumidor para a fila indicada.

    O consumidor fica executando até o usuário interromper com CTRL+C.
    Cada mensagem recebida é processada pelo handler e confirmada com ack().
    """
    if queue_key not in QUEUES:
        available = ", ".join(sorted(QUEUES.keys()))
        raise ValueError(f"Fila lógica inválida: {queue_key}. Opções: {available}")

    definition = QUEUES[queue_key]

    with create_connection() as connection:
        with connection.channel() as channel:
            declare_topology(channel)
            queue = rabbitpy.Queue(channel, definition.name, durable=True, auto_delete=False)
            queue.declare()

            print(f"[CONSUMIDOR] Aguardando mensagens em: {definition.name}")
            print("[CONSUMIDOR] Pressione CTRL+C para encerrar.\n")

            try:
                for message in queue:
                    event = _decode_message(message)
                    print(f"[CONSUMIDOR] Mensagem recebida: {event['event_type']}")
                    handler(event)
                    message.ack()
                    print("[CONSUMIDOR] Mensagem confirmada com ACK.\n")
                    time.sleep(0.5)
            except KeyboardInterrupt:
                print("\n[CONSUMIDOR] Encerrado pelo usuário.")
