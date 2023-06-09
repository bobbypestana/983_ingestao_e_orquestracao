import pika

# Create a connection to the RabbitMQ server running on the local machine
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare a queue to consume messages from
result = channel.queue_declare(
    queue='Q1', 
    durable=True
)

# Declare a queue to consume messages from
result = channel.queue_declare(
    queue='Q2_A', 
    durable=True
)

# Declare a queue to consume messages from
result = channel.queue_declare(
    queue='Q2_B', 
    durable=True
)

# Declare a queue to consume messages from
result = channel.queue_declare(
    queue='Q2_C', 
    durable=True
)

# Declare a queue to consume messages from
result = channel.queue_declare(
    queue='Q2_D', 
    durable=True
)

# Declare a queue to consume messages from
result = channel.queue_declare(
    queue='Q3', 
    durable=True
)

# Declare a queue to consume messages from
result = channel.queue_declare(
    queue='Q4', 
    durable=True
)

connection.close()