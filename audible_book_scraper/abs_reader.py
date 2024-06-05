import os
from pathlib import Path

from bs4 import BeautifulSoup
import pandas as pd

import utils

def process_folder(folder,csvfile,debug=0,overwrite=0,limit=-1):
    '''process htmls into a csv'''
    if os.path.exists(csvfile) and overwrite==0:       # if file already exists then skip it
        if debug: 
            print('csv already exists')
        return
    df = read_folder(folder,debug,limit)      # process folder of htmls, return a df
    df.to_csv(csvfile, index=False)     
    if debug: 
        print('create',csvfile)

def read_folder(folder,debug=0,limit=-1):
    '''read through a folder of html files, outputting a dataframe'''
    df = pd.DataFrame([])
    for file in os.listdir(folder):                     # loop over all downloaded items
        temp_list = extract_books_from_html(folder+file,debug)              # read each file, convert it to a list with beautiful soup
        temp_df = pd.DataFrame(temp_list)               # list to df
        df = df.append(temp_df)                         # append the new df to the main df
        if limit == 1 : break
        limit -=1
        
    if debug:   
        print(len(df.index),'total books processed')
        print('first book is')
        print(df.iloc[0])
    return df

def extract_books_from_html(filename,debug=0):
    '''audible html file -> book listing as dictionary items in a list'''
    soup = BeautifulSoup(open(filename, encoding='utf-8'), 'lxml')      # load the file
    books = soup.findAll('li',class_='productListItem')         # find all the book items on the page
    book_list = []

    for book in books:
        dict = {}
        dict['name'] = book.find('h2').get_text()
        
        author = book.find(class_='authorLabel')        # find the first item that matches that class
        author = list(author.children)[1].text          # select the second child        
        author = author.replace('By:','').strip()       # strip out characters
        dict['author'] = author
        
        
        narator = book.find(class_='narratorLabel')        # find the first item that matches that class
        narator = list(narator.children)[1].text          # select the second child        
        narator = narator.replace('Narrated By:','').strip()
        dict['narator'] = narator
        
        stars = book.find(string=lambda text: "out of 5 stars" in text.lower())          # find the field that contains specified characters
        dict['stars'] = stars.replace('out of 5 stars','')                      # strip chars
        
        rating = book.find(string=lambda text: "ratings" in text.lower())
        if rating == None: 
            rating = 0
        else:
            rating = int(str(rating).split()[0].replace(',',''))            
        dict['ratings'] = rating
        
        url = book.find('a',class_='bc-link')
        url = url['href'].split('/')[-1]
        dict['url'] = url
        
        dict['full url'] = 'www.audible.com/pd/'+ url

        book_list.append(dict)
    if debug>1:
        print(len(book_list),'items processed')
    return book_list


def download_first_html_as_xml():
    main_dir = Path.cwd().parents[0]
    cache_folder = main_dir.joinpath('cache')
    first_html_file = list(cache_folder.glob('*.html'))[0]
    xml_folder, xml_filename = 'testing', 'test.xml'
    test_xml_file = main_dir.joinpath(xml_folder, xml_filename)
    utils.convert_html_to_xml(first_html_file,test_xml_file)

if __name__ == '__main__':
    download_first_html_as_xml()

