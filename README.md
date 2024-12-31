# -Social-Media-Data-Analysis---Analyzing-Tesla-Related-Tweets


Kafka Producer and Consumer:
The Kafka producer sends tweets to a Kafka topic, and the consumer processes them in real-time. This indicates streaming data capabilities, which is a characteristic of real-time systems.

SQLite Database:
The processed tweets are inserted into the tweets_processed table using the consumer. This insertion happens almost immediately after the consumer processes the data, showcasing near real-time behavior.

UI Updates:
The UI displays the data as soon as it is inserted into the database, further emphasizing a near real-time user experience.
