"""Funções reutilizáveis para publicação de mensagens JSON."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Dict
from uuid import uuid4

import rabbitpy

from messaging.connection import create_connection
from messaging.topology import QUEUES, declare_topology


def publish_event(queue_key: str, event_type: str, payload: Dict[str, Any]) -> None:
    """Publica um evento JSON na fila associada a queue_key.

    Args:
        queue_key: chave lógica da fila em QUEUES, por exemplo "orders".
        event_type: nome do evento de negócio, por exemplo "PedidoCriado".
        payload: dados específicos do evento.
    """
    if queue_key not in QUEUES:
        available = ", ".join(sorted(QUEUES.keys()))
        raise ValueError(f"Fila lógica inválida: {queue_key}. Opções: {available}")

    definition = QUEUES[queue_key]
    event = {
        "event_id": str(uuid4()),
        "event_type": event_type,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "payload": payload,
    }

    with create_connection() as connection:
        with connection.channel() as channel:
            exchange = declare_topology(channel)
            body = json.dumps(event, ensure_ascii=False)
            message = rabbitpy.Message(channel, body)
            message.publish(exchange, definition.routing_key)

    print(
        f"[PRODUTOR] Evento {event_type} publicado em {definition.name} "
        f"com routing key '{definition.routing_key}'."
    )
