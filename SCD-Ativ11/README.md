# Exercício 11 — Filas de Mensagens com AMQP/RabbitMQ

## 1. Descrição

Este projeto implementa uma aplicação distribuída simples baseada em filas de mensagens usando RabbitMQ/AMQP e Python.

O domínio escolhido é uma loja online. A aplicação simula quatro áreas de negócio:

- pedidos;
- pagamentos;
- estoque;
- notificações.

Cada área possui uma fila específica no RabbitMQ, produtores que publicam eventos e consumidores que processam esses eventos.

## 2. Arquitetura

```text
Produtores Python
   |
   v
Exchange direct: loja.direct
   |
   +-- routing key pedido.criado ---------> fila loja.pedidos.criados ---------> consumidor de pedidos
   +-- routing key pagamento.processado --> fila loja.pagamentos.processados --> consumidor de pagamentos
   +-- routing key estoque.reserva -------> fila loja.estoque.reservas -------> consumidor de estoque
   +-- routing key notificacao.envio -----> fila loja.notificacoes.envio -----> consumidor de notificações
```

## 3. Estrutura de pastas

```text
exercicio11_rabbitmq_loja/
├── README.md
├── requirements.txt
├── .env.example
├── config.py
├── messaging/
│   ├── __init__.py
│   ├── connection.py
│   ├── topology.py
│   ├── publisher.py
│   └── consumer_base.py
├── producers/
│   ├── __init__.py
│   ├── producer_orders.py
│   ├── producer_payments.py
│   ├── producer_stock.py
│   ├── producer_notifications.py
│   └── run_all_producers.py
├── consumers/
│   ├── __init__.py
│   ├── consumer_orders.py
│   ├── consumer_payments.py
│   ├── consumer_stock.py
│   └── consumer_notifications.py
├── docs/
│   └── comparacao_rabbitmq_kafka.md
└── scripts/
    └── rabbitmq_setup_commands.md
```

## 4. Pré-requisitos

- Python 3 instalado;
- RabbitMQ Server instalado e em execução;
- usuário, senha e vhost configurados no RabbitMQ.

## 5. Instalação das dependências Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 6. Configuração da conexão

Por padrão, a aplicação usa:

```text
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_USER=myuser
RABBITMQ_PASSWORD=abc123
RABBITMQ_VHOST=my_vhost
```

Se o RabbitMQ estiver em outro servidor, configure as variáveis de ambiente:

```bash
export RABBITMQ_HOST=IP_DO_SERVIDOR
export RABBITMQ_PORT=5672
export RABBITMQ_USER=myuser
export RABBITMQ_PASSWORD=abc123
export RABBITMQ_VHOST=my_vhost
```

## 7. Como executar

### Terminal 1 — consumidor de pedidos

```bash
python -m consumers.consumer_orders
```

### Terminal 2 — consumidor de pagamentos

```bash
python -m consumers.consumer_payments
```

### Terminal 3 — consumidor de estoque

```bash
python -m consumers.consumer_stock
```

### Terminal 4 — consumidor de notificações

```bash
python -m consumers.consumer_notifications
```

### Terminal 5 — executar todos os produtores

```bash
python -m producers.run_all_producers
```

Também é possível executar os produtores separadamente:

```bash
python -m producers.producer_orders
python -m producers.producer_payments
python -m producers.producer_stock
python -m producers.producer_notifications
```

## 8. Resultado esperado

Os produtores publicarão eventos JSON no RabbitMQ. O exchange `loja.direct` enviará cada evento para a fila correta. Cada consumidor receberá mensagens da sua fila específica, executará uma tarefa simulada e confirmará o processamento com `ack()`.

## 9. Observação

Os consumidores ficam aguardando mensagens continuamente. Para encerrar, pressione `CTRL+C` no terminal correspondente.
