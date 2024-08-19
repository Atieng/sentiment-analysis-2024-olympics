
# Sentiment Analysis-Paris Olympics 2024

![attachment:logo.png](Images/logo.png)

## Overview
The Paris Olympics 2024 promises to be one of the most significant global events of the decade, uniting nations, cultures, and athletes from around the world. As excitement builds and discussions around the event intensify, understanding public sentiment becomes crucial for stakeholders, including organizers, sponsors, media outlets, and even fans. This project aims to analyze the sentiment of conversations surrounding the Paris Olympics 2024, offering insights into public opinion, perceptions, and the overall sentiment landscape leading up to and during the event.

## Goal
This project aims to capture and decode the global sentiment surrounding the Paris Olympics 2024. By analyzing emotions and opinions from diverse sources, we seek to provide real-time insights that empower organizers, brands, and media to align with public sentiment, ensuring the Paris Olympics 2024 resonates positively worldwide.

## Objectives
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

 ## CRISP-DM Methodology

**Data understanding**

The data was extracted from X using Octorparse Webscraping Tool. The focus was on tweets in the form of hashtags, comments and retweets discussing the various aspects of the Paris Olympics.
 
**Data preparation/ data cleaning**

The data processing step involved analyzing and cleaning a merged dataset of tweets related to the 2024 Paris Olympics, originally composed of multiple CSV files. A DataUnderstanding class was created to examine the dataset, revealing missing values and discrepancies, as well as a large number of apparent duplicates, most of which were false positives due to partial similarities.


  **Modeling**
  
The modeling process involved evaluating several machine learning models including Logistic Regression, Support Vector Machine, Random Forest and Naive Bayes using a TF-IDF vectorization approach. The models were trained on a balanced dataset created using SMOTE to address class imbalance. After initial evaluation the Random Forest model emerged as the best performer among these traditional ML models. Hyperparameter tuning was then performed on the Random Forest model to optimize its performance. Pre-trained models like VADER and DistilBERT were tested for comparison. The VADER model outperformed all others achieving an impressive accuracy of 0.946.

**Conclusion**

The VADER (Valence Aware Dictionary and sEntiment Reasoner) model significantly outperformed all other models including the tuned Random Forest achieving an accuracy of 94.60%, precision of 94.74%, recall of 94.60% and an F1-score of 94.65%. These metrics exceeded the predefined success criteria across all sentiment categories (positive, negative and neutral). The success of VADER, a rule-based model designed specifically for social media text, highlights the importance of domain-specific tools in sentiment analysis especially when dealing with the nuanced language of Olympic-related discussions on social media platforms. 

**Recommendations**

Based on the outstanding performance of the VADER model, it is recommended to implement a comprehensive sentiment analysis strategy for the 2024 Paris Olympics. This should include developing a real-time sentiment tracking dashboard for organizers and media partners to enable quick responses to public opinion shifts. Expanding the analysis to multiple languages will cater to the international nature of the Olympics. Implementing a sentiment-based alert system for potentially controversial topics will allow for rapid communication team responses. Integrating sentiment analysis results with other data sources like ticket sales and TV ratings will provide a holistic view of public engagement. Using sentiment trends to guide content creation and social media strategies will help focus on themes and athletes generating positive engagement. Regular sentiment reports should be provided to sponsors to optimize their Olympic-related marketing campaigns. Lastly, collaborating with local Paris businesses to use sentiment data can help improve visitor experiences during the Olympics.

**Next steps**

To further enhance the sentiment analysis capabilities for the 2024 Paris Olympics, several key steps should be taken. First, improve feature engineering by incorporating Olympics-specific features such as mentions of particular sports, athletes or events. Develop a custom Olympic VADER lexicon to include specialized terms and their sentiment associations. Extend the analysis to multiple social media platforms and news sources for a more comprehensive view. Create interactive, user-friendly dashboards for stakeholders to explore real-time sentiment data. Establish a benchmarking system to compare sentiment trends with previous Olympic events. Develop algorithms to automatically identify and report significant shifts in sentiment or emerging trends. Conduct training sessions for various stakeholders on interpreting and acting upon the sentiment analysis results. Set up infrastructure for continued analysis post-Olympics to track the event's lasting impact on public sentiment towards Paris and the Olympic movement. Finally, preprocess the multilingual Olympics data and fine-tune a model to accurately detect sentiment across different languages ensuring a truly global analysis of public opinion.

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
    ├── Csv Files
    ├── Images
    ├── Models
    ├── Notebooks
    ├── X_data
    ├── the_team
    ├── .DS_Store
    ├── .gitattributes
    ├── .gitignore
    ├── LICENSE
    ├── Presentation_Capstone.pptx
    ├── README.md
    ├── logo.png
    ├── presentation.pdf
    ├── requirements.txt
    ├── sentiment.ipynb
    ├── sentiment_analysis_paris_olympics.docx
    ├── sentiment_analysis_word_doc.pdf
    └── vader.py
      
```


