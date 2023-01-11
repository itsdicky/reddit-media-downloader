import praw
import controller
import sys
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

reddit = praw.Reddit(
    client_id=config.get('REDDIT', 'CLIENT_ID'),
    client_secret=config.get('REDDIT', 'CLIENT_SECRET'),
    user_agent=config.get('REDDIT', 'USER_AGENT'),
    username=config.get('REDDIT', 'USERNAME'),
    password=config.get('REDDIT', 'PASSWORD')
)

setup = {
    "directory": config.get('SETUP', 'SAVE_DIRECTORY'),
}

def main():
    num_args = len(sys.argv)
    
    if num_args == 2:
        input_args = sys.argv[1]
        match input_args:
            case 'saved':
                limit = int(input('Enter submission limit: '))
                controller.download_saved(reddit=reddit, save_path=setup["directory"], limit=limit)
            case 'subreddit':
                subreddit = input('Enter subreddit name: ')
                limit = int(input('Enter submission limit: '))
                controller.download_subreddit(reddit=reddit, save_path=setup['directory'], subreddit_name=subreddit, limit=limit)
            case 'redditor':
                redditor = input('Enter redditor name: ')
                limit = int(input('Enter submission limit: '))
                controller.download_redditor(reddit=reddit, save_path=setup['directory'], redditor_name=redditor, limit=limit)
            case 'submission':
                url = input('Enter submission URL: ')
                file_name = input('Enter file name: ')
                controller.download_submission(reddit=reddit, save_path=setup['directory'], submission_url=url, file_name=file_name)
    else:
        print('usage: python main.py [download type]')

if __name__ == '__main__':
    main()
    
