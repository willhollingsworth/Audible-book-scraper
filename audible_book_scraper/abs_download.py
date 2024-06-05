import requests
from pathlib import Path
import os
from urllib.parse import urlparse
'''
Download functions


links
https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse
https://realpython.com/python-pathlib/
'''


def download_html(url,debug=0):
    cache_folder = 'cache'
    # set folder based on run location
    if __name__ == '__main__':
        main_dir = Path.cwd().parents[0]
    else:
        main_dir = Path.cwd()
    full_folder_path = main_dir.joinpath(cache_folder)     # join the cache folder to the path
    if not os.path.exists(full_folder_path):        # ensure cache exists
        os.mkdir(full_folder_path) 
    filename = urlparse(url).path.replace('/','_') + '.html'     # set filename based on url path
    full_path = full_folder_path.joinpath(filename)
    if os.path.exists(full_path) :       # if file already exists then skip it
        if debug:
            print(filename,'already exists', end=', ')
        return
    r = requests.get(url, allow_redirects=True) # download the page
    with open(full_path,'wb') as f:
        f.write(r.content) # save the web page    
    if debug:
        print(filename,'downloaded', end=', ')        

if __name__ == '__main__':
    import json
    with open('../urls.json') as r:
        pages_to_download = json.load(r)
    download_html(pages_to_download[0]['url'], debug= 1)