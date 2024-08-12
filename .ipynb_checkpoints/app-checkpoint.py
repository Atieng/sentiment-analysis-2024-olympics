import streamlit as st
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import pandas as pd


# Load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Create Olympic torch based on sentiment
def create_torch(sentiment):
    # Define colors based on sentiment
    colors = {
        "positive": "rgb(0, 0, 255)",   # Blue for positive
        "neutral": "rgb(255, 255, 0)",  # Yellow for neutral
        "negative": "rgb(255, 0, 0)"    # Red for negative
    }

    # Create a triangular shape resembling an Olympic torch
    fig = go.Figure(data=[go.Scatter(
        x=[0, 1, 2],                    
        y=[0, 1.5, 0],                  
        fill="toself",                  
        fillcolor=colors[sentiment],    
        line=dict(color="rgba(0,0,0,0)")
    )])

    # Update layout to hide axes and frame the torch
    fig.update_layout(
        showlegend=False,               
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        margin=dict(l=0, r=0, t=0, b=0),
        height=300,                    
        width=200                       
    )
    
    return fig

# Set page config
st.set_page_config(page_title="2024 Olympics Sentiment Analyzer", layout="wide")

# Olympic ring colors
ring_colors = ["blue", "yellow", "green", "red"]

# Create tabs
tabs = st.tabs(["🏠 Home", "📊 Sentiment Analyzer", "👥 The Data Sentinels", "ℹ️ Info"])

# Apply Olympic ring colors to tabs and style them as rings
st.markdown(f"""
<style>
.stTabs {{
    display: flex;
    justify-content: space-evenly;
}}

.stTabs [data-baseweb="tab"] {{
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 5px solid transparent;
    line-height: 60px;
    text-align: center;
    color: white;
    font-weight: bold;
    transition: transform 0.3s ease;
}}

.stTabs [data-baseweb="tab"]:nth-child(1) {{
    border-color: {ring_colors[0]};
}}

.stTabs [data-baseweb="tab"]:nth-child(2) {{
    border-color: {ring_colors[1]};
}}

.stTabs [data-baseweb="tab"]:nth-child(3) {{
    border-color: {ring_colors[2]};
}}

.stTabs [data-baseweb="tab"]:nth-child(4) {{
    border-color: {ring_colors[3]};
}}

.stTabs [data-baseweb="tab"]:hover {{
    transform: scale(1.1);
}}

</style>
""", unsafe_allow_html=True)

# Content for each tab
with tabs[0]:
    st.title("Welcome to the 2024 Paris Olympics Sentiment Analyzer")
    
    # Lottie Olympic-themed animation
    lottie_url = "https://lottie.host/fe78a580-e21b-4613-b5d6-cc64b1a934b7/vDApSHkH81.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=400)
    st.write("Analyze the sentiment of Olympic-related content with our advanced tool.")

with tabs[1]:
    st.title("Olympic Sentiment Analyzer")
    
    # Load and display team Lottie animation
    lottie_url = "https://lottie.host/83213d4d-0fde-4804-86d7-03b17919cf3b/nYDHta6PFS.json"  
    lottie_json = load_lottieurl(lottie_url)
    
    st_lottie(lottie_json, height=300)
    # Initialize sentiment to a default value
    sentiment = "neutral"
    
    # File upload
    uploaded_file = st.file_uploader("Upload your data (CSV or TXT)", type=["csv", "txt"])
    
    def dummy_sentiment_analysis(text):
        # Basic sentiment keywords
        positive_keywords = ["happy", "good", "great", "excellent", "fantastic", "amazing"]
        negative_keywords = ["bad", "terrible", "poor", "awful", "horrible", "sad"]
    
        # Convert text to lowercase for keyword matching
        text_lower = text.lower()
    
        # Check for positive and negative keywords
        positive_count = sum(word in text_lower for word in positive_keywords)
        negative_count = sum(word in text_lower for word in negative_keywords)
    
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
            
    if uploaded_file is not None:
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            df['sentiment'] = df['text'].apply(lambda x: dummy_sentiment_analysis(x))
            st.write(df)
            # Set sentiment to the predominant sentiment in the DataFrame, if needed
            sentiment = df['sentiment'].mode()[0] if not df['sentiment'].empty else "neutral"
        else:
            content = uploaded_file.getvalue().decode("utf-8")
            sentiment = dummy_sentiment_analysis(content)
            st.write(f"Sentiment: {sentiment}")
    else:
        user_input = st.text_area("Or enter text to analyze:")
        if st.button("Analyze Sentiment"):
            sentiment = dummy_sentiment_analysis(user_input) if user_input else "neutral"
            st.write(f"Sentiment: {sentiment}")

    # Display Olympic torch
    st.plotly_chart(create_torch(sentiment), use_container_width=True)

