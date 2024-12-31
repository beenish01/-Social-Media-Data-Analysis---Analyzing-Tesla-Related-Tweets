from confluent_kafka import Consumer, KafkaError
import sqlite3
import json

def create_db():
    conn = sqlite3.connect('tweets_processed.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tesla_processed (
            username TEXT,
            followers REAL,
            tweet TEXT,
            tweet_clean TEXT,
            sentiment TEXT
        )
    """)
    conn.commit()
    return conn, c



def write_to_db(cursor, conn, tweet_data):
    print("Writing to DB:", tweet_data)

    # Insert data into SQLite database
    cursor.execute("""
        INSERT INTO tesla_processed (username, followers, tweet, tweet_clean, sentiment)
        VALUES (?, ?, ?, ?, ?)
    """, (tweet_data['username'], tweet_data['followers'], tweet_data['tweet'], tweet_data['tweet_clean'], tweet_data['sentiment']))
    conn.commit()

# Kafka consumer configuration
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'twitter-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Initialize Kafka consumer
consumer = Consumer(consumer_conf)

# Subscribe to the Kafka topic
topic = 'twitter2'
consumer.subscribe([topic])

# Initialize SQLite
conn, c = create_db()

print("Consuming messages from Kafka topic:", topic)

try:
    while True:
        msg = consumer.poll(1.0)  # Poll Kafka for messages

        if msg is None:
            print("No messages received yet")
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"End of partition reached {msg.topic()} [{msg.partition()}]")
            elif msg.error():
                raise KafkaError(msg.error())
            continue

        # Deserialize the Kafka message (assuming it's JSON)
        tweet_data = json.loads(msg.value().decode('utf-8'))

        print("Received message:", tweet_data)  # Log the message to the console

        # Process and save the tweet data
        write_to_db(c, conn, tweet_data)

except KeyboardInterrupt:
    print("Aborted by user")

finally:
    # Close consumer and database connection
    consumer.close()
    conn.close()
