import sqlite3
import json
from confluent_kafka import Producer
import socket

# Kafka settings
bootstrap_servers = 'localhost:9092'
data_encoding = 'utf-8'
twitter_kafka_topic_name = 'twitter2'

# Database settings
tweets_database_path = 'tweets.db'
tweets_table_name = 'tesla'

def delivery_report(err, msg):
    """Delivery report callback to confirm message delivery."""
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Kafka producer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': socket.gethostname()
}
producer = Producer(conf)

# Function to fetch data from SQLite database
def fetch_data_from_db(db_path, table_name):
    """Fetch all records from the specified SQLite database table."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Fetch column names
    column_names = [description[0] for description in cursor.description]
    conn.close()

    # Convert rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]
    return data

# Function to produce messages to Kafka
def produce_messages_to_kafka(data):
    """Send each record in the data list to the specified Kafka topic."""
    for record in data:
        try:
            # Convert the record to JSON and send to Kafka
            producer.produce(
                twitter_kafka_topic_name,
                value=json.dumps(record).encode(data_encoding),
                callback=delivery_report
            )
        except Exception as e:
            print(f"Failed to send message: {e}")
        producer.flush()

def main():
    """Main function to fetch data and produce messages to Kafka."""
    print("Fetching data from the database...")
    data = fetch_data_from_db(tweets_database_path, tweets_table_name)
    print(f"Fetched {len(data)} records.")
    
    print("Sending data to Kafka...")
    produce_messages_to_kafka(data)
    print("Data sent to Kafka successfully.")

if __name__ == "__main__":
    main()
