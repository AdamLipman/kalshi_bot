
from data_retrieval import fetch_data
import json  # For debugging or pretty-printing

# Base API URL for Kalshi
BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

# Replace these with your valid credentials
PRIVATE_KEY_PATH = "./kalshi_key.pem"  # Path to your private key
API_KEY = "your-api-key-id"            # Kalshi API Key ID

def display_markets():
    """
    Fetch active markets, filter by significant trading volume (> $10,000 traded), 
    and sort the results by liquidity (highest to lowest).
    """
    endpoint = "/markets?status=open"  # Fetch all open markets
    data = fetch_data(BASE_URL, endpoint, PRIVATE_KEY_PATH, API_KEY)

    if not data or "markets" not in data:
        print("\nNo markets found or failed to fetch data.")
        return

    # Debug: Print raw volumes for all markets to verify the data
    print("\n--- Debug: Raw Volumes for All Markets ---")
    for market in data["markets"]:
        print(f"{market.get('ticker')}: Volume = {market.get('volume', 0)}")

    # Filter markets with volume > 10,000
    significant_markets = [
        market for market in data["markets"]
        if market.get("volume", 0) > 10000  # Enforce strict filtering
    ]

    # Sort markets by liquidity in descending order
    sorted_markets = sorted(significant_markets, key=lambda m: m.get("liquidity", 0), reverse=True)

    # Display the filtered and sorted markets
    if sorted_markets:
        print("\n--- Filtered Markets (Volume > $10K, Sorted by Liquidity) ---")
        for market in sorted_markets:
            ticker = market.get("ticker", "N/A")
            title = market.get("title", "No Title Provided")
            volume = market.get("volume", "N/A")
            yes_bid = market.get("yes_bid", "N/A")
            no_bid = market.get("no_bid", "N/A")
            yes_ask = market.get("yes_ask", "N/A")
            no_ask = market.get("no_ask", "N/A")
            liquidity = market.get("liquidity", "N/A")

            print(f"Ticker: {ticker}")
            print(f"  Title: {title}")
            print(f"  Volume: {volume}")
            print(f"  Yes Bid: {yes_bid}¢ | Yes Ask: {yes_ask}¢")
            print(f"  No Bid: {no_bid}¢ | No Ask: {no_ask}¢")
            print(f"  Liquidity: {liquidity}\n")
    else:
        print("\nNo markets match the criteria (Volume > 10,000).")

if __name__ == "__main__":
    display_markets()
