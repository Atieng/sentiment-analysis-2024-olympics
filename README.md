
# Sentiment Analysis-Paris Olympics 2024

![attachment:logo.png](Images/logo.png)

## Table of Contents

1. [Business Understanding](#business-understanding)
   - [Overview](#overview)
   - [Goal](#goal)
   - [Objectives](#objectives)
   - [Stakeholders](#stakeholders)

2. [Data Understanding](#data-understanding)

3. [Data Preparation](#data-preparation)

4. [Modeling](#modeling)

5. [Conclusion](#conclusion)

6. [Recommendations](#recommendations)

7. [Next Steps](#next-steps)

8. [Deployment](#deployment)
   - [Installation](#installation)

9. [Libraries and Tools Used](#libraries-and-tools-used)

10. [License](#license)

11. [Contributing Members](#contributing-members)

12. [Contacts](#contacts)

13. [Repository Structure](#repository-structure)

## Business Understanding

**Overview**

The Paris Olympics 2024 promises to be one of the most significant global events of the decade, uniting nations, cultures, and athletes from around the world. As excitement builds and discussions around the event intensify, understanding public sentiment becomes crucial for stakeholders, including organizers, sponsors, media outlets, and even fans. This project aims to analyze the sentiment of conversations surrounding the Paris Olympics 2024, offering insights into public opinion, perceptions, and the overall sentiment landscape leading up to and during the event.

**Goal**

This project aims to capture and decode the global sentiment surrounding the Paris Olympics 2024. By analyzing emotions and opinions from diverse sources, we seek to provide real-time insights that empower organizers, brands, and media to align with public sentiment, ensuring the Paris Olympics 2024 resonates positively worldwide.

**Objectives**

1. Develop a comprehensive social media sentiment analysis model that accurately captures and interprets public sentiment about the Paris Olympics from social media data.
2. To extract, preprocess and clean social media data from multiple platforms addressing quality issues and handling multilingual content related to the Paris Olympics. 
3. To develop and train advanced natural language processing models to accurately classify sentiments incorporating techniques to handle sarcasm and contextual nuances. 
4. To create interactive visualizations to display sentiment trends and key events providing actionable insights to stakeholders based on comprehensive analysis of public opinions.

## Stakeholders
1. Organizers of the Paris Olympics 2024 - Sentiment analysis helps them gauge public
opinion allowing them to make informed decisions and adjust their strategies
accordingly.
2. Sponsors - Sentiment analysis helps them understand how their brand is perceived in
relation to the Olympics.
3. Media outlets - Sentiment analysis provides them with insights into public interest and
trending topics.
4. Fans and general public - They are the primary audience for the Olympics and their
sentiment directly impacts the event's success.
5. Athletes - They are the central figures of the Olympics and public sentiment towards
them can affect their performance and well-being.
6. Local authorities and businesses in Paris - The Olympics significantly impact the host
city and sentiment analysis can help gauge public opinion on local issues related to the
event.

## Data Understanding

The data was extracted from X using Octorparse Webscraping Tool. The focus was on tweets in the form of hashtags, comments and retweets discussing the various aspects of the Paris Olympics.
 
## Data Preparation

The data processing step involved analyzing and cleaning a merged dataset of tweets related to the 2024 Paris Olympics originally composed of multiple CSV files. A DataUnderstanding class was created to examine the dataset revealing missing values and discrepancies as well as a large number of apparent duplicates most of which were false positives due to partial similarities.
## Visualizations
 
 
[![Visualization DashBoard](https://img.shields.io/badge/Olympics-F4C300?style=plastic)]( 
https://public.tableau.com/app/profile/ivy.atieng/viz/2024PARISOLYMPICSVISUALIZATIONS/Dashboard2)
 ## Modeling
  
The model development and evaluation process involved testing several approaches. We started with traditional machine learning models, including Logistic Regression, Support Vector Machine, Random Forest, and Naive Bayes. Among these, the Random Forest model emerged as the best performer initially achieving 97.4% accuracy which slightly decreased to 96.6% after tuning. We also implemented an XGBoost model using RandomizedSearchCV for hyperparameter tuning, which achieved 82.2% accuracy. The VADER model demonstrated excellent performance with 94.92% accuracy and impressive overall metrics: 95.20% Precision, 94.92% Recall and 95.01% F1-Score. In contrast, the DistilBERT model showed lower performance with 44.34% accuracy and overall metrics of 45.94% Precision, 44.34% Recall and 44.62% F1-Score.

## Conclusion

> The VADER (Valence Aware Dictionary and sEntiment Reasoner) model significantly outperformed all other models including the tuned Random Forest. The success of VADER, a rule-based model designed specifically for social media text, highlights the importance of domain-specific tools in sentiment analysis especially when dealing with the nuanced language of Olympic-related discussions on social media platforms. 

## Recommendations

1.	Implement a real-time sentiment tracking dashboard for organizers and media partners, allowing them to respond quickly to shifts in public opinion. 
2.	Develop a multi-lingual sentiment analysis capability to cater to the international nature of the Olympics using language-specific versions of VADER where available. 
3.	Create a sentiment-based alert system for potentially controversial or viral topics enabling rapid response from the communications team. 
4.	Integrate sentiment analysis results with other data sources (e.g. ticket sales, TV ratings) to provide a comprehensive view of public engagement. 
5.	Use sentiment trends to guide content creation and social media strategies focusing on themes and athletes that generate positive engagement. 
6.	Provide regular sentiment reports to sponsors helping them optimize their Olympic-related marketing campaigns. 
7.	Collaborate with local Paris businesses to use sentiment data for improving visitor experiences during the Olympics.

## Next steps

1.	Incorporate Olympics-specific features such as mentions of specific sports, athletes or events to improve classification accuracy. 
2.	Create a specialized lexicon for VADER that includes Olympic-specific terms and their sentiment associations. 
3.	Extend the sentiment analysis to multiple social media platforms and news sources for a more comprehensive view. 
4.	Develop user-friendly and interactive dashboards for stakeholders to explore sentiment data in real-time. 
5.	Set up a system to compare sentiment trends with previous Olympic events to identify unique characteristics of the Paris Olympics. 
6.	Develop algorithms to automatically identify and report on significant shifts in sentiment or emerging trends. 
7.	Offer training sessions for various stakeholders on how to interpret and act upon the sentiment analysis results. 
8.	Set up infrastructure for continued analysis post-Olympics to track the event's lasting impact on public sentiment towards Paris and the Olympic movement.

### Deployment
Check out our app by clicking on your favorite color: [![Paris](https://img.shields.io/badge/Paris-0072CE?style=plastic&logo=Olympics&logoColor=white)](https://olympicssentimentanalysis.streamlit.app/)
[![Olympics](https://img.shields.io/badge/Olympics-F4C300?style=plastic)](https://olympicssentimentanalysis.streamlit.app/)
[![Sentiment](https://img.shields.io/badge/Sentiment-000000?style=plastic)](https://olympicssentimentanalysis.streamlit.app/)
[![Analysis](https://img.shields.io/badge/Analysis-00843D?style=plastic)](https://olympicssentimentanalysis.streamlit.app/)
[![App](https://img.shields.io/badge/App-EE334E?style=plastic)](https://olympicssentimentanalysis.streamlit.app/)

### Installation 
To run the application locally, follow the following steps:

**Clone the repository**

**https:**
```
git clone https://github.com/Atieng/sentiment-analysis-2024-olympics.git
```
**ssh:**
```
git clone git@github.com:Atieng/sentiment-analysis-2024-olympics.git
```
**Navigate to the project directory**

```
cd sentiment-analysis-2024-olympics.git
```
**Create a virtual environment**

```
python -m venv vader_env
```
**Activate the virtual environment**

**Windows:**
```
vader_env\Scripts\activate
```
**MacOS/Linux:**
```
source vader_env/bin/activate
```
**Install dependencies**
```
pip install -r requirements.txt
```
**Execute the app on Streamlit**
```
streamlit run vader.py
```

## 🔗 Libraries and Tools Used
![numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![tensorflow](https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=blue)
![keras](https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![nltk](https://img.shields.io/badge/NLTK-154f3c?style=for-the-badge&logo=python&logoColor=white)
![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=pink)
![vadersentiment](https://img.shields.io/badge/vaderSentiment-7D4698?style=for-the-badge&logo=python&logoColor=white)
![scikitlearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)


## License
MIT License

## Contributing members
- [Ivy Atieng](https://github.com/Atieng)
- [Evaclaire Wamitu](https://github.com/Eva-Claire)
- [Sheila Mulwa](https://github.com/Sheila-Mulwa)
- [Titus Kaluma](https://github.com/Kaluma-67)
- [Elizabeth Masai](https://github.com/ElizabethMasai)
  
## Contacts
- atiengivylisa@gmail.com
- evamunyika@gmail.com
- sheila.n.mulwa@gmail.com
- mwirigikaluma@gmail.com
- elizabethchemtaim@gmail.com

Kindly don't hesitate to reach out to the team if you have any questions.

## Repository Structure

```
Sentiment Analysis-Paris Olympics 2024/
│
└── Project Files/
    ├── .ipynb_checkpoints
    ├── .streamlit
    ├── Csv Files
    ├── Images
    ├── Models
    ├── Notebooks
    ├── the_team
    ├── .DS_Store
    ├── .gitattributes
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── Sentiment Analysis Presentation.pdf
    ├── requirements.txt
    ├── sentiment_analysis_paris_olympics.docx
    └── vader.py
      
```


