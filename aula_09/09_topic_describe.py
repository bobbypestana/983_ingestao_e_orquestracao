# Importando as bibliotecas necessárias
from kafka.admin import KafkaAdminClient
from config import KAFKA_BROKERS, TOPICS, CLIENTS, PARTITIONS

# Cria uma instância do KafkaAdminClient
admin_client = KafkaAdminClient(
    bootstrap_servers=KAFKA_BROKERS,
)

# Descreve os tópicos especificados
topic_description = admin_client.describe_topics(TOPICS)

# Imprime cabeçalho da tabela
print(
    f'{"Tópico":<20} {"Partição":<9} {"Líder"} {"Réplicas":<15} '
    f'{"In-Sync Replicas (isr)":<10} {"offline_replicas"} '
)

# Itera sobre a descrição do tópico
for topic in topic_description:
    # Itera sobre as partições do tópico
    for partition in topic["partitions"]:
        # Imprime detalhes da partição
        print(
            f'{topic["topic"]:<20} {partition["partition"]:<9} {partition["leader"]:<5} '
            f'{partition["replicas"]} {" ":10} {partition["isr"]} {" ":20} {partition["offline_replicas"]} '
        )
