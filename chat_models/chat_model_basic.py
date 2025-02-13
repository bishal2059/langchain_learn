from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

#Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

#Invoke the model with a message
result = model.invoke("What is 48 divided by 8?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)