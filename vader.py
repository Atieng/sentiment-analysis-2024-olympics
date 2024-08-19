import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import base64
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import sklearn


# Set page configuration
st.set_page_config(page_title="2024 Olympics Sentiment Analyzer", layout="wide")

# Load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
st.markdown("---")

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
    
    lottie_url = "https://lottie.host/fe78a580-e21b-4613-b5d6-cc64b1a934b7/vDApSHkH81.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)
    st.write("Analyze sentiments of the 2024 Paris Olympics with our advanced tool.")

 
# Sentiment analyzer tab
with tabs[1]:
    st.title("Olympic Sentiment Analyzer")
    
    lottie_url = "https://lottie.host/83213d4d-0fde-4804-86d7-03b17919cf3b/nYDHta6PFS.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)

     # Load the pickled VADER model
    with open('Models/vader_model.pkl', 'rb') as vader_file:
        loaded_vader = pickle.load(vader_file)
        
    def clean_tweet(tweet):
        # Remove URLs
        tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
        # Remove user @ references
        tweet = re.sub(r'\@\w+', '', tweet)
        return tweet.strip()
    
    # Function to get sentiment emoticon
    def get_sentiment_emoticon(sentiment):
        emoticons = {
            "POSITIVE": "😄",
            "NEUTRAL": "😐",
            "NEGATIVE": "😞"
        }
        return emoticons.get(sentiment, "❓") 

    # Function to analyze sentiment using VADER
    def analyze_sentiment_vader(text):
    
        # Use the VADER model to predict the sentiment
        vader_scores = loaded_vader.polarity_scores(text)
        
        # Determine sentiment based on VADER compound score
        compound_score = vader_scores['compound']
        if compound_score >= 0.05:
            sentiment = 'POSITIVE'
        elif compound_score <= -0.05:
            sentiment = 'NEGATIVE'
        else:
            sentiment = 'NEUTRAL'
        
        return sentiment, compound_score, get_sentiment_emoticon(sentiment)

    # Option to choose between manual input and file upload
    analysis_option = st.radio("Choose analysis option:", ["Manual Input", "File Upload"])

    if analysis_option == "Manual Input":
        tweet = st.text_area("Enter a tweet to analyze sentiment:")
        
        if st.button("Analyze"):
            if tweet:
                label, score, emoticon = analyze_sentiment_vader(tweet)
                st.markdown(f"""
                <div style="text-align: center;">
                    <span style="font-size: 100px;">{emoticon}</span>
                    <div style="font-size: 24px;">Sentiment: {label}</div>
                    <div style="font-size: 18px;">Confidence Score: {score:.2f}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Please enter a tweet before analyzing.")

    else:  # File Upload option
        uploaded_file = st.file_uploader("Upload a CSV or TXT file", type=["csv", "txt"])
        
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.csv'): # .csv file
                df = pd.read_csv(uploaded_file)
                text_column = st.selectbox("Select the column containing the text to analyze:", df.columns)
            else:  # .txt file
                content = uploaded_file.getvalue().decode("utf-8")
                df = pd.DataFrame({"Text": content.split('\n')})
                text_column = "Text"

            if st.button("Analyze File"):
                # Apply sentiment analysis to each row
                results = [analyze_sentiment_vader(text) for text in df[text_column]]
                
                # Create new columns for sentiment, score and emoticon
                df['Sentiment'] = [r[0] for r in results]
                df['Score'] = [r[1] for r in results]
                df['Emoticon'] = [r[2] for r in results]

                # Display results
                st.write(df)

                # Display summary
                st.subheader("Summary")
                sentiment_counts = df['Sentiment'].value_counts()
                
                # Map sentiments to colors
                colors = sentiment_counts.index.map({
                    'POSITIVE': 'blue',
                    'NEGATIVE': 'red',
                    'NEUTRAL': 'gray'
                })
                
                # Create a bar plot color coded as per sentiment
                fig, ax = plt.subplots()
                sentiment_counts.plot(kind='bar', ax=ax, color=colors)
                plt.title("Sentiment Distribution")
                plt.xlabel("Sentiment")
                plt.ylabel("Count")
                st.pyplot(fig)

# Team tab
with tabs[2]:
    st.title("The Data Sentinels")
    # Load Lottie animation
    lottie_url = "https://lottie.host/18039274-4e01-4558-845e-a1d1d3b950eb/cKT9Btma01.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)
    # Style contact icons
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
    # Team member details
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
            "title": "Data Visualization Specialist",
            "bio": "Elizabeth excels at creating insightful and interactive data visualizations. Her skills are essential for presenting our findings in a clear and impactful manner.",
            "image": "the_team/elizabeth.jpg",
            "github": "ElizabethMasai",
            "email": "elizabethchemtaim@gmail.com",
            "linkedin": "elizabeth-masai-6aab8118a"
        },
        {
            "name": "Sheila Mulwa",
            "title": "Data Narrative Architect",
            "bio": "Sheila blends her data science and machine learning expertise with creativity, turning complex datasets into insightful visual narratives. Her engaging presentations make our models and findings accessible to both technical and non-technical audiences.",
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
    # Create two columns and loop through each member applying custom styles
    for member in team_members:
        col1, col2 = st.columns([1, 3])
        
        with col1: # Add member images
            try:
                image = Image.open(member["image"])
                st.image(image, width=150)
            except FileNotFoundError:
                st.image("https://via.placeholder.com/200", width=1500)
                
        with col2: # Apply custom styles
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
                font-style: italic;
            }}
            .member-bio {{
                margin-bottom: 10px;
                color: black;
            }}
            .member-contact a {{
                margin-right: 10px;
                color: #007bff;
                text-decoration: none;
            }}
            .member-contact a:hover {{
                color: #0056b3;
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
    # Load lottie animation
    lottie_url = "https://lottie.host/93047e01-af1c-425a-89f5-c4d49abc3aaa/LVMzN5PPXM.json"  
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=200)
    
    st.write("""
    The Olympic Sentiment Analyzer is a powerful tool designed to analyze public sentiment surrounding the 2024 Paris Olympic Games. 
    The application uses advanced natural language processing and machine learning techniques to process large volumes of 
    text data from Twitter and user-submitted content.
    It was created to provide real-time insights into public opinion and reactions to Olympic events, athletes and other related topics.
    """)

    st.subheader("How it works")
    st.write("""
    - Tweets are collected using a web-scraping tool known as Octoparse.
    - Each tweet is analyzed for sentiment using natural language processing.
    - Results are visualized and updated continuously.
    """)
    
    # st.subheader("Technologies used")
    # st.write("""
    # - Python
    # - Streamlit
    # - Pandas for data manipulation and analysis
    # - NLTK and VaderSentiment for sentiment analysis
    # - Scikit-Learn for machine learning operations
    # - Matplotlib and Seaborn for visualizations
    # """)

    st.write("""This project is developed by a team of data scientists and machine learning experts passionate about sports and data analysis. 
    Our goal is to provide valuable insights into public opinion and sentiment trends throughout the 2024 Olympic Games.
    """)

# Feedback tab
with tabs[4]:
    st.title("We Value Your Feedback")
    
    st.subheader("Share Your Thoughts")
    feedback = st.text_area("What do you think about our Olympic Sentiment Analyzer?")
    
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please enter your feedback before submitting.")

    st.markdown("---")
            
    st.subheader("Rate Our App")

    rating = st.radio("Select your rating:", options=[1, 2, 3, 4, 5], index=2)
    
    if st.button("Submit Rating"):
        st.success(f"Thank you for rating us {rating} star(s)!")

# Footer 
st.markdown("---")
st.markdown("© 2024 Olympic Sentiment Analyzer. All rights reserved.")
