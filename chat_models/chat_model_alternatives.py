from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

messages = [
    SystemMessage(content="Solve the following math problem?"),
    HumanMessage(content="What is 48 divided by 8?"),
]

#LangChain Open AI Chat Model
model = ChatOpenAI(model="gpt-4o-mini")

#Invoke the model with a message
result = model.invoke(messages)
print(f"Answer from OpenAI: {result.content}")


#LangChain Anthropic Chat Model
model = ChatAnthropic(model="claude-3-5-sonnet-20241022")

#Invoke the model with a message
result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")

#LangChain Google Gen AI Chat Model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

#Invoke the model with a message
result = model.invoke(messages)
print(f"Answer from Google: {result.content}")