# LM Studio Chatbot

This repository contains Python implementations of a chatbot using the LM Studio API. The chatbot is designed to interact with language models served by LM Studio, providing an easy-to-use interface for natural language conversations.

## Features

- Command-line interface for quick interactions
- Streamlit web application for a user-friendly GUI
- Customizable system messages to control the chatbot's behavior
- Integration with LM Studio's API for powerful language model capabilities

## Requirements

- Python 3.7+
- LM Studio server running locally
- Required Python packages:
  - `requests`
  - `streamlit` (for the web app version)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/lm-studio-chatbot.git
   cd lm-studio-chatbot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure LM Studio is running and serving a model on `localhost:1234`.

## Usage

### Command-line Interface

Run the command-line version of the chatbot:

```
python cli_chatbot.py
```

Follow the prompts to interact with the chatbot.

### Streamlit Web Application

Launch the Streamlit web app:

```
streamlit run streamlit_chatbot.py
```

The app will open in your default web browser, providing a modern interface for chatbot interactions.

## Customization

- Modify the `MODEL` variable in the scripts to use different LM Studio models.
- Adjust the `temperature` and other parameters in the API call to fine-tune the chatbot's responses.
- Customize the system message in the Streamlit app's sidebar to change the chatbot's behavior.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- This project uses the LM Studio API for language model inference.
- The web interface is built with Streamlit.

