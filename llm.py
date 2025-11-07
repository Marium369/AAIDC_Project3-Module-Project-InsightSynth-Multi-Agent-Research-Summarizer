import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


GROQ_API_KEY= os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found! Make sure it is set in your.env file.")

client=Groq(api_key=GROQ_API_KEY)

def run_llm(prompt: str, max_tokens: int=300):

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content
print("Loaded Key: ", GROQ_API_KEY)
if __name__ == "__main__":                
    reply = run_llm("Hello, how are you?")
    print(reply) 