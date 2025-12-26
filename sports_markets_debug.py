
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
    Fetch all events, with optional nested market data inclusion.
    """
    endpoint = "/events"
    if with_nested_markets:
        endpoint += "?with_nested_markets=true"

    data = fetch_data(BASE_URL, endpoint, PRIVATE_KEY_PATH, API_KEY)

    print("\n--- Debugging `/events` Response ---")
    print(json.dumps(data, indent=4))  # Full API response

    if data and "events" in data:
        print("\n--- Sports Events ---")
        for event in data["events"]:
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
    # Fetch sports and competitions
    fetch_sports_and_competitions()

    # Fetch all events (debug response for titles or tickers with "NBA", "Basketball")
    fetch_events(with_nested_markets=True)

    # Fetch details for a specific event, if applicable
    example_ticker = "KXNBA2025-LAK@NYK"  # Replace with a valid ticker if found
    fetch_event_details(event_ticker=example_ticker)
