import requests
import json

API_URL = "http://localhost:1234/v1/chat/completions"
MODEL = "lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"

def get_bot_response(message, system_message="You are a helpful assistant."):
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": message}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    print("Welcome to the LM Studio Chatbot!")
    print("Type 'quit' to exit.")
    
    system_message = input("Enter a system message (or press Enter for default): ")
    if not system_message:
        system_message = "You are a helpful assistant."
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        bot_response = get_bot_response(user_input, system_message)
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()