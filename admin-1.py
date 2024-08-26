from confluent_kafka.admin import NewTopic, AdminClient

conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094'  # Kafka broker address
}

admin_client = AdminClient(conf)

me = 'hisham.karam-1'
num_partitions = 3
replication_factor = 1

new_topic = NewTopic(me, num_partitions=num_partitions, replication_factor=replication_factor)

admin_client.create_topics([new_topic])[me].result()
