import streamlit as st
import openai

# Initialize the OpenAI API with your API key
openai.api_key = "your-openai-api-key"

# Function to generate a response from ChatGPT using the updated API
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the appropriate model, such as "gpt-3.5-turbo" or "gpt-4"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
    )
    message = response['choices'][0]['message']['content'].strip()
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
        