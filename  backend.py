import requests
import re

DEEPSEEK_API_KEY = "sk-b5e9b03c33244f1ab5bc78e2ed9bc746"

def chat_with_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def clean_response(text):
    text = re.sub(r'[*#`>_\[\]\(\)]', '', text)  # remove markdown characters
    text = re.sub(r'\s{2,}', ' ', text)          # remove extra spaces
    return text.strip()

if __name__ == "__main__":
    print("🤖 MK Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("MK Chatbot: Goodbye!")
            break
        raw_response = chat_with_deepseek(user_input)
        cleaned = clean_response(raw_response)
        print("MK Chatbot:", cleaned)