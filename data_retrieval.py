import requests
from auth import generate_auth_headers

def fetch_data(base_url, endpoint, private_key_path, api_key):
    """Make an authenticated request to Kalshi API."""
    url = f"{base_url}{endpoint}"
    headers = generate_auth_headers(private_key_path, api_key, "GET", endpoint)
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None
