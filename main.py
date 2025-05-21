# lines that start with a # are comments

# These are imported modules. They add functionality beyond what vanilla python can do

from ollama import * # This module helps simplify ollama api access
                     # that command lets this file access all the functions that the ollama module has

                     
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
