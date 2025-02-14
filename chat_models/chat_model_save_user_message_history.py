import os
import firebase_admin
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_openai import ChatOpenAI
from firebase_admin import credentials

load_dotenv()

#Initialize Firebase Admin SDK
cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)

PROJECT_ID = "langchain-learn-d9f94"
SESSION_ID = "chat_session_1"
COLLECTION_NAME = "chat_history"

#Setup Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

#Initialize FirestoreChatMessageHistory
print("Initializing FirestoreChatMessageHistory...")
chat_history = FirestoreChatMessageHistory(client=client, session_id=SESSION_ID, collection=COLLECTION_NAME)

print("Chat history initialized.")
print("Current Chat History: ", chat_history.messages)

#Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

print("Start chatting with the AI... Type 'exit' to end the chat.")

#Chat loop:
while True:
    query = input("User: ")
    if query == "exit":
        break
    chat_history.add_user_message(query)
    
    #Get AI response using history
    result = model.invoke(chat_history.messages)
    response = result.content
    chat_history.add_ai_message(response)
    
    print("AI: ", response)