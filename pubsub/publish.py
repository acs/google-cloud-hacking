import time

from google.cloud import pubsub_v1

PROJECT_ID = "k8strain-301514"

if __name__ == '__main__':

    topic_id = "acs1"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, topic_id)

    start_time = time.time()

    publisher.publish(topic_path, b'New message from python publisher %i!' % (start_time), spam='eggs')
    end_time_ms = (time.time() - start_time) * 1000

    print("Message published to %s in %4.2f miliseconds" % (topic_path, end_time_ms))

