# admin_consumer.py
from kafka import KafkaConsumer
from const import *

topics = ['admin_logs', 'system_alerts']

consumer = KafkaConsumer(
    *topics,
    bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
    auto_offset_reset='latest'
)

print(f"Monitorando tópicos administrativos: {topics}")
print("Pressione Ctrl+C para sair.\n")

try:
    for msg in consumer:
        print(f"[{msg.topic}] {msg.value.decode('utf-8')}")
except KeyboardInterrupt:
    pass
finally:
    print("\nEncerrando admin_consumer.")
    consumer.close()

