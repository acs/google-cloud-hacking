import time

from google.cloud import pubsub_v1
import google.api_core.exceptions


PROJECT_ID = "k8strain-301514"


# Executed in a thread to receive messages using streaming pull
def receive_message(message):
    print(message.data)
    message.ack()
    # Be careful not reading lots of messages too fast
    time.sleep(1)


if __name__ == '__main__':

    topic_id = "acs1"
    subscription_id = "acs1"

    topic_name = "projects/%s/topics/%s" % (PROJECT_ID, topic_id)

    subscription_name = "projects/%s/subscriptions/%s" % (PROJECT_ID, subscription_id)

    subscriber = pubsub_v1.SubscriberClient()

    try:
        try:
            subscriber.create_subscription(name=subscription_name, topic=topic_name)
        except google.api_core.exceptions.AlreadyExists:
            print("The subscription %s already exists" % (subscription_name))

        print("Reading messages from %s" % subscription_name)
        future = subscriber.subscribe(subscription_name, receive_message)

        future.result()

    except KeyboardInterrupt:
        future.cancel()

