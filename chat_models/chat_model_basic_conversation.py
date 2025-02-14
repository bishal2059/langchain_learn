from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

load_dotenv()

#Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

#Message to send to the model
messages = [
    SystemMessage(content="Solve the following math problem?"),
    HumanMessage(content="What is 48 divided by 8?"),
]

#Invoke the model with a message
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")

#AIMessage:
messages = [
    SystemMessage(content="Solve the following math problem?"),
    HumanMessage(content="What is 48 divided by 8?"),
    AIMessage(content="48 divided by 8 is 6."),
    HumanMessage(content="What is 10 times 5?"),
]

#Invoke the model with a message
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
