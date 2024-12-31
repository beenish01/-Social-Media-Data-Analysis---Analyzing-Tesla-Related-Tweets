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


# Dashboard


![WhatsApp Image 2024-12-31 at 23 33 01_c1ecbf0b](https://github.com/user-attachments/assets/34e591bd-27e2-47d3-875b-495cdc9a47e3)

![WhatsApp Image 2024-12-31 at 23 33 49_6f483777](https://github.com/user-attachments/assets/3f973fe2-f2d9-4348-88e1-2e0b1dce74c9)

![WhatsApp Image 2024-12-31 at 23 34 48_7373c4c3](https://github.com/user-attachments/assets/fd6147b4-dff3-476c-b41c-7c2acc0d743b)

![WhatsApp Image 2024-12-31 at 23 35 21_2267fb0b](https://github.com/user-attachments/assets/a0b6b87c-d560-4253-87d3-5d647cb18cd0)

![WhatsApp Image 2024-12-31 at 23 35 31_4a939869](https://github.com/user-attachments/assets/7b9aeaef-a951-4730-bd35-097343444649)





