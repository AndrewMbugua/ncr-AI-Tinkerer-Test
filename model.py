
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
prompt = ("Extract all emails signature information from the following text and then output it as a JSON"
          "Jenny Doe",
          "Senior Marketing Consultant"
          "e: jkeo@yesware.com",
          "p: 123-5676-4443",
          "w: www.yesware.com",
          "a: 75, Keen St. Boston MA334"
          )


result = llm.invoke(prompt)

print(result)
