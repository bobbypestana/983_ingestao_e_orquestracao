import pika

# Create a connection to the RabbitMQ server running on the local machine
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare a queue to consume messages from
result = channel.queue_delete(
    queue='Q1'
)

# Declare a queue to consume messages from
result = channel.queue_delete(
    queue='Q2_A'
)

# Declare a queue to consume messages from
result = channel.queue_delete(
    queue='Q2_B'
)

# Declare a queue to consume messages from
result = channel.queue_delete(
    queue='Q2_C'
)

# Declare a queue to consume messages from
result = channel.queue_delete(
    queue='Q2_D',
)

# Declare a queue to consume messages from
result = channel.queue_delete(
    queue='Q3'
)

# Declare a queue to consume messages from
result = channel.queue_delete(
    queue='Q4'
)

# Declare a queue to consume messages from
result = channel.exchange_delete('exchange_topic')
result = channel.exchange_delete('exchange_direct')
result = channel.exchange_delete('exchange_fanout')


connection.close()