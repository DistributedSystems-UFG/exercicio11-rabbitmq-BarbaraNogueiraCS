"""Configurações da aplicação.

Os valores podem ser alterados por variáveis de ambiente, evitando deixar
endereços, usuários e senhas fixos no código-fonte.
"""

import os
from urllib.parse import quote


RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "192.168.100.14")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "myuser")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "abc123")
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "my_vhost")


def amqp_url() -> str:
    """Monta a URL de conexão AMQP usada pelos produtores e consumidores."""
    user = quote(RABBITMQ_USER, safe="")
    password = quote(RABBITMQ_PASSWORD, safe="")
    vhost = quote(RABBITMQ_VHOST, safe="")
    return f"amqp://{user}:{password}@{RABBITMQ_HOST}:{RABBITMQ_PORT}/{vhost}"
