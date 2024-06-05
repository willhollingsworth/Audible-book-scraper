

import json

import audible_book_scraper.abs_download as abs_download


#  load urls
with open('urls.json') as r:
    pages_to_download = json.load(r)
first_url = pages_to_download[0]['url']
print('download first url :',first_url)
abs_download.download_html(first_url, debug = True)



