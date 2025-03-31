import streamlit as st 
from openai import OpenAI

class BuuhBot:
    def __init__(self) -> None:
        st.set_page_config(
            page_title="Buuh ChatBot", 
            page_icon=":bear:",
            layout="centered",
        )
        self.session_state = st.session_state
        self.initCache()
        self.OPENROUTER_API_KEY = st.secrets.API_KEYS.OPENROUTER_API_KEY
        self.initUserMessage()
        
    def initCache(self):
        if "messages" not in self.session_state: 
            self.session_state.messages = []

        for message in self.session_state.messages: 
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
            
    
    def createCache(self,role:str, content:str):
        if role and content:
            self.session_state.messages.append({
                "role" : role, 
                "content": content
            })
    
    def initUserMessage(self):
        self.user_input = st.chat_input('Hello, How can I help you?')
        if self.user_input: 
            self.user_message_widget = st.chat_message('user')
            self.user_message_widget.markdown(self.user_input)
            self.createCache("user",self.user_input)
            self.initBotMessage(self.user_input)

    def initBotMessage(self, user_input):
        if user_input:
            self.bot_message_widget = st.chat_message("assistant")
            with self.bot_message_widget:
                # Create an empty placeholder for the loading message
                reply = st.empty()  
                
                # Use the spinner while getting the response
                with st.spinner("Getting response...",show_time=True):
                    response = self.getResponse(user_input)  # Get the response from the API
                
                    # Display the actual response
                reply.write_stream(response)  # Update the placeholder with the actual response
                self.createCache("assistant", response)  # Cache the response

    def getResponse(self,user_input):

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.OPENROUTER_API_KEY,
        )

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",
            messages=[
                {
                    "role": "system", 
                    "content": """You are Buuh, a helpful AI assistant. Your role is to assist users with coding problems and provide career advice. 

                    - **Guidelines**:
                      - Always respond in a formal and short manner.
                      - Provide clear and actionable solutions.
                      - Encourage users to ask follow-up questions for clarification.
                    """
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ], 
            stream = True
        )
        return response
    
if __name__ == "__main__":
    BuuhBot()