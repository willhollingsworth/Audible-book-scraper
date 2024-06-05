import requests
from pathlib import Path
import os
'''
loop over each sale page, saving the content of the web page to disk

https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un
'''


def download_html(url,debug=0):
    cache_folder = 'cache'
    # set folder based on run location
    if __name__ == '__main__':
        main_dir = Path.cwd().parents[0]
    else:
        main_dir = Path.cwd()

    full_folder_path = main_dir.joinpath(cache_folder)
    print(full_folder_path)

    if not os.path.exists(full_folder_path):        # ensure downloads folder is created
        os.mkdir(full_folder_path) 

    filename = 'test.html'
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
    download_html('https://example.com/')
    # print(Path.cwd())
    # print(Path(__file__).parent)
