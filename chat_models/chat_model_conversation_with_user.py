from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

#Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")


#User's chat history 
chat_history = []

system_message = SystemMessage("You are a helpful AI assistant.")

chat_history.append(system_message)

#Chat loop:
while True:
    query = input("You: ")
    if query == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    #Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print("AI: ", response)

print("Chat ended.")
print("---------Full chat history-----------")
print(chat_history)
