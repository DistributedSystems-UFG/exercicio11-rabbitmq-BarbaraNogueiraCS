"""Declaração da topologia de mensageria da aplicação.

Neste arquivo ficam os nomes do exchange, das filas e das routing keys.
Centralizar esses nomes evita erros de digitação entre produtores e consumidores.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import rabbitpy


EXCHANGE_NAME = "loja.direct"
EXCHANGE_TYPE = "direct"


@dataclass(frozen=True)
class QueueDefinition:
    name: str
    routing_key: str
    description: str


QUEUES: Dict[str, QueueDefinition] = {
    "orders": QueueDefinition(
        name="loja.pedidos.criados",
        routing_key="pedido.criado",
        description="Pedidos criados por clientes",
    ),
    "payments": QueueDefinition(
        name="loja.pagamentos.processados",
        routing_key="pagamento.processado",
        description="Resultados de processamento de pagamentos",
    ),
    "stock": QueueDefinition(
        name="loja.estoque.reservas",
        routing_key="estoque.reserva",
        description="Solicitações de reserva/baixa de produtos no estoque",
    ),
    "notifications": QueueDefinition(
        name="loja.notificacoes.envio",
        routing_key="notificacao.envio",
        description="Mensagens de notificação para clientes",
    ),
}


def declare_topology(channel: rabbitpy.Channel) -> rabbitpy.Exchange:
    """Cria exchange, filas e vínculos caso ainda não existam.

    A função é chamada por produtores e consumidores para garantir que a
    infraestrutura necessária exista antes de publicar ou consumir mensagens.
    """
    exchange = rabbitpy.Exchange(
        channel,
        EXCHANGE_NAME,
        exchange_type=EXCHANGE_TYPE,
        durable=True,
        auto_delete=False,
    )
    exchange.declare()

    for definition in QUEUES.values():
        queue = rabbitpy.Queue(
            channel,
            definition.name,
            durable=True,
            auto_delete=False,
        )
        queue.declare()
        queue.bind(exchange, definition.routing_key)

    return exchange
