#!/usr/bin/env python3
"""
Xplain Reddit Scanner - Pre-Pump Signal Detection
Monitors crypto subreddits for early pump indicators
"""

import sqlite3
import re
import json
from datetime import datetime, timedelta

# Try to import Reddit API wrapper
try:
    import praw
    PRAW_AVAILABLE = True
except ImportError:
    PRAW_AVAILABLE = False
    print("Warning: praw not installed. Running in demo mode.")

# Try to load config
try:
    from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
except ImportError:
    REDDIT_CLIENT_ID = "YOUR_CLIENT_ID"
    REDDIT_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
    REDDIT_USER_AGENT = "XplainBot/1.0"

# Configuration
DB_PATH = "xplain.db"
TARGET_SUBREDDITS = [
    "cryptomoonshots",
    "CryptoCurrency",
    "SatoshiStreetBets",
    "altcoin",
    "CryptoMarkets"
]

# Known crypto tickers for validation
COMMON_TICKERS = {
    "BTC", "ETH", "BNB", "XRP", "SOL", "ADA", "AVAX", "DOT", "MATIC",
    "LINK", "UNI", "AAVE", "COMP", "MKR", "YFI", "SUSHI", "CRV",
    "DOGE", "SHIB", "PEPE", "FLOKI", "BONK", "MEME", "WOJAK",
    "VET", "FIL", "TRX", "ETC", "XTZ", "ALGO", "ATOM", "NEAR",

Xplain_data_bot, [14.04.26 06:46]
    "FTM", "GRT", "MANA", "SAND", "AXS", "ENJ", "CHZ", "FLOW"
}


class RedditMonitor:
    """Monitor Reddit for crypto mentions and calculate signal strength"""
    
    def __init__(self):
        self.reddit = None
