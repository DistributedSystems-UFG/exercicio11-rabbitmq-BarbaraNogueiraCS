# Comandos básicos para preparar o RabbitMQ

Após instalar e iniciar o RabbitMQ, configure um usuário e um vhost compatíveis com a aplicação.

```bash
sudo systemctl start rabbitmq-server
sudo rabbitmqctl add_user myuser abc123
sudo rabbitmqctl add_vhost my_vhost
sudo rabbitmqctl set_permissions -p my_vhost myuser ".*" ".*" ".*"
```

Para verificar o status:

```bash
sudo systemctl status rabbitmq-server
```

Para ativar a interface web de administração, se desejado:

```bash
sudo rabbitmq-plugins enable rabbitmq_management
```

A interface costuma ficar disponível em:

```text
http://localhost:15672
```
