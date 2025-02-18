from openai import OpenAI

# Set Key as env_var before running code
client = OpenAI()

conversation_history = [
    {"role": "system", "content": f"You are a highly sarcastic and witty AI. Respond to the following statement with a humorous and sarcastic remark"}
]

def generate_sarcastic_response(user_input):
    userQuery = { "role": "user", "content": user_input }
    conversation_history.append(userQuery)
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= conversation_history,
    temperature=0.7,
    )
    conversation_history.append({"role": "assistant", "content": response.choices[0].message.content})
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = generate_sarcastic_response(user_input)
        print(f"\nSarcastic AI: {response}\n")