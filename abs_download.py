import requests
import os

'''
loop over each sale page, saving the content of the web page to disk

https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un
'''

script_folder = os.path.dirname(__file__)

def download_html(list,folder,debug=0):
    if not os.path.exists(folder):        # ensure downloads folder is created
        os.mkdir(folder) 

    for x in list:         # loop over each category in at values
        # print(x['url'])
        for y in range(1,x['page_length']+1):   # load each page url, limit is manually set in varible page length
            url = x['url']+str(y)               # add the page number to the url
            filename = folder + '\\' + x['filename'] + str(y) + '.html'   # build the filename
            if os.path.exists(filename) :       # if file already exists then skip it
                if debug:
                    print(filename,'already exists, skipping')
                continue
            r = requests.get(url, allow_redirects=True) # download the page
            with open(filename,'wb') as f:
                f.write(r.content) # save the web page    
            if debug:
                print(filename,'downloaded')        

