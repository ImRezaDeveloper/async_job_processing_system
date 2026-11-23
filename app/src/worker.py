import pika
from fastapi import FastAPI

app = FastAPI()

connection = pika.BlockingConnection(parameters=pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

@app.post('/jobs/reports')
def send_job():
    channel.queue_declare('fastapi')
    channel.basic_publish(exchange='', routing_key='fastapi', body="this is test 12 body")
    print("task sent!")
    return "task sent"
    # connection.close()

# send_job()