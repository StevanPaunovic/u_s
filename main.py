import openai

openai.api_key = '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'

num_rounds = 3

# Lese Systembeschreibung
with open('prompt_templates/system_desc.txt', "r") as f:
    system_prompt = f.read()
    system_prompt = system_prompt.replace("<Num_Rounds>", str(num_rounds))

# Lese Agent-Beschreibung
with open('prompt_templates/agent_desc.txt', "r") as f:
    agent_prompt = f.read()

# Lese Anweisungen für Feedback
with open('prompt_templates/instructions/feedback/v1.txt', "r") as f:
    instruction_feedback = f.read()

# Lese Anweisungen für Agent
with open('prompt_templates/instructions/agent/v3.txt', "r") as f:
    instruction_agent = f.read()

# Ersetze Platzhalter in den Prompts
feedback_prompt = agent_prompt.replace('<Role>', 'Sales Person').replace('<Instruction>', instruction_feedback)
agent_prompt = agent_prompt.replace('<Role>', 'Customer').replace('<Instruction>', instruction_agent)

# Füge Systeminformationen zu den Prompts hinzu
feedback_prompt = system_prompt + '\n' + feedback_prompt + '\n'
agent_prompt = system_prompt + '\n' + agent_prompt + '\n'

round = 1

while round <= num_rounds + 1:
    # Generiere Antwort für den Agent
    res_agent = openai.Completion.create(
        engine="text-davinci-002",
        prompt=agent_prompt + '\n ' + str(num_rounds - round),
        temperature=0.7,
        max_tokens=150
    )

    # Aktualisiere die Agenten-Prompts
    feedback_prompt = feedback_prompt + '\n\n' + res_agent.choices[0].text
    agent_prompt = agent_prompt + '\n\n' + res_agent.choices[0].text

    # Generiere Antwort für das Feedback
    res_feedback = openai.Completion.create(
        engine="text-davinci-002",
        prompt=feedback_prompt + '\n Only generate the next answer of the sales person. After generating the answer display the latest offer of sales person and the latest offer of customer: Last offer sales person: [amount]; Last offer customer: [amount]; Rounds to go before customer leaves: ' + str(num_rounds - round),
        temperature=0.7,
        max_tokens=150
    )

    # Aktualisiere die Feedback-Prompts
    feedback_prompt = feedback_prompt + '\n\n' + res_feedback.choices[0].text
    agent_prompt = agent_prompt + '\n\n' + res_feedback.choices[0].text

    round += 1

# https://arxiv.org/pdf/2305.10142.pdf
