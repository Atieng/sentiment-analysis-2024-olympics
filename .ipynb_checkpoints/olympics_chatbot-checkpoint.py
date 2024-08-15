import streamlit as st
import pandas as pd

dataset = pd.read_csv('cleaned_olympics_data.csv')

# Function to get medal count by country
def get_medal_count_by_country(country):
    # Normalize country name to avoid partial matches and case sensitivity issues
    country_matches = dataset[dataset['country'].str.lower() == country.lower()]
    
    if not country_matches.empty:
        summary = country_matches.groupby('medal_type').size().to_dict()
        return summary
    else:
        return f"No medal information found for {country}."

# Function to get medals won by a specific athlete
def get_medals_by_athlete(athlete_name):
    athlete_medals = dataset[dataset['name'].str.contains(athlete_name, case=False, na=False)]
    if not athlete_medals.empty:
        return athlete_medals[['medal_date', 'medal_type', 'event']]
    else:
        return f"No medal information found for athlete {athlete_name}."

# Function to get event details
def get_medals_by_event(event_name):
    event_medals = dataset[dataset['event'].str.contains(event_name, case=False, na=False)]
    if not event_medals.empty:
        return event_medals[['medal_date', 'medal_type', 'name', 'country']]
    else:
        return f"No medal information found for event {event_name}."

# Streamlit app setup
st.title("Paris 2024 Olympics Medals")

# Input for user query
user_query = st.text_input("Ask me anything about the Paris 2024 Olympics:")

if user_query:
    if "medal" in user_query.lower():
        country = st.text_input("Enter the country name:")
        if country:
            response = get_medal_count_by_country(country)
            st.write(response)
    elif "athlete" in user_query.lower():
        athlete_name = st.text_input("Enter the athlete's name:")
        if athlete_name:
            response = get_medals_by_athlete(athlete_name)
            st.write(response)
    elif "event" in user_query.lower():
        event_name = st.text_input("Enter the event name:")
        if event_name:
            response = get_medals_by_event(event_name)
            st.write(response)
    else:
        # If none of the above keywords are found, assume the query is about a country
        response = get_medal_count_by_country(user_query)
        st.write(response)
