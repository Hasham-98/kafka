from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import sys
import random

me = 'hisham.karam-1'
groupId = me + '-group1'
conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094',  # Kafka broker address
    'group.id': groupId,
    'enable.auto.commit' : True,  
    'auto.offset.reset': 'smallest'
}
consumer = Consumer(conf)
topics = [me]
consumer.subscribe(topics)

#def detect_object(id):
#    return random.choice(['car','house','person'])

#def msg_process(msg):
#    #for msg in consumer:
#    img_info = msg.value().decode('utf-8')
#    print("got a message of image : ",img_info)
#    img_id = str(img_info['id'])
#    detect_img = detect_object(img_id)
#    print(detect_img)

def msg_process(msg):
    print("a new message delivered : ", msg.value())

       
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None: continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
        
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            msg_process(msg)
finally:
    consumer.close()


