# Comparação entre RabbitMQ/AMQP e Kafka na aplicação implementada

## 1. Contexto da aplicação

A aplicação implementada simula uma loja online com quatro tipos de tarefas assíncronas:

- processamento de pedidos;
- processamento de pagamentos;
- reserva de estoque;
- envio de notificações.

Cada tarefa possui uma fila própria no RabbitMQ e um consumidor específico responsável por processá-la.

## 2. RabbitMQ/AMQP

RabbitMQ é adequado para esta aplicação porque o problema central é distribuir tarefas para consumidores específicos. O produtor não precisa conhecer o consumidor diretamente. Ele publica uma mensagem no exchange, e o RabbitMQ encaminha a mensagem para a fila correta com base na routing key.

Na aplicação:

- `pedido.criado` vai para `loja.pedidos.criados`;
- `pagamento.processado` vai para `loja.pagamentos.processados`;
- `estoque.reserva` vai para `loja.estoque.reservas`;
- `notificacao.envio` vai para `loja.notificacoes.envio`.

Esse modelo facilita a separação de responsabilidades, pois cada consumidor cuida apenas da sua fila.

## 3. Kafka

Kafka também poderia ser usado, mas sua ideia principal é trabalhar com tópicos de eventos, retenção e leitura por consumidores ao longo do tempo. Ele é muito forte para fluxos contínuos de dados, logs, telemetria, eventos analíticos e cenários em que os eventos precisam ser armazenados e reprocessados.

Para esta aplicação pequena, Kafka funcionaria, mas adicionaria mais complexidade operacional, pois seria necessário lidar com tópicos, partições, offsets e grupos de consumidores.

## 4. Comparação direta

| Critério | RabbitMQ/AMQP | Kafka |
|---|---|---|
| Unidade principal | Fila | Tópico |
| Melhor uso | Distribuição de tarefas | Fluxo contínuo de eventos |
| Roteamento | Forte, com exchanges e routing keys | Baseado em tópicos e partições |
| Consumo | Consumidores retiram/processam mensagens de filas | Consumidores leem eventos de tópicos |
| Histórico/reprocessamento | Mais focado na entrega da mensagem | Mais forte para retenção e replay de eventos |
| Complexidade para a aplicação | Menor | Maior |
| Adequação ao exercício | Muito adequada | Adequada, mas mais complexa |

## 5. Conclusão

Para a aplicação implementada, RabbitMQ/AMQP é mais adequado porque a atividade pede explicitamente filas de mensagens, produtores enviando tarefas e consumidores específicos processando essas tarefas. Kafka seria mais indicado se a aplicação precisasse manter um histórico durável de eventos por mais tempo, permitir reprocessamento frequente ou lidar com grande volume contínuo de dados.
