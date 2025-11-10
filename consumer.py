# consumer.py
from kafka import KafkaConsumer
from const import *
import sys

try:
    topic = sys.argv[1]
except IndexError:
    print('Usage: python3 consumer.py <topic_name>')
    exit(1)

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT],
    # Ignora mensagens antigas e foca apenas nas novas
    auto_offset_reset='latest'
)

print(f"Ouvindo o grupo '{topic}'...")
print("Pressione Ctrl+C para sair.")

try:
    for msg in consumer:
        # Decodifica a mensagem de bytes para string UTF-8
        print(msg.value.decode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    print("\nEncerrando consumer.")
    consumer.close()
