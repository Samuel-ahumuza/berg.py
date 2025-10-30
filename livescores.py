import requests
import json
import time

# NOTE: This is a demo key provided by TheSportsDB. For production use,
# you should sign up for your own key.
API_KEY = "50130162"

def get_live_scores(league_id="4328"):
    """
    Fetches live soccer scores for a specific league.
    :param league_id: The ID of the league to fetch scores for (e.g., '4328' for the English Premier League).
    """
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventslive.php?s=Soccer"
    
    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the response was an error
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the 'events' key exists and is not empty
        if data.get('events'):
            print("--- Live Match Scores ---")
            for event in data['events']:
                home_team = event['strHomeTeam']
                away_team = event['strAwayTeam']
                home_score = event['intHomeScore']
                away_score = event['intAwayScore']
                status = event['strStatus']
                
                print(f"{home_team} {home_score} - {away_team} {away_score} ({status})")
            print("-------------------------")
        else:
            print("No live matches found at the moment.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON from the response.")

# Example usage: Poll for scores every 30 seconds
if __name__ == "__main__":
    while True:
        get_live_scores()
        print("Waiting for 30 seconds for the next update...")
        time.sleep(30)