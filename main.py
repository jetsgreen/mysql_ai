from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
  db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
  return SQLDatabase.from_uri(db_uri)

st.set_page_config(page_title="Chat with MySQL", page_icon="💾")

st.title("Chat with MySQL 🤖")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a simple chat application using MySQL.  Connect to the database and start chatting.")

    st.text_input("Host", value="localhost", key="Host")
    st.text_input("Port", value="3307", key="Port")
    st.text_input("User", value="flex21", key="User")
    st.text_input("Password", type="password", value="Lalitha513!", key="Password")
    st.text_input("Database", value="chinook", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
            )
            st.session_state.db = db
            st.success("Connected to database!")
          

st.chat_input("Type a message")