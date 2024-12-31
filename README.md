# -Social-Media-Data-Analysis---Analyzing-Tesla-Related-Tweets



This code comprises a Kafka producer and consumer system integrated with SQLite databases to handle streaming data.

Kafka_producer:
The producer (twitter_producer.py) fetches records from an SQLite database (tweets.db) containing a table named tesla. Each record is serialized into JSON format and sent as messages to a Kafka topic (twitter2) using the Confluent Kafka producer. A delivery report callback ensures message delivery status is logged. The producer facilitates transferring database content to a distributed messaging system like Kafka for real-time processing.

Kafka_consumer:
The consumer (twitter_consumer.py) subscribes to the Kafka topic and processes the incoming messages. It deserializes the JSON messages, logs them to the console, and saves them into a separate SQLite database (tweets_processed.db) under the tesla_processed table. The database schema includes fields like username, followers, tweet, tweet_clean, and sentiment. The code uses a while loop to continuously poll Kafka for new messages, processes them, and stores the results in the database. This setup demonstrates a typical pipeline for real-time data ingestion, processing, and storage using Kafka and SQLite.

SQLite Database:
The processed tweets are inserted into the tweets_processed table using the consumer. This insertion happens almost immediately after the consumer processes the data, showcasing near real-time behavior. the consumer will generate tweets_processed.db

UI Updates:
The UI displays the data as soon as it is inserted into the database, further emphasizing a near real-time user experience. streamlit is used for this : streamlit run dashboard.py

Problem Statement and BDA Process



![{F02882B0-44BD-4F4D-9C3A-0E813F2EB0D2}](https://github.com/user-attachments/assets/75c49a2d-b5d6-4162-b10b-23d99dd82cf6)

SQlite database
![{CAE3520A-3B05-40A9-9758-D32DE03C5F6A}](https://github.com/user-attachments/assets/b99f9bd7-090e-44f2-98ae-3b2576e7dcfa)



