
# -Social-Media-Data-Analysis---Analyzing-Tesla-Related-Tweets

## How to run the project 

Create a kafka topic, run the producer and consumer python scripts and then run dashboard.py to view dashboard.

 ## Set up
 This project was built using:
 Python 3,
 Kafka, 
 Spark SQL, 
 SQLite,
 Streamlit

 ## Implementation
 Obtaining twitter data.
 
 Creating a kafka producer that publishes messages to a topic.
 
 Creating a kafka consumer that consumes messages from the kafka topic.
 
 Processing content of the tweets and storing it to SQLite database.
 
 Use Spark SQL to query data from SQLite database and creating visualizations using Streamlit.

Zookeeper connection 
zookeeper connection using :zookeeper-server-start.bat ..\..\config\zookeeper.properties
![image](https://github.com/user-attachments/assets/496cea7a-1ada-4e77-be4b-d1834b5fb088)

Kafka Connection 
kafka connection using: kafka-server-start.bat ..\..\config\server.properties
![image](https://github.com/user-attachments/assets/8322c2a1-92e3-40ee-a3d5-7a57b542c316)

create topic:

![image](https://github.com/user-attachments/assets/2a2fedcb-a891-4200-9c62-c466e60908c9)


 
 
## Problem Statement and BDA Process



![{F02882B0-44BD-4F4D-9C3A-0E813F2EB0D2}](https://github.com/user-attachments/assets/75c49a2d-b5d6-4162-b10b-23d99dd82cf6)








This code comprises a Kafka producer and consumer system integrated with SQLite databases to handle streaming data.

Kafka_producer:
The producer (twitter_producer.py) fetches records from an SQLite database (tweets.db) containing a table named tesla. Each record is serialized into JSON format and sent as messages to a Kafka topic (twitter2) using the Confluent Kafka producer. A delivery report callback ensures message delivery status is logged. The producer facilitates transferring database content to a distributed messaging system like Kafka for real-time processing.

![image](https://github.com/user-attachments/assets/b9d25003-aa91-4aca-972c-b6387187dee2)

Kafka_consumer:
The consumer (twitter_consumer.py) subscribes to the Kafka topic and processes the incoming messages. It deserializes the JSON messages, logs them to the console, and saves them into a separate SQLite database (tweets_processed.db) under the tesla_processed table. The database schema includes fields like username, followers, tweet, tweet_clean, and sentiment. The code uses a while loop to continuously poll Kafka for new messages, processes them, and stores the results in the database. This setup demonstrates a typical pipeline for real-time data ingestion, processing, and storage using Kafka and SQLite.

![image](https://github.com/user-attachments/assets/ebbf47b6-dc5c-4ea0-9cc1-56ce4bcba419)


SQLite Database:
The dataset involves Twitter data stored in tweets.db, containing user information, tweet text, and associated sentiments. The producer streams this raw data from tweets.db for real-time processing. The consumer processes the streamed data by cleaning the tweets, removing noise, and categorizing them into sentiments (positive, neutral, or negative). The processed data, including cleaned tweets and sentiment classifications, is then saved into tweets_processed.db.

SQlite database
![{CAE3520A-3B05-40A9-9758-D32DE03C5F6A}](https://github.com/user-attachments/assets/b99f9bd7-090e-44f2-98ae-3b2576e7dcfa)

UI Updates:
The UI displays the data as soon as it is inserted into the database, further emphasizing a near real-time user experience. streamlit is used for this : streamlit run dashboard.py

# Dashboard


![WhatsApp Image 2024-12-31 at 23 33 01_c1ecbf0b](https://github.com/user-attachments/assets/34e591bd-27e2-47d3-875b-495cdc9a47e3)

![WhatsApp Image 2024-12-31 at 23 33 49_6f483777](https://github.com/user-attachments/assets/3f973fe2-f2d9-4348-88e1-2e0b1dce74c9)

![{7E6A3BE9-C12C-45C2-A432-CC8F30745CEB}](https://github.com/user-attachments/assets/0758e0b7-097c-4641-9a48-439653cb2ec5)

![{14E34501-C8C3-4A82-8CEB-76B248671648}](https://github.com/user-attachments/assets/d4027267-76a0-4291-bbd9-522270977584)

![WhatsApp Image 2024-12-31 at 23 35 31_4a939869](https://github.com/user-attachments/assets/7b9aeaef-a951-4730-bd35-097343444649)





