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


categories = ['EVENTO', 'PROMOCAO']
priorities = ['ALTA', 'MEDIA', 'BAIXA']
# statuses = ['ABERTA', 'ENCERRADA']
department = 'MKT'

# Create a message 
for i in range (10_000):

    # Assemble message
    category = random.choice(categories)
    priority = random.choice(priorities)
    # status = random.choice(statuses)

    time_stamp = dt.datetime.strftime(dt.datetime.now(), format='%Y-%m-%d %H:%M:%S.%f')
    message = f'{time_stamp} {i:6} Mensagem criada por {department} com prioridade {priority} para informar sobre {category}.'


## REGRAS DE ENVIO


## 1. Eventos importantes (prioridade alta) são publicados no modo *direct*, rota *eventos_importantes*.

    if (category=='EVENTO') & (priority == 'ALTA'):

        # Define exchange name and route
        exchange_name_ = 'exchange_direct'
        route_ = 'eventos_importantes'

        # Publish message
        channel.basic_publish(
            exchange=exchange_name_,
            routing_key=route_,
            body=message
        )

## 2. Todas as promoções são publicadas no modo *topic*, rota *department.category.priority*.

    if category == 'PROMOCAO':
        # Define exchange name and route
        exchange_name_ = 'exchange_topic'
        route_ = f'{department.lower()}.{category.lower()}.{priority.lower()}'

        # Publish message
        channel.basic_publish(
            exchange=exchange_name_,
            routing_key=route_,
            body=message
        )    


    print(f" [x] Sent {message}")
    time.sleep(random.randint(0,3))



# Close the connection
connection.close()