from downloader import download

def download_saved(reddit, save_path, limit) -> None:
    savedcontent = reddit.user.me().saved(limit=limit)

    print('[DOWNLOAD START]')

    for submission in savedcontent:
        
        url = submission.url
        print('Downloading file from '+ url)

        #download
        download(url=url, save_path=save_path, file_name=submission.id)

    print('[DOWNLOAD FINISHED]')


def download_submission(reddit, submission_url, save_path, file_name) -> None:
    submission = reddit.submission(url=submission_url)
    url = submission.url

    print('[DOWNLOAD START]')
    print('Downloading file from '+ url)

    #download
    download(url=url, save_path=save_path, file_name=file_name)

    print('[DOWNLOAD FINISHED]')

def download_subreddit(reddit, subreddit_name, save_path, limit) -> None:
    subreddit = reddit.subreddit(subreddit_name)
    
    print('[DOWNLOAD START]')

    for submission in subreddit.hot(limit=limit):
        url = submission.url
        print('Downloading file from '+ url)

        #download
        download(url=url, save_path=save_path, file_name=submission.id)

    print('[DOWNLOAD FINISHED]')


def download_redditor(reddit, redditor_name, save_path, limit) -> None:
    redditor = reddit.redditor(redditor_name)
    
    print('[DOWNLOAD START]')

    for submission in redditor.submissions.hot(limit=limit):
        url = submission.url
        print('Downloading file from '+ url)

        #download
        download(url=url, save_path=save_path, file_name=submission.id)

    print('[DOWNLOAD FINISHED]')