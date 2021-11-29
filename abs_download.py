import requests
import os

'''
loop over each sale page, saving the content of the web page to disk

https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un
'''

script_folder = os.path.dirname(__file__)
downloads_folder = script_folder+'\\downloads'
at_values = [{
    'url':'https://www.audible.com/ep/black-friday-week-sale-2021-sff?pageSize=50&page=',
    'page_length':4,
    'filename':'sff'
    },{
    'url':'https://www.audible.com/ep/black-friday-week-sale-2021-mt?pageSize=50&page=',
    'page_length':6,
    'filename':'mt'
}]

if not os.path.exists(downloads_folder):        # ensure downloads folder is created
    os.mkdir(downloads_folder) 

for x in at_values:         # loop over each category in at values
    # print(x['url'])
    for y in range(1,x['page_length']+1):   # load each page url, limit is manually set in varible page length
        url = x['url']+str(y)               # add the page number to the url
        r = requests.get(url, allow_redirects=True) # download the page
        filename = downloads_folder + '\\' + x['filename'] + str(y) + '.html'   # build the filename
        open(filename,'wb').write(r.content)    # save the web page         

