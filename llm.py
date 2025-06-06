from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatGroq(model="llama-3.3-70b-versatile")

prompt_template = ChatPromptTemplate.from_messages(
  [
    ("system", "{system_message}"),
    MessagesPlaceholder("messages"),
  ]
)

chain = prompt_template | llm
