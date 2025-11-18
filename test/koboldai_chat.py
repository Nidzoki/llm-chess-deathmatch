from ai4free import KOBOLDAI

koboldai = KOBOLDAI()

while True:
    prompt = input("You: ")
    response = koboldai.chat(prompt)
    print(f"KoboldAI: {response}")