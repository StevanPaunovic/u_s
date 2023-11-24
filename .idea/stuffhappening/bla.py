import os
from openai import OpenAI

# Replace 'your-api-key' with the actual name of your environment variable
api_key = os.environ.get("API_KEY")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You give back the conversation between the users"},
        {"role": "user", "content": "You're a talkative person on a dating platform. Your hobbies are baking, partying, art, and computer science. Your name is Max."},
        {"role": "user", "content": "You're a talkative person on a dating platform. Your hobbies are cooking, going to bars, fitness, and politics. Your name is Ben."}
    ]
)

print(completion.choices[0].message)