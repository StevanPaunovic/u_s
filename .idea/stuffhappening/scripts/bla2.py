import os
import json
from openai import OpenAI

api_key = os.environ.get("API_KEY")

client = OpenAI(api_key=api_key)

# Sample conversation data
conversation_data = {
    "user_messages": [
        {"role": "user", "content": "You're a talkative person on a social platform. Your hobbies are baking, partying, art, and computer science. Your name is Max."},
        {"role": "user", "content": "You're a talkative person on a social platform. Your hobbies are cooking, going to bars, fitness, and politics. Your name is Ben."},
    ],
    "assistant_messages": [
        {"role": "assistant", "content": "You're an evaluator. Evaluate the depth of the conversation. Give it a out of 10 ranking. Give it back like this <<Depth-Score: {NUMBER}>>"},
        {"role": "assistant", "content": "You also echo the full conversation of the users in text"},
    ],
}

# Create a JSON representation of the conversation data
json_data = json.dumps(conversation_data, indent=2)

# Specify the file path
file_path = "system_response.json"

# Write the JSON content to the file
with open(file_path, "w") as file:
    file.write(json_data)

print(f"System response saved to {file_path}")

# Print the JSON content
print(json_data)