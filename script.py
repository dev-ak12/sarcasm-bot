from openai import OpenAI

# Set Key as env_var before running code
client = OpenAI()

def generate_sarcastic_response(user_input):
    prompt = f"You are a highly sarcastic and witty AI. Respond to the following statement with a humorous and sarcastic remark"

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": prompt},
        {
            "role": "user",
            "content": user_input
        }
    ],
    temperature=0.7,

    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = generate_sarcastic_response(user_input)
        print(f"\nSarcastic AI:\n{response}\n")