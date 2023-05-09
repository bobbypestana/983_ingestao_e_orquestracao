import pika


# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

# Create a channel
channel = connection.channel()

type_ = 'topic'

# Define exchange name
exchange_name_ = f'exchange_{type_}'

# Declare exchange
channel.exchange_declare(
    exchange=exchange_name_,
    exchange_type=type_
)

connection.close()