with tabs[2]:
    st.title("The Data Sentinels")
    # Load and display team Lottie animation
    lottie_url = "https://lottie.host/18039274-4e01-4558-845e-a1d1d3b950eb/cKT9Btma01.json"  
    lottie_json = load_lottieurl(lottie_url)
    
    st_lottie(lottie_json, height=300)

    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .social-icon {
            font-size: 24px;
            margin-right: 10px;
            color: #1a1a1a;
            text-decoration: none;
        }
        .social-icon:hover {
            opacity: 0.7;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Team members
    team_members = [
        {
            "name": "Ivy Atieng",
            "title": "Scrum Master",
            "bio": "Ivy is an experienced data scientist with a focus on natural language processing and sentiment analysis. She is our data pipeline expert and brings valuable insights to the team.",
            "image": "the_team/ivy.jpg",
            "github": "Atieng",
            "email": "atiengivylisa@gmail.com",
            "linkedin": ""
        },
        {
            "name": "Titus Kaluma",
            "title": "Project Manager",
            "bio": "Titus coordinates the team's efforts and ensures that we meet our project milestones. His background in both data science and project management keeps us on track and aligned with our goals.",
            "image": "the_team/titus.jpg",
            "github": "Kaluma-67",
            "email": "mwirigikaluma@gmail.com",
            "linkedin": ""
        },
        {
            "name": "Elizabeth Masai",
            "title": "Visualization Specialist",
            "bio": "Elizabeth excels at creating insightful and interactive data visualizations. Her skills are essential for presenting our findings in a clear and impactful manner.",
            "image": "the_team/elizabeth.jpg",
            "github": "ElizabethMasai",
            "email": "elizabethchemtaim@gmail.com",
            "linkedin": ""
        },
        {
            "name": "Sheila Mulwa",
            "title": "Presentation Expert",
            "bio": "Sheila brings a unique blend of analytical thinking and creative flair to our team by creating compelling visual narratives and engaging presentations that make our findings accessible to both technical and non-technical audiences.",
            "image": "the_team/sheila.jpg",
            "github": "Sheila-Mulwa",
            "email": "sheila.n.mulwa@gmail.com",
            "linkedin": ""
        },
        {
            "name": "Evaclaire Munyika",
            "title": "Deployment Specialist",
            "bio": "Claire is our go-to expert for turning our sentiment analysis models into robust, scalable applications. Her knowledge of serverless computing allows us to deploy our sentiment analysis tools in a cost-effective and highly available manner.",
            "image": "the_team/claire.jpg",
            "github": "Eva-Claire",
            "email": "evamunyika@gmail.com",
            "linkedin": "www.linkedin.com/in/evaclaire-munyika-991295114"
        }
    ]

    # Display team members with Olympic theme
    for member in team_members:
        col1, col2 = st.columns([1, 3])
        
        with col1:
            try:
                image = Image.open(member["image"])
                st.image(image, width=150)
            except FileNotFoundError:
                st.image("https://via.placeholder.com/200", width=200)
        
        with col2:
            st.markdown(f"""
            <div class="team-member">
                <div class="member-name">{member['name']}</div>
                <div class="member-title">{member['title']}</div>
                <div class="member-bio">{member['bio']}</div>
                <div class="member-contact">
                    <a href="https://github.com/{member['github']}" target="_blank" class="social-icon">
                        <i class="fab fa-github"></i>
                    </a>
                    <a href="mailto:{member['email']}" class="social-icon">
                        <i class="far fa-envelope"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/{member['linkedin']}" target="_blank" class="social-icon">
                        <i class="fab fa-linkedin"></i>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)



with tabs[3]:
    st.title("About the Olympic Sentiment Analyzer")
    # Load and display torch bearer Lottie animation
    lottie_url = "https://lottie.host/93047e01-af1c-425a-89f5-c4d49abc3aaa/LVMzN5PPXM.json"  
    lottie_json = load_lottieurl(lottie_url)
    
    st_lottie(lottie_json, height=300)
    st.write("""
    The Olympic Sentiment Analyzer is a powerful tool designed to analyze public sentiment surrounding the 2024 Olympic Games. 
    Our application uses advanced natural language processing and machine learning techniques to process large volumes of 
    text data from Twitter, news articles and user-submitted content.

    Key features:
    - Real-time sentiment analysis of 2024 Olympic-related content
    - Support for multiple data sources and formats
    - Interactive visualization of sentiment trends

    This project is developed by a team of data scientists and machine learning experts passionate about sports and data analysis. 
    Our goal is to provide valuable insights into public opinion and sentiment trends throughout the 2024 Olympic Games.
    """)

# Footer
st.markdown("---")
st.markdown("© 2024 Olympic Sentiment Analyzer. All rights reserved.")
