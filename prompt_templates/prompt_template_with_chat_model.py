from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

#Create OpenAI chat model
model = ChatOpenAI(model="gpt-4o-mini")

#Part 1: Prompt with single variable
template = "Tell me a joke about {topic}."
prompt_template = ChatPromptTemplate.from_template(template)

print("-----Prompt Template with single placeholder-----")
prompt = prompt_template.invoke({"topic": "chickens"})
result = model.invoke(prompt)
print(result.content)

#Part 2: Prompt with multiple variables
template_multiple = """ You are a helpful assistant.
Human: Tell me a {adjective} story about a {animal}.
AI:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "cat"})

print("-----Prompt Template with multiple placeholder-----")
result = model.invoke(prompt)
print(result.content)

#Part 3: Prompt with System and Human messages
messages =[
    ("system","You are a comedian who tells jokes about {topic}"),
    ("human","Tell me {joke_count} jokes.")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "car", "joke_count": "3"})
print("-----Prompt Template with System and Human messages-----")
result = model.invoke(prompt)
print(result.content)
