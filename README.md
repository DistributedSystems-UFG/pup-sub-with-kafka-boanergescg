[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eycvIrW-)
# pub-sub-basics-with-kafka
Very simple pub-sub example

# Chat distribuído com Kafka (Publish–Subscribe)

Este projeto implementa uma aplicação de chat em grupo usando o middleware **Apache Kafka**.

Cada grupo corresponde a um **tópico Kafka**, e os usuários podem trocar mensagens em tempo real.  
Além disso, há dois tópicos administrativos:
- `admin_logs`: registra todas as mensagens enviadas
- `system_alerts`: envia notificações gerais do sistema

### Estrutura dos arquivos
- `producer.py`: envia mensagens aos grupos
- `consumer.py`: recebe mensagens de um grupo
- `admin_consumer.py`: monitora logs e alertas
- `system_notifier.py`: publica alertas do sistema
- `const.py`: configurações de conexão Kafka

### Execução
```bash
python3 producer.py chat_grupo1 usuario1
python3 consumer.py chat_grupo1
python3 admin_consumer.py
python3 system_notifier.py

Exemplo: Iniciar o Kafka
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties

Criar tópicos
kafka-topics.sh --create --topic chat_grupo1 --bootstrap-server 172.31.91.151:9092
kafka-topics.sh --create --topic admin_logs --bootstrap-server 172.31.91.151:9092
kafka-topics.sh --create --topic system_alerts --bootstrap-server 172.31.91.151:9092

Inicar consumidores
python3 consumer.py chat_grupo1
python3 admin_consumer.py

Enviar mensagens
python3 producer.py chat_grupo1 boanerges
python3 system_notifier.py


