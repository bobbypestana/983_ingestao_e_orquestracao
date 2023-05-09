# Importando as bibliotecas necessárias
from kafka import KafkaProducer
from faker import Faker
import json
import time
import random
import uuid
import datetime as dt
from config import KAFKA_BROKERS, TOPICS, CLIENTS, PARTITIONS

# Instanciando o gerador de dados falsos
fake = Faker()

# Definindo a função de callback para sucesso no envio
def on_send_success(record_metadata):
    print(f'Mensagem  enviada com sucesso para o tópico {record_metadata.topic} na partição {record_metadata.partition} com offset {record_metadata.offset}')

# Definindo a função de callback para erro no envio
def on_send_error(ex):
    print(f'Erro ao enviar mensagem: {ex}')

# Instanciando o produtor Kafka com configurações específicas
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS,
                         value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                         key_serializer=lambda v: json.dumps(v).encode("utf-8"),
                         )

# Função para gerar uma transação fictícia
def generate_transaction():
    trans_time = dt.datetime.now()
    return {
        "customer_id": random.randint(1, CLIENTS),
        "timestamp": trans_time.strftime('%Y-%m-%d %H:%M:%S.%f'),
        "transaction_id": fake.uuid4(),
        "amount": round(random.uniform(1, 1000), 2),
        "currency": "USD",
        "card_brand": random.choice(["Visa", "MC", "Elo", "Amex"]),
    }

# Função principal para enviar transações para o tópico Kafka
def main():
    while True:
        # Gerar uma transação
        transaction = generate_transaction()
        print(transaction)
        # Enviar a transação para o tópico Kafka
        future = producer.send(TOPICS["transactions"], key={"transaction_id": transaction["transaction_id"], "customer_id": transaction["customer_id"], "card_brand": transaction["card_brand"]}, value=transaction)
        try:
            # Tentativa de obter metadados de registro
            record_metadata = future.get(timeout=10)
            # Se bem sucedido, chamar a função de sucesso
            on_send_success(record_metadata)
        except Exception as ex:
            # Se falhar, chamar a função de erro
            on_send_error(ex)
        # Adormecer por um período aleatório de tempo entre 0.5 e 2 segundos
        time.sleep(random.uniform(0.5, 2))

# Certificando-se de que o script é executado apenas quando é o script principal
if __name__:
    main()
