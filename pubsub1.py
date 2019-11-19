from google.cloud import pubsub_v1

# TODO project_id = "Your Google Cloud Project ID"
# TODO topic_name = "Your Pub/Sub topic name"

topic_name = "geginfo"
project_id = 'iot-geg-2019'



#topic = publisher.create_topic(topic_path)

def publish_message(project_id, topic_name,data):

    from google.cloud import pubsub_v1
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    future = publisher.publish(topic_path, data=data)
    print(future.result())


def publish_messages(project_id, topic_name):
    """Publishes multiple messages to a Pub/Sub topic."""
    # [START pubsub_quickstart_publisher]
    # [START pubsub_publish]
    from google.cloud import pubsub_v1

    # TODO project_id = "Your Google Cloud Project ID"
    # TODO topic_name = "Your Pub/Sub topic name"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = publisher.topic_path(project_id, topic_name)

    for n in range(1, 10):
        data = u'Message number {}'.format(n)
        # Data must be a bytestring
        data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        print(future.result())

    print('Published messages.')
    # [END pubsub_quickstart_publisher]
    # [END pubsub_publish]

def receive_messages(project_id, subscription_name):
    """Receives messages from a pull subscription."""
    # [START pubsub_subscriber_async_pull]
    # [START pubsub_quickstart_subscriber]
    import time

    from google.cloud import pubsub_v1

    # TODO project_id = "Your Google Cloud Project ID"
    # TODO subscription_name = "Your Pub/Sub subscription name"

    subscriber = pubsub_v1.SubscriberClient()
    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    def callback(message):
        #print('Received message: {}'.format(message))
        print(message.data.decode())
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    # The subscriber is non-blocking. We must keep the main thread from
    # exiting to allow it to process messages asynchronously in the background.
    print('Listening for messages on {}'.format(subscription_path))
    while True:
        time.sleep(60)
    # [END pubsub_subscriber_async_pull]
    # [END pubsub_quickstart_subscriber]

subscription_name = 'my-sub'
#publish_messages(project_id, topic_name)
#publish_message(project_id, topic_name,str.encode('Esta es una prueba 100'))
receive_messages(project_id, subscription_name)
