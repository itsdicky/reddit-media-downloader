# reddit-media-downloader

A simple code that can be used to download image and gif form reddit submission

Supported media extension: gif, jpg, jpeg, png

## Configuration

Before use this script, you should create a configuration file named config.ini

```ini
[REDDIT]
CLIENT_ID = <your client id>
CLIENT_SECRET = <your secret>
USER_AGENT = script:com.rmd.script:v1.0 (by u/satdic)
USERNAME = <your reddit username>
PASSWORD = <your reddit password>

[SETUP]
SAVE_DIRECTORY = <your save directory>
```

## Usage

Run this:

```bash
python main.py [download type]
```

There is 4 download type:
1. saved, will download media from your saved submission
2. subreddit, will download media from specific subreddit
3. redditor, will download media from specific redditor
4. submission, will download media from specific submission