
from data_retrieval import fetch_data
import json

# Base API URL for Kalshi (authenticated access)
BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

# Replace with your valid credentials
PRIVATE_KEY_PATH = "./kalshi_key.pem"
API_KEY = "your-api-key-id"

def fetch_sports_and_competitions():
    """
    Attempt to fetch all sports and competitions currently listed by `/search/filters_by_sport`.
    """
    endpoint = "/search/filters_by_sport"
    data = fetch_data(BASE_URL, endpoint, PRIVATE_KEY_PATH, API_KEY)

    print("\n--- Debugging `/search/filters_by_sport` ---")
    print(json.dumps(data, indent=4))  # Full API response

    if data and "sports" in data:
        print("\n--- Available Sports and Competitions ---")
        for sport in data["sports"]:
            print(f"Sport: {sport.get('name', 'N/A')}")
            for competition in sport.get("competitions", []):
                print(f"  Competition: {competition.get('name', 'N/A')} ({competition.get('ticker', 'N/A')})")
    else:
        print("\nFailed to fetch sports and competitions.")

def fetch_events(with_nested_markets=False):
    """
    Fetch all events, enhanced with complete event debug output for analysis.
    """
    endpoint = "/events"
    if with_nested_markets:
        endpoint += "?with_nested_markets=true"

    data = fetch_data(BASE_URL, endpoint, PRIVATE_KEY_PATH, API_KEY)

    print("\n--- Debugging `/events` Full Response ---")
    print(json.dumps(data, indent=4))  # Full API response for analysis

    if data and "events" in data:
        print("\n--- Sports Events ---")
        for event in data["events"]:
            # Debugging all fields for the event
            print(f"Event Debug:\n{json.dumps(event, indent=4)}\n")

            # Manual filtering for NBA-related events based on the title
            if "NBA" in event.get("title", "") or "Basketball" in event.get("title", ""):
                print(f"Filtered NBA Event: {event.get('title')}")
                print(f"  Ticker: {event.get('ticker', 'N/A')}")
                print(f"  Start Time: {event.get('start_time', 'N/A')}")
                print(f"  Status: {event.get('status', 'N/A')}")
    else:
        print("\nFailed to fetch events.")

def fetch_event_details(event_ticker):
    """
    Fetch details for a specific event by `event_ticker`.
    """
    endpoint = f"/events/{event_ticker}"
    data = fetch_data(BASE_URL, endpoint, PRIVATE_KEY_PATH, API_KEY)

    print(f"\n--- Debugging `/events/{event_ticker}` Response ---")
    if data:
        print(json.dumps(data, indent=4))  # Full API response
    else:
        print(f"Failed to fetch event details for {event_ticker}.")

if __name__ == "__main__":
    # Step 1: Fetch and debug sports and competition data
    print("\n### Fetching Sports and Competitions ###")
    fetch_sports_and_competitions()

    # Step 2: Fetch and debug all events (filtering for NBA-related titles)
    print("\n### Fetching All Events ###")
    fetch_events(with_nested_markets=True)

    # Step 3: Fetch and debug details for a specific event
    example_ticker = "KXNBA2025-LAK@NYK"  # Replace with a valid ticker from the debug output
    print("\n### Fetching Details for Specific Event ###")
    fetch_event_details(event_ticker=example_ticker)
    
