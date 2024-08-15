import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

# Function to generate a response using the latest API
def generate_response(prompt):
    response = openai.chat_completions.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

# Streamlit app layout
st.title("Olympics Chatbot")
st.write("Ask anything about the Olympics!")

# Input from the user
user_input = st.text_input("You:", placeholder="Ask me about the Olympics...")

# Button to submit the query
chatgpt_response = None
if st.button("Send"):
    if user_input:
        # Generate the response
        chatgpt_response = generate_response(user_input)
        
        # Display the response
        st.write(f"ChatGPT: {chatgpt_response}")

# Keep a history of the conversation (optional)
if "history" not in st.session_state:
    st.session_state.history = []

if user_input and chatgpt_response:
    st.session_state.history.append(f"You: {user_input}")
    st.session_state.history.append(f"ChatGPT: {chatgpt_response}")

# Display conversation history
if st.session_state.history:
    st.write("### Conversation History")
    for message in st.session_state.history:
        st.write(message)