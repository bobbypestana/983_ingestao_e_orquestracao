# Importando as bibliotecas necessárias
from kafka.admin import KafkaAdminClient
from config import KAFKA_BROKERS, TOPICS, CLIENTS, PARTITIONS

# Configurando o cliente do administrador Kafka
admin_client = KafkaAdminClient(
    bootstrap_servers=KAFKA_BROKERS  # Servidores Kafka
)

# Listando os tópicos para deletar
topics_to_delete = admin_client.list_topics()

# Iterando sobre os tópicos a serem deletados
for topic in topics_to_delete:
    try:
        # Tentando deletar o tópico
        delete_result = admin_client.delete_topics([topic])
        print(delete_result)
        print('\n')
    except Exception as ex:
        # Imprimindo o erro se não for possível deletar o tópico
        print(f'Erro: {ex}')
        print('\n')
