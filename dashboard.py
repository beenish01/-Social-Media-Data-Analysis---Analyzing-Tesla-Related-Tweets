# import streamlit as st
# import sqlite3
# import pandas as pd
# import matplotlib.pyplot as plt
# import random

# # Connect to SQLite database
# def get_connection():
#     return sqlite3.connect('tweets_processed.db')

# # Fetch all data from the database
# def fetch_data():
#     conn = get_connection()
#     query = "SELECT * FROM tesla_processed;"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# # Insert new data into the database
# def insert_data(username, tweet, sentiment, followers):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO tesla_processed (username, tweet, sentiment, followers) VALUES (?, ?, ?, ?)",
#         (username, tweet, sentiment, followers)
#     )
#     conn.commit()
#     conn.close()

# # Start Streamlit app
# st.title("Tesla Tweets Sentiment Analysis Dashboard")

# # Fetch data and display it
# df = fetch_data()
# st.subheader("Raw Data")
# st.dataframe(df)

# # Analyze sentiment distribution
# st.subheader("Sentiment Distribution")
# sentiment_counts = df['sentiment'].value_counts()
# st.bar_chart(sentiment_counts)

# # Display most followed user
# st.subheader("Most Followed User")
# most_followed = df.loc[df['followers'].idxmax()]
# st.write(f"Username: {most_followed['username']}")
# st.write(f"Followers: {most_followed['followers']}")
# st.write(f"Tweet: {most_followed['tweet']}")

# # Filter tweets by sentiment
# st.subheader("Filter Tweets by Sentiment")
# sentiment_filter = st.selectbox("Select Sentiment", df['sentiment'].unique())
# filtered_tweets = df[df['sentiment'] == sentiment_filter]
# st.write(filtered_tweets[['username', 'tweet', 'sentiment']])

# # Add a new tweet
# st.subheader("Add New Tweet")
# username = st.text_input("Username")
# tweet = st.text_area("Tweet")
# followers = st.number_input("Followers", min_value=0)

# if st.button("Add Data"):
#     if username and tweet:
#         # Assign a random sentiment from the existing sentiments in the database
#         random_sentiment = random.choice(df['sentiment'].unique())
#         insert_data(username, tweet, random_sentiment, followers)
#         st.success("Tweet added successfully!")
#         st.experimental_rerun()  # Refresh the dashboard
#     else:
#         st.error("All fields are required!")

# # Additional insights
# st.subheader("Sentiment Pie Chart")
# fig, ax = plt.subplots()
# sentiment_counts.plot.pie(autopct='%1.1f%%', ax=ax)
# ax.set_ylabel('')
# st.pyplot(fig)

# st.subheader("Followers Analysis")
# st.write(f"Average followers per user: {df['followers'].mean():.2f}")
# st.write(f"Total followers: {df['followers'].sum()}")
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import random

# Connect to SQLite database
def get_connection():
    return sqlite3.connect('tweets_processed.db')

# Fetch all data from the database
def fetch_data():
    conn = get_connection()
    query = "SELECT * FROM tesla_processed;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Insert new data into the database
def insert_data(username, tweet, sentiment, followers):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tesla_processed (username, tweet, sentiment, followers) VALUES (?, ?, ?, ?)",
        (username, tweet, sentiment, followers)
    )
    conn.commit()
    conn.close()

# Search for data by username
def search_by_user(username):
    conn = get_connection()
    query = "SELECT * FROM tesla_processed WHERE username = ?;"
    df = pd.read_sql(query, conn, params=(username,))
    conn.close()
    return df

# Search for data by tweet content
def search_by_tweet(tweet_content):
    conn = get_connection()
    query = "SELECT * FROM tesla_processed WHERE tweet LIKE ?;"
    df = pd.read_sql(query, conn, params=(f"%{tweet_content}%",))
    conn.close()
    return df

# Start Streamlit app
st.title("Tesla Tweets Sentiment Analysis Dashboard")

# Fetch data and display it
df = fetch_data()
st.subheader("Raw Data")
st.dataframe(df)

# Analyze sentiment distribution
st.subheader("Sentiment Distribution")
sentiment_counts = df['sentiment'].value_counts()
st.bar_chart(sentiment_counts)

# Display most followed user
st.subheader("Most Followed User")
most_followed = df.loc[df['followers'].idxmax()]
st.write(f"Username: {most_followed['username']}")
st.write(f"Followers: {most_followed['followers']}")
st.write(f"Tweet: {most_followed['tweet']}")

# Filter tweets by sentiment
st.subheader("Filter Tweets by Sentiment")
sentiment_filter = st.selectbox("Select Sentiment", df['sentiment'].unique())
filtered_tweets = df[df['sentiment'] == sentiment_filter]
st.write(filtered_tweets[['username', 'tweet', 'sentiment']])

# Add a new tweet
st.subheader("Add New Tweet")
username = st.text_input("Username")
tweet = st.text_area("Tweet")
followers = st.number_input("Followers", min_value=0)

if st.button("Add Data"):
    if username and tweet:
        # Assign a random sentiment from the existing sentiments in the database
        random_sentiment = random.choice(df['sentiment'].unique())
        insert_data(username, tweet, random_sentiment, followers)
        st.success("Tweet added successfully!")
        st.experimental_rerun()  # Refresh the dashboard
    else:
        st.error("All fields are required!")

# Search for a specific user
st.subheader("Search for a Specific User")
search_username = st.text_input("Enter username to search")
if st.button("Search User"):
    user_data = search_by_user(search_username)
    if not user_data.empty:
        st.write(f"Data for user: {search_username}")
        st.dataframe(user_data)
        st.write(f"Most used sentiment by {search_username}: {user_data['sentiment'].mode()[0]}")
    else:
        st.write("No data found for this user.")

# Search for a specific tweet
st.subheader("Search for a Specific Tweet")
search_tweet = st.text_input("Enter tweet content to search")
if st.button("Search Tweet"):
    tweet_data = search_by_tweet(search_tweet)
    if not tweet_data.empty:
        st.write("Matching tweets:")
        st.dataframe(tweet_data)
    else:
        st.write("No matching tweets found.")

# Additional insights
st.subheader("Sentiment Pie Chart")
fig, ax = plt.subplots()
sentiment_counts.plot.pie(autopct='%1.1f%%', ax=ax)
ax.set_ylabel('')
st.pyplot(fig)

st.subheader("Followers Analysis")
st.write(f"Average followers per user: {df['followers'].mean():.2f}")
st.write(f"Total followers: {df['followers'].sum()}")
