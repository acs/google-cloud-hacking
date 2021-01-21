import time

from google.cloud import pubsub_v1
import google.api_core.exceptions


PROJECT_ID = "k8strain-301514"


# Executed in a thread to receive messages using streaming pull
def receive_message_1(message):
    print("Message from subscription 1 ", message.data)
    message.ack()
    # Be careful not reading lots of messages too fast
    time.sleep(1)


def receive_message_2(message):
    print("Message from subscription 2 ", message.data)
    message.ack()
    # Be careful not reading lots of messages too fast
    time.sleep(1)


if __name__ == '__main__':

    topic_id = "acs1"
    subscription_id_1 = "acs1"
    subscription_id_2 = "acsSub1"

    topic_name = "projects/%s/topics/%s" % (PROJECT_ID, topic_id)

    subscription_name_1 = "projects/%s/subscriptions/%s" % (PROJECT_ID, subscription_id_1)
    subscription_name_2 = "projects/%s/subscriptions/%s" % (PROJECT_ID, subscription_id_2)

    subscriber = pubsub_v1.SubscriberClient()

    try:
        try:
            subscriber.create_subscription(name=subscription_name_1, topic=topic_name)
            subscriber.create_subscription(name=subscription_name_2, topic=topic_name)
        except google.api_core.exceptions.AlreadyExists:
            print("Subscriptions already exists")

        print("Reading messages from %s" % subscription_name_1)
        future1 = subscriber.subscribe(subscription_name_1, receive_message_1)

        print("Reading messages from %s" % subscription_name_2)
        future2 = subscriber.subscribe(subscription_name_2, receive_message_2)

        future1.result()
        # future2.result()

    except KeyboardInterrupt:
        future1.cancel()
        future2.cancel()

