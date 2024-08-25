import requests
import json

API_URL = "http://localhost:1234/v1/chat/completions"

def get_bot_response(message):
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "messages": [
            {"role": "user", "content": message}
        ],
        "model": "default"  # You may need to adjust this based on LM Studio's requirements
    }
    
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    print("Welcome to the LM Studio Chatbot!")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        bot_response = get_bot_response(user_input)
        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()