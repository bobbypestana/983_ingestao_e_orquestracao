import pika

# Create a connection to the RabbitMQ server running on the local machine
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

exchange_name_ = 'exchange_direct'
queue_name_ = 'Q2_D'
routing_key_ = 'eventos_importantes'

channel.queue_bind(
            exchange=exchange_name_,
            queue=queue_name_,
            routing_key=routing_key_
        )

connection.close()