# lines that start with a #hash are comments

# These are imported modules. They add functionality beyond what vanilla python can do

import ollama # This module helps simplify ollama api access

# This basically asks the chatbot "prompt" and prints it out. This is just placeholder, but it should work
response: ChatResponse = chat(
    model="codellama:latest",
    messages=[
        {
            "role": "user",
            "content": "prompt",
        },
    ],
)

print(response["message"]["content"])
