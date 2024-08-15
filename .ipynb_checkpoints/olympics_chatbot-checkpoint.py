pip install streamlit openai

import streamlit as st
import openai

# Initialize the OpenAI API with your API key
openai.api_key = "your-openai-api-key"

# Function to generate a response from ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Streamlit app layout
st.title("Olympics Chatbot")
st.write("Ask anything about the Olympics!")

# Input from the user
user_input = st.text_input("You:", placeholder="Ask me about the Olympics...")

# Button to submit the query
if st.button("Send"):
    if user_input:
        # Generate the response
        chatgpt_response = generate_response(user_input)
        
        # Display the response
        st.write(f"ChatGPT: {chatgpt_response}")

# Keep a history of the conversation (optional)
if "history" not in st.session_state:
    st.session_state.history = []

if user_input:
    st.session_state.history.append(f"You: {user_input}")
    st.session_state.history.append(f"ChatGPT: {chatgpt_response}")

# Display conversation history
if st.session_state.history:
    st.write("### Conversation History")
    for i, message in enumerate(st.session_state.history):
        st.write(message)
