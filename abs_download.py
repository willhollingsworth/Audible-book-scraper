import requests
import os

'''
loop over each sale page, saving the content of the web page to disk

https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un
'''

script_folder = os.path.dirname(__file__)

def download_html(categories, save_directory, debug=0):
    if not os.path.exists(save_directory):  
    for category in categories:      
        content = download_pages(category, save_directory)

def skip_download(path):
    if os.path.exists(path) : return true
        if debug:
            print(path,'already exists', end=', ')
    return false
  
def write_page(content, filename)            
    with open(fullpath,'wb') as f:
        f.write(content) # save the web page    
    if debug:
        print(filename,'downloaded', end=', ')        
               
def save_pages(category, save_directory):
    number_of_pages = category['page_length']
    for pageN in range(1, number_of_pages +1):   
        page_filename = category['filename'] + str(pageN) + '.html'
        filepath = os.path.join(save_directory, page_filename) # Using path join because the remembering the "/" in the right place is prone to breaking
        if skip_download(filepath): continue  
        url = category['url']+str(pageN)              
        r = requests.get(url, allow_redirects=True)
        write_page(r.content, filepath)
    
