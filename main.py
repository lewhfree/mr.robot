# lines that start with a #hash are comments

# These are imported modules. They add functionality beyond what vanilla python can do

from ollama import chat,ChatResponse # This module helps simplify ollama api access

# This basically asks the chatbot "prompt" and prints it out. This is just placeholder, but it should work
response: ChatResponse = chat(
    model="codellama:latest",
    messages=[
        {
            "role": "user",
            "content": "How do i do a html comment",
        },
    ],
)

print(response["message"]["content"])
