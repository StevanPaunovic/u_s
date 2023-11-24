import yaml
config = yaml.safe_load(open("config.yml"))


# You have to sign up and get an API key: https://platform.openai.com/signup
from openai import OpenAI

client = OpenAI(api_key='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')


# OpenAI API documentation: https://platform.openai.com/docs/introduction/overview
# "The main input is the messages parameter. Messages must be an array of message objects, where each
# object has a role (either "system", "user", or "assistant") and content. Conversations can be as short
# as one message or many back and forth turns."
client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Who won the world series in 2020?"},
  ])

# "The system message helps set the behavior of the assistant. For example, you can modify the
# personality of the assistant or provide specific instructions about how it should behave throughout
# the conversation. However note that the system message is optional and the model’s behavior without
# a system message is likely to be similar to using a generic message such as "You are a helpful assistant."
client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
      {"role": "system", "content": "You are a child, who doesn't know anything about baseball."},
      {"role": "user", "content": "Who won the world series in 2020?"},
  ])


client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
      {"role": "user", "content": "Who won the world series in 2020?"},
  ])

client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Who won the world series in 2020?"},
      {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
      {"role": "user", "content": "Where was it played?"}
  ])