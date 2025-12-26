
Kalshi is an exchange and so counterparties are people making offers. The prices of a binary event could display like 33% and 67%. The sum need not add to 100% however since there are bid/ask spreads. For sports betting, we use American odds. +100 = 50% because 100/200. +300 = 25% because 100/400. -300 = 75% because 300/400. We'll need to convert american odds to percents when dealing with sports. The first couple goals we should have is 1. Ordinary sports ev betting and 2. Pulling liquidity values.

For (1), pulling kalshi prices for sports and comparing to the market average or a benchmark like Pinnacle sportsbook will tell us if there's any value in kalshi prices. Any value also needs to overcome trading fees which vary between whether you're a maker or taker. Schedule found here: https://kalshi.com/docs/kalshi-fee-schedule.pdf and we'll talk about it.

For (2), a simple approach for following sharp money is when a single order of high liquidity is placed. It's probably even more important to care about such an order when it goes against the market. We'd possibly want to front run such orders.

I can send you my api key and private key. They're free to create when you have a kalshi account.


AI summary of files in Github

# Kalshi Data Pipeline

This repository contains a Python-based data pipeline for interacting with Kalshi's APIs, specifically focusing on fetching, organizing, and analyzing market and event data. The pipeline is designed for flexibility and extensibility, with separate modules for API calls, authentication, debugging, and data processing.

---

## **Repository Structure**
Here’s an overview of the main files and their purposes:

### **1. `sports_markets.py`**
- **Purpose**: Main script for interacting with Kalshi's API.
- Contains functions to fetch data for sports markets, competitions, and events.
- Includes functionality for filtering markets (e.g., high-volume markets, sports-related events).

### **2. `sports_markets_debug.py`**
- **Purpose**: Debugging-focused version of `sports_markets.py`.
- Outputs detailed debugging logs (e.g., raw Kalshi API responses) to assist with analyzing incomplete or missing data.
- Ideal for development and debugging.

### **3. `data_retrieval.py`**
- **Purpose**: Handles all API interactions (e.g., GET requests to Kalshi's endpoints).
- Centralized logic for making secure API calls with proper authentication.
- Ensures code reusability by separating data retrieval logic from other modules.

### **4. `auth.py`**
- **Purpose**: Manages authentication for Kalshi API access.
- Uses your API Key ID and private key to securely sign API requests.
- Essential for ensuring all API calls are authenticated.

### **5. `scheduler.py`**
- **Purpose**: A utility script that fetches, filters, and processes open markets.
- Includes functionality to identify markets with specific conditions (e.g., volume > $10,000, sorted by liquidity).
- Useful for scheduling periodic tasks to fetch and process data.

### **6. `analysis.py`**
- **Purpose**: (Optional) Analyzes and visualizes data fetched from Kalshi.
- Includes functions for data cleaning, statistical analysis, and creating visualizations (e.g., market trends).
- This file can be expanded as needed to support deeper analytics.

### **7. `requirements.txt`**
- **Purpose**: Lists Python dependencies for the project.
- Use it to install all required libraries:
  ```bash
  pip install -r requirements.txt
  ```

### **8. `.gitignore`**
- **Purpose**: Prevents sensitive or unnecessary files from being added to Git.
- Examples of files to ignore:
  - `__pycache__/`
  - `*.pyc`
  - Temporary files (`*.py~` or `*.un~`)
  - Sensitive files like `kalshi_key.pem`

---

## **Getting Started**

### 1. **Environment Setup**
- Ensure Python is installed (recommended version: Python 3.10+).
- Clone the repository:
  ```bash
  git clone https://github.com/AdamLipman/kalshi_bot.git
  cd kalshi_bot
  ```
- Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate   # On Linux/Mac
  .\venv\Scripts\Activate    # On Windows
  ```

### 2. **Install Dependencies**
- Install required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```

### 3. **Run the Pipeline**
- Start with `sports_markets.py` to fetch sports-related market data:
  ```bash
  python sports_markets.py
  ```

---

## **Future Enhancements**
- Expand `analysis.py` for data analytics and visualization.
- Add real-time data streaming functionality via Kalshi WebSockets.
- Automate periodic data fetching using a task scheduler (e.g., `scheduler.py`).

---

## **Contributing**
Feel free to fork this repository, submit pull requests, or open issues for feature requests or bug reports.

---

### License
This project is licensed under the MIT License.