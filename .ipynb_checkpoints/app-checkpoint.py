import streamlit as st
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
from PIL import Image
import pandas as pd
import base64

# Set page configuration
st.set_page_config(page_title="2024 Olympics Sentiment Analyzer", layout="wide")

def add_bg_image(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png" if image_file.name.endswith("png") else "jpg"};base64,{encoded_string});
        background-size: 100%; /* Adjust the percentage to zoom out or in */
        background-position: top;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Call the function with your image file
add_bg_image("images/background.jpg")

# Load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def display_sentiment_emoticon(sentiment):
    emoticons = {
        "positive": "😄",  # Smiley face for positive sentiments
        "neutral": "😐",   # Neutral face for neutral sentiments
        "negative": "😞"   # Sad face for negative sentiments
    } 
    
    colors = {
        "positive": "blue",
        "neutral": "yellow",
        "negative": "red"
    }
    
    emoticon = emoticons.get(sentiment, "❓")  # Retrieves emoticon based on the sentiment, returns question mark if sentiment is unknown
    color = colors.get(sentiment, "black") # Retrieves a color associated with the sentiment, if sentiment not found default color is "black"

    
    # Display the sentiment emoticon and sentiment text centered on the screen
    # The emoticon is displayed with a large font size and color based on the sentiment
    # The sentiment text is shown below the emoticon, centered and styled with the corresponding color based on sentiment
    st.markdown(f"""
    <div style="display: flex; 
    justify-content: center; 
    align-items: center; 
    height: 200px;">
        <span style="font-size: 100px; color: {color};">{emoticon}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; 
    font-size: 24px; 
    color: {color};">
        Sentiment: {sentiment.capitalize()}
    </div>
    """, unsafe_allow_html=True)



# Olympic ring colors
ring_colors = ["blue", "yellow", "gray", "green", "red"]

# Create tabs
tabs = st.tabs(["🏠 Home", "📊 Analyzer", "👥 The Team", "ℹ️ Info", "💬 Feedback"])

# Apply Olympic ring colors to tabs and style them as rings
st.markdown(f"""
<style>
.stTabs {{
    display: flex;
    justify-content: space-evenly;
}}
    
.stTabs [data-baseweb="tab"] {{
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 5px solid transparent;
    line-height: 60px;
    text-align: center;
    color: auto;
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

.stTabs [data-baseweb="tab"]:nth-child(5) {{
    border-color: {ring_colors[4]};
}}

.stTabs [data-baseweb="tab"]:hover {{
    transform: scale(1.1);
}}

</style>
""", unsafe_allow_html=True)

# Home tab
with tabs[0]:
    st.title("Welcome to the 2024 Paris Olympics Sentiment Analyzer")
    
    # Lottie Olympic-themed animation
    lottie_url = "https://lottie.host/fe78a580-e21b-4613-b5d6-cc64b1a934b7/vDApSHkH81.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)
    st.write("Analyze sentiment of the 2024 Paris Olympics with our advanced tool.")

# Sentiment analyzer tab
with tabs[1]:
    st.title("Olympic Sentiment Analyzer")
    
    # Load and display team Lottie animation
    lottie_url = "https://lottie.host/83213d4d-0fde-4804-86d7-03b17919cf3b/nYDHta6PFS.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)
    
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
            df["sentiment"] = df["text"].apply(lambda x: dummy_sentiment_analysis(x))
            df["emoticon"] = df["sentiment"].apply(get_sentiment_emoticon)  # Add emoticon column 
            st.write(df) # Display the DataFrame
            
            # Set sentiment to the predominant sentiment in the DataFrame when needed
            sentiment = df["sentiment"].mode()[0] if not df["sentiment"].empty else "neutral"
        else:
            content = uploaded_file.getvalue().decode("utf-8")
            sentiment = dummy_sentiment_analysis(content)
    else:
        user_input = st.text_area("..or enter text to analyze:")
        if st.button("Analyze Sentiment"):
            sentiment = dummy_sentiment_analysis(user_input) if user_input else "neutral"
            
    # Display sentiment emoticon
    display_sentiment_emoticon(sentiment)

# Team tab
with tabs[2]:
    st.title("The Data Sentinels")
    
    # Load and display team animation
    lottie_url = "https://lottie.host/18039274-4e01-4558-845e-a1d1d3b950eb/cKT9Btma01.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)

    # Add link to Font Awesome CSS file to retrieve social media icons
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
    
    # Team members info
    team_members = [
        {
            "name": "Ivy Atieng",
            "title": "Scrum Master",
            "bio": "Ivy is an experienced data scientist with a focus on natural language processing and sentiment analysis. She is our data pipeline expert and brings valuable insights to the team.",
            "image": "the_team/ivy.jpg",
            "github": "Atieng",
            "email": "atiengivylisa@gmail.com",
            "linkedin": "ivy-atieng/"
        },
        {
            "name": "Titus Kaluma",
            "title": "Project Manager",
            "bio": "Titus coordinates the team's efforts and ensures that we meet our project milestones. His background in both data science and project management keeps us on track and aligned with our goals.",
            "image": "the_team/titus.jpg",
            "github": "Kaluma-67",
            "email": "mwirigikaluma@gmail.com",
            "linkedin": "titus-mwirigi-62952972/"
        },
        {
            "name": "Elizabeth Masai",
            "title": "Visualization Specialist",
            "bio": "Elizabeth excels at creating insightful and interactive data visualizations. Her skills are essential for presenting our findings in a clear and impactful manner.",
            "image": "the_team/elizabeth.jpg",
            "github": "ElizabethMasai",
            "email": "elizabethchemtaim@gmail.com",
            "linkedin": "elizabeth-masai-6aab8118a"
        },
        {
            "name": "Sheila Mulwa",
            "title": "Presentation Expert",
            "bio": "Sheila brings a unique blend of analytical thinking and creative flair to our team by creating compelling visual narratives and engaging presentations that make our findings accessible to both technical and non-technical audiences.",
            "image": "the_team/sheila.jpg",
            "github": "Sheila-Mulwa",
            "email": "sheila.n.mulwa@gmail.com",
            "linkedin": "sheila-mulwa?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
        },
        {
            "name": "Evaclaire Munyika",
            "title": "Deployment Specialist",
            "bio": "Claire is our go-to expert for turning our sentiment analysis models into robust, scalable applications. Her knowledge of serverless computing allows us to deploy our sentiment analysis tools in a cost-effective and highly available manner.",
            "image": "the_team/claire.jpg",
            "github": "Eva-Claire",
            "email": "evamunyika@gmail.com",
            "linkedin": "evaclaire-munyika-991295114"
        }
    ]

    # Loop through each team member and display info and image, if image not found, display placeholder image
    for member in team_members:
        col1, col2 = st.columns([1, 3])
        
        with col1:
            try:
                image = Image.open(member["image"])
                st.image(image, width=150)
            except FileNotFoundError:
                st.image("https://via.placeholder.com/200", width=200)
                

        # Define CSS styles for the team member section:
        # - The "team-member" class creates a light gray bubble with padding, rounded corners, a slight border and a shadow for depth
        # - The "member-name" class styles the team member's name with bold font, a larger font size and black color
        # - The "member-title" class styles the team member's title with blue color, italic font style and a smaller font size than member name
        # - The "member-bio" class adds space below the bio text and styles it with black color
        # - The "member-contact" class adds styling for the contact icons including color, margin and hover effects
        # Display the team member's name, title, bio and contact links within a styled div element
        with col2:
            st.markdown(f"""
            <style>
            .team-member {{
                background-color: #f0f0f0; 
                padding: 20px;
                border-radius: 15px; 
                border: 1px solid #ddd; 
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); 
                margin-bottom: 20px; 
            }}
            .member-name {{
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 5px;
                color: black;
            }}
            .member-title {{
                font-size: 16px;
                color: blue;
                margin-bottom: 10px;
                font-style: italic; /* Italicize the title */
            }}
            .member-bio {{
                margin-bottom: 10px;
                color: black;
            }}
            .member-contact a {{
                margin-right: 10px;
                color: #007bff; /* Color for the icons */
                text-decoration: none;
            }}
            .member-contact a:hover {{
                color: #0056b3; /* Darker color on hover */
            }}
            </style>
            <div class="team-member">
                <div class="member-name">{member['name']}</div>
                <div class="member-title">{member['title']}</div>
                <div class="member-bio">{member['bio']}</div>
                <div class="member-contact">
                    <a href="https://github.com/{member['github']}" target="_blank">
                        <i class="fab fa-github"></i>
                    </a>
                    <a href="mailto:{member['email']}">
                        <i class="far fa-envelope"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/{member['linkedin']}" target="_blank">
                        <i class="fab fa-linkedin"></i>
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
# About tab
with tabs[3]:
    st.title("About The App")
    
    # Load and display torch bearer animation
    lottie_url = "https://lottie.host/93047e01-af1c-425a-89f5-c4d49abc3aaa/LVMzN5PPXM.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)
    
    st.write("""
    The Olympic Sentiment Analyzer is a powerful tool designed to analyze public sentiment surrounding the 2024 Olympic Games. 
    The application uses advanced natural language processing and machine learning techniques to process large volumes of 
    text data from Twitter, news articles and user-submitted content.
    It was created to provide real-time insights into public opinion and reactions to Olympic events, athletes and related topics.
    """)

    st.subheader("How it works")
    st.write("""
    - Tweets are collected using a web-scraping tool known as Octoparse.
    - Each tweet is analyzed for sentiment using natural language processing.
    - Results are visualized and updated continuously.
    """)
    
    st.subheader("Technologies used")
    st.write("""
    - Python
    - Streamlit
    - NLTK for sentiment analysis
    - Matplotlib and Seaborn for visualizations
    """)

    st.write("""This project is developed by a team of data scientists and machine learning experts passionate about sports and data analysis. 
    Our goal is to provide valuable insights into public opinion and sentiment trends throughout the 2024 Olympic Games.
    """)


# Feedback tab
with tabs[4]:
    st.title("We Value Your Feedback")
    
    # Feedback form
    st.subheader("Share Your Thoughts")
    feedback = st.text_area("What do you think about our Olympic Sentiment Analyzer?")
    
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please enter your feedback before submitting.")

# Footer 
st.markdown("---")
st.markdown("© 2024 Olympic Sentiment Analyzer. All rights reserved.")
