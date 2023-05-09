# Importando as bibliotecas necessárias
from kafka import KafkaConsumer, TopicPartition
from config import KAFKA_BROKERS, TOPICS, CLIENTS, PARTITIONS, GROUPS

# Itera sobre todos os grupos de consumidores
for group_id_ in GROUPS:

    # Configura o consumidor Kafka
    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_BROKERS,
        auto_offset_reset='earliest',
        group_id=group_id_,
    )

    # Itera sobre todos os tópicos
    for topic in TOPICS:
        # Obtém todas as partições para o tópico atual
        partitions = consumer.partitions_for_topic(topic)
        
        try:
            # Itera sobre todas as partições
            for partition in partitions:
                # Define a partição específica
                tp = TopicPartition(topic, partition)

                # Atribui a partição ao consumidor
                consumer.assign([tp])
                
                # Obtém a posição atual do offset
                current_offset = consumer.position(tp)
            
                # Obtém o offset mais recente da partição
                end_offset = consumer.end_offsets([tp])[tp]

                # Calcula a quantidade de mensagens não consumidas
                unconsumed_messages = end_offset - current_offset
                
                # Imprime os detalhes do grupo de consumidores, tópico, partição e mensagens não consumidas
                print(
                    f'group_id: {group_id_:18} topic: {topic:20} partition: {partition:3} '
                    f'current_offset: {current_offset:5} end_offset: {end_offset:5} '
                    f'unconsumed_messages: {unconsumed_messages:5}'
                )

                
        except Exception as ex:
            print(f'Erro: {ex}')
    print('\n')
