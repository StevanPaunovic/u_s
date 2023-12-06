import os
from openai import OpenAI

api_key = os.environ.get("API_KEY")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "You're a talkative person on a social platform. Your hobbies are baking, partying, art, and computer science. Your name is Max."},
        {"role": "user", "content": "You're a talkative person on a social platform. Your hobbies are cooking, going to bars, fitness, and politics. Your name is Ben."},
        {"role": "system", "content": "You're an evaluator. Evaluate the depth of the conversation. Give it a out of 10 ranking. Give it back like this <<Depth-Score: {NUMBER}>>"},
        {"role": "system", "content": "You  give back the full conversation of the users in text"}
    ]
)


# Get the content from the "system" role
system_response = completion.choices[0].message.content

# Specify the file path
file_path = "system_response.txt"

# Write the content to the file
with open(file_path, "w") as file:
    file.write(system_response)

print(f"System response saved to {file_path}")

print(completion.choices[0].message.content)