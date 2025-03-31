# Buuh ChatBot

Buuh ChatBot is a conversational AI application built using Streamlit and [DeepSeek v3](https://openrouter.ai/deepseek/deepseek-chat:free) model API from [OPENROUTER](https://openrouter.ai/). The chatbot is designed to assist users with coding problems and provide career advice in a friendly and formal manner.

## Features

- Interactive chat interface for user input and bot responses.
- Utilizes OpenRouter's API to generate responses based on user queries.
- Displays a loading spinner while retrieving responses to enhance user experience.
- Caches conversation history for a seamless chat experience.

## Technologies Used

- [Streamlit](https://streamlit.io/) - A framework for building web applications in Python.
- [OpenRouter API](https://openrouter.ai/deepseek/deepseek-chat:free) - Provides access to powerful language models for generating text responses.
- [Python](https://www.python.org/) - The programming language used for development.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BuuhChatBot.git
   cd BuuhChatBot
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   # For macOS and Linux
   python -m venv venv
   source venv/bin/activate

   # For Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a file named `.streamlit/secrets.toml` in the root directory of your project.
   - Add your OpenRouter API key in the following format:
     ```toml
     [API_KEYS]
     OPENROUTER_API_KEY = "your_openai_api_key"
     ```


## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to shown adress on terminal to interact with the chatbot.

3. Type your questions or coding problems in the input box and press Enter. The chatbot will respond with helpful information and advice.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
