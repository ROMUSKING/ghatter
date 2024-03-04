import keys
import google.generativeai as genai
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=keys.API_CHATGPT)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion.choices[0].message.content)
# Used to securely store your API key
genai.configure(api_key=keys.API_GEMINI)

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("what should i make as my first independent project from boot.dev?")
print(response.text)  # cold.
