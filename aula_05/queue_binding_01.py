import pika

# Create a connection to the RabbitMQ server running on the local machine
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

exchange_name_ = 'exchange_topic'
queue_name_ = 'Q1'
routing_key_ = 'it.*.alta.aberta'

channel.queue_bind(
            exchange=exchange_name_,
            queue=queue_name_,
            routing_key=routing_key_
        )

connection.close()