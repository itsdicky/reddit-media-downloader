from downloader import download
from praw import Reddit

def download_saved(reddit: Reddit, save_path: str, limit: int) -> None:
    '''
    This function will download saved Reddit submissions from the user and
    save them to the specified directory path
    
    Args:
        reddit: A ``Reddit`` class from praw package
        save_path: A directory path where the content will stored
        limit: Number of submissions that will be tried to download
    
    Returns:
        None
    '''
    savedcontent = reddit.user.me().saved(limit=limit)

    print('[DOWNLOAD START]')

    for submission in savedcontent:
        
        url = submission.url
        print('Downloading file from '+ url)

        #download
        download(url=url, save_path=save_path, file_name=submission.id)

    print('[DOWNLOAD FINISHED]')


def download_submission(reddit: Reddit, submission_url: str, save_path: str, file_name: str) -> None:
    '''
    This function will download a specified Reddit submissions from the URL
    and save them to the specified directory path
    
    Args:
        reddit: A ``Reddit`` class from praw package
        submission_url: A Reddit submission URL
        save_path: A directory path where the content will stored
        file_name: The name of the file to be saved
    
    Returns:
        None
    '''
    submission = reddit.submission(url=submission_url)
    url = submission.url

    print('[DOWNLOAD START]')
    print('Downloading file from '+ url)

    #download
    download(url=url, save_path=save_path, file_name=file_name)

    print('[DOWNLOAD FINISHED]')

def download_subreddit(reddit: Reddit, subreddit_name: str, save_path: str, limit: int) -> None:
    '''
    This function will download Reddit submissions from a specified
    subreddit and save them to the specified directory path
    
    Args:
        reddit: A ``Reddit`` class from praw package
        subreddit_name: The subreddit name
        save_path: A directory path where the content will stored
        limit: Number of submissions that will be tried to download
    
    Returns:
        None
    '''
    subreddit = reddit.subreddit(subreddit_name)
    
    print('[DOWNLOAD START]')

    for submission in subreddit.hot(limit=limit):
        url = submission.url
        print('Downloading file from '+ url)

        #download
        download(url=url, save_path=save_path, file_name=submission.id)

    print('[DOWNLOAD FINISHED]')


def download_redditor(reddit: Reddit, redditor_name: str, save_path: str, limit: int) -> None:
    '''
    This function will download Reddit submissions from a specified
    redditor and save them to the specified directory path
    
    Args:
        reddit: A ``Reddit`` class from praw package
        redditor_name: The redditor username
        save_path: A directory path where the content will stored
        limit: Number of submissions that will be tried to download
    
    Returns:
        None
    '''
    redditor = reddit.redditor(redditor_name)
    
    print('[DOWNLOAD START]')

    for submission in redditor.submissions.hot(limit=limit):
        url = submission.url
        print('Downloading file from '+ url)

        #download
        download(url=url, save_path=save_path, file_name=submission.id)

    print('[DOWNLOAD FINISHED]')