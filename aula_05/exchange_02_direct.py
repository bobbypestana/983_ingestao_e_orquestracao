import pika
import datetime as dt
import time
import random

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

# Create a channel
channel = connection.channel()

type_ = 'direct'

# Define exchange name
exchange_name_ = f'exchange_{type_}'

# Declare exchange
channel.exchange_declare(
    exchange=exchange_name_,
    exchange_type=type_
)