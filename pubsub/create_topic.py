from google.cloud import pubsub_v1
import google.api_core.exceptions

PROJECT_ID = "k8strain-301514"

if __name__ == '__main__':

    topic_creation_id = "acs2"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, topic_creation_id)

    try:
        topic = publisher.create_topic(request={"name": topic_path})
        print("Created topic: {}".format(topic.name))
    except google.api_core.exceptions.AlreadyExists:
        print("The topic %s already exists" % topic_path)
