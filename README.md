# Xplain Reddit Scanner

A cryptocurrency sentiment analysis tool that monitors Reddit for early pre-pump signals.

## What it does

This tool scans specified cryptocurrency subreddits to detect unusual activity patterns that may indicate upcoming price movements. It analyzes:

- **Mention frequency** - How often a coin is discussed
- **Engagement metrics** - Upvotes, comments, post scores
- **Author diversity** - Unique users vs. potential spam
- **Cross-subreddit activity** - Spread across communities

## How it works

1. **Scans Reddit** - Monitors r/cryptomoonshots, r/CryptoCurrency, and other crypto subreddits
2. **Extracts coin mentions** - Identifies ticker symbols (e.g., $BTC, $ETH)
3. **Calculates signal strength** - Aggregates data into a 0-100 score
4. **Sends alerts** - Notifies via Telegram when threshold is exceeded

## Signal Strength Algorithm

The signal is calculated based on five factors:

- **Mention Score** (0-30 pts): Number of mentions in timeframe
- **Upvote Score** (0-25 pts): Average post engagement
- **Comment Score** (0-20 pts): Discussion activity
- **Diversity Score** (0-15 pts): Unique authors mentioning
- **Cross-Sub Score** (0-10 pts): Spread across subreddits

**Thresholds:**
- 🔥 70-100: Very strong signal
- ⚠️ 50-69: Strong signal
- 📊 20-49: Moderate signal
- 📉 0-19: Weak signal

## Installation

```bash
# Clone repository
git clone https://github.com/[username]/xplain-reddit-scanner.git
cd xplain-reddit-scanner

# Install dependencies
pip install -r requirements.txt

# Configure Reddit API
# Create config.py with your credentials (see config.example.py)

# Run
python xplain_reddit.py

Reddit API Setup

1. Go to https://www.reddit.com/prefs/apps
2. Create a "script" app
3. Copy Client ID and Secret
4. Add to config.py (not included in repo)

Disclaimer

This is for educational and research purposes only. Not financial advice. Always DYOR (Do Your Own Research).

The tool only reads public Reddit data. It does not post, comment, or interact with users.

License

MIT License - Open source, use at your own risk.
