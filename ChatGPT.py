import openai

# Define sua chave API do OpenAI
openai.api_key = "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"

# Define o modelo que será usado pelo chatbot
model_engine = "text-davinci-002"

# Define a função que irá gerar as respostas do chatbot
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

# Loop principal do chatbot
while True:
    # Lê a entrada do usuário
    user_input = input("Você: ")

    # Gera uma resposta usando o GPT-3
    prompt = f"Eu: {user_input}\nUsuário:"
    response = generate_response(prompt)

    # Imprime a resposta do chatbot
    print("Chatbot:", response)