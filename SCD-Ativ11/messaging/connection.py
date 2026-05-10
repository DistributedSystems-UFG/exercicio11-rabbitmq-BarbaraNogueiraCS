"""Funções de conexão com o RabbitMQ."""

import rabbitpy

from config import amqp_url


def create_connection() -> rabbitpy.Connection:
    """Cria uma conexão AMQP com o RabbitMQ."""
    return rabbitpy.Connection(amqp_url())
