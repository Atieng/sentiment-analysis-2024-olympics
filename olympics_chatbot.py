import pandas as pd
import os
import streamlit as st

# Load the individual CSV files
schedules = pd.read_csv('Paris_olympics_data/schedules.csv')
schedules_preliminary = pd.read_csv('Paris_olympics_data/schedules_preliminary.csv')
teams = pd.read_csv('Paris_olympics_data/teams.csv')
torch_route = pd.read_csv('Paris_olympics_data/torch_route.csv')
venues = pd.read_csv('Paris_olympics_data/venues.csv')
athletes = pd.read_csv('Paris_olympics_data/athletes.csv')
coaches = pd.read_csv('Paris_olympics_data/coaches.csv')
events = pd.read_csv('Paris_olympics_data/events.csv')
medallists = pd.read_csv('Paris_olympics_data/medallists.csv')
medals = pd.read_csv('Paris_olympics_data/medals.csv')
medals_total = pd.read_csv('Paris_olympics_data/medals_total.csv')

# Load the results folder contents
results_folder = 'Paris_olympics_data/results'
results_files = {file.split('.')[0]: pd.read_csv(os.path.join(results_folder, file))
                 for file in os.listdir(results_folder) if file.endswith('.csv')}

def get_medal_count_by_country(country):
    return medals_total[medals_total['Country'] == country].to_dict(orient='records')

def get_athlete_info(athlete_name):
    return athletes[athletes['Name'].str.contains(athlete_name, case=False, na=False)].to_dict(orient='records')

def get_sport_results(sport):
    sport_results = results_files.get(sport.lower())
    if sport_results is not None:
        return sport_results.to_dict(orient='records')
    else:
        return f"No results found for {sport}."
st.title("olympics_chatbot")

user_query = st.text_input("Ask me about the Olympics:")

if user_query:
    if "medal" in user_query.lower():
        country = st.text_input("Enter the country name:")
        if country:
            response = get_medal_count_by_country(country)
            st.write(response)
    elif "athlete" in user_query.lower():
        athlete_name = st.text_input("Enter the athlete's name:")
        if athlete_name:
            response = get_athlete_info(athlete_name)
            st.write(response)
    elif "result" in user_query.lower():
        sport = st.text_input("Enter the sport name:")
        if sport:
            response = get_sport_results(sport)
            st.write(response)
    else:
        st.write("Sorry, I didn't understand the query.")
