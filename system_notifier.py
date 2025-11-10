# system_notifier.py
from kafka import KafkaProducer
from const import *
import time

producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])
topic = 'system_alerts'

print("Notificador do sistema iniciado. Pressione Ctrl+C para parar.")

try:
    while True:
        msg = input("Mensagem de alerta: ")
        if msg.lower() == 'exit':
            break
        producer.send(topic, value=f"[ALERTA DO SISTEMA]: {msg}".encode('utf-8'))
        producer.flush()
except KeyboardInterrupt:
    pass
finally:
    print("\nEncerrando notificador.")
    producer.close()

