# reddit-media-downloader

A simple code that can be used to download images and gifs from Reddit submissions and store them in a specific directory. This code uses [PRAW](https://praw.readthedocs.io/en/stable/) to get media URLs from Reddit.

> _Supported media extension: gif, jpg, jpeg, png_

## Installation

```bash
pip install praw
```

## Configuration

Before using this script, you should create a configuration file named `config.ini` inside the root directory, the content should be like this:

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

For `CLIENT_ID` and `CLIENT_SECRET` you can get them from [Reddit](https://www.reddit.com/prefs/apps) or you can check [OAuth2](https://github.com/reddit-archive/reddit/wiki/OAuth2) if still confused

## Usage

### How to run this script

```
python main.py [download type]
```

While running the script, you will be shown several forms for additional information like submission limit, redditor username, subreddit name, and submission URL.

There is 4 __download types__:
1. `saved`, will download media from your saved submission.
2. `subreddit`, will download media from specific subreddit.
3. `redditor`, will download media from specific redditor.
4. `submission`, will download a single media from specific.submission

### Example

```bash
python main.py saved
```

Then you will be shown like this

```
Enter submission limit:
```

Fill in the number of submissions you will download and it will try to download media from your saved submission with the specific limit you are given.

> _Note: It will download supported file extensions only, so the not supported ones will be skipped._

## Contact

itsDicky - disatriage@gmail.com

Project Link: https://github.com/itsdicky/reddit-media-downloader