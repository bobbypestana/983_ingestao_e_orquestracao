# Importando as bibliotecas necessárias
from kafka.admin import KafkaAdminClient, NewTopic
from config import KAFKA_BROKERS, TOPICS, CLIENTS, PARTITIONS, REPLICATION_FACTOR


def create_topics():
    # Configurando o cliente do administrador Kafka
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKERS)
    
    # Criando os tópicos
    for topic_temp in TOPICS:
        try:
            # Configurando o novo tópico
            topic = NewTopic(
                name=topic_temp, 
                num_partitions=PARTITIONS, 
                replication_factor=REPLICATION_FACTOR
            )
            # Tentando criar o tópico
            admin_client.create_topics(new_topics=[topic], validate_only=False)
            print(f'Topic {topic.name} created successfully.')
            print('\n')

        except Exception as ex:
            # Imprimindo o erro se não for possível criar o tópico
            print(f'Erro: {ex}')
            print('\n')

    # Encerrando o objeto KafkaAdminClient
    admin_client.close()


if __name__ == "__main__":
    create_topics()
