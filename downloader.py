import requests
import os

extension = ('.jpg', '.png', '.gif')
"""list (str): List of supported file extension

Due for some reason, the current download function cannot download file
from embeded third party service.
"""

def download(url: str, save_path: str, file_name: str) -> None:
    '''
    This function takes an URL and download content from it and stores it in
    a given directory with the specified file name
    
    Args:
        url: A content URL
        save_path: A directory path where the content will stored
        file_name: The name of the file to be saved
    
    Returns:
        None
    '''
    file_ext = __get_ext(url)
    
    if file_ext not in extension:
        print(__BColors.FAIL + 'Download error: doesn\'t support "' + file_ext + '" type of extension' + __BColors.ENDC)
        return

    if not os.path.exists(save_path):
        print(__BColors.FAIL + 'Download error: path not found' + __BColors.ENDC)
        return

    file_path = os.path.join(save_path, file_name + file_ext)
    img_data = requests.get(url).content
    with open(file_path, 'wb') as file:
        file.write(img_data)

    print(__BColors.OKGREEN + 'Download success: the file is stored in ' + file_path + __BColors.ENDC)


def __get_ext(url: str) -> str:
    '''
    This function takes an URL and get a file extension from it
    
    Args:
        url: An URL
    
    Returns:
        The file extension
    '''
    splitted_url = os.path.splitext(url)
    file_ext = splitted_url[1]

    if file_ext == '.gifv':
        file_ext = '.webm'

    return file_ext


class __BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'