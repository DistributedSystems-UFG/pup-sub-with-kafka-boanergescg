# producer.py
from kafka import KafkaProducer
from const import *
import sys

try:
    topic = sys.argv[1]
    username = sys.argv[2]
except IndexError:
    print('Usage: python3 producer.py <topic_name> <username>')
    exit(1)
    
producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

# Novo tópico para logs, conforme solicitado
admin_topic = 'admin_logs'

print(f"Enviando para o grupo '{topic}' como '{username}'")
print("Digite 'exit' para sair.")

try:
    while True:
        msg_text = input('> ')
        
        if msg_text.lower() == 'exit':
            break
            
        # 1. Envia a mensagem principal para o tópico do chat
        formatted_msg = f"[{username}]: {msg_text}"
        producer.send(topic, value=formatted_msg.encode('utf-8'))
        
        # 2. Envia a mensagem de log para o tópico de administração
        log_msg = f"[LOG] User '{username}' enviou para o grupo '{topic}'"
        producer.send(admin_topic, value=log_msg.encode('utf-8'))
        
        # Garante o envio imediato
        producer.flush() 
            
except KeyboardInterrupt:
    pass
finally:
    print("\nEncerrando producer.")
    producer.close()
