# tweeter--scraper
A Python-based tool to extract tweets from a user account on X (formerly Twitter), with both official API and web scraping (snscrape) support.
## Features

- Extract tweets from any public X/Twitter user account.
- Save tweets as CSV in a `data/` folder.
- Easy to configure for API  usage.
- Modular code structure for easy extension.


## Folder Structure

```
tweet-scraper/
│
├── requirements.txt
├── config.py
├── main.py
├── scraper/
│   ├── __init__.py
│   ├── twitter_api.py
│   └── save.py
└── data/
```
## Setup

1. **Clone the repository:**
   ```bash
  [ git clone https://github.com/YOUR_USERNAME/tweet-scraper.git](https://github.com/BATzAashish/tweeter--scraper.git)
   cd tweet-scraper
   ```
