from confluent_kafka import Producer
import json 

me = 'hisham.karam-1'

conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094',  # Kafka broker address
    'client.id' : me
}

producer = Producer(conf)

def produce_message():
    topic = me    
    producer.produce(topic, key=None, value=input("enter u r text"))
    producer.flush()

if __name__=='__main__':
    produce_message()
