import os
from bs4 import BeautifulSoup
import pandas as pd


script_folder = os.path.dirname(__file__)

def process_folder(folder,csvfile,debug=0,overwrite=0,limit=-1):
    '''process htmls into a csv'''
    if os.path.exists(csvfile) and overwrite==0:       # if file already exists then skip it
        if debug: print('csv already exists')
        return
    df = read_folder(folder,debug,limit)      # process folder of htmls, return a df
    df.to_csv(csvfile, index=False)     
    if debug: print('create',csvfile)

def read_folder(folder,debug=0,limit=-1):
    '''read through a folder of html files, outputting a dataframe'''
    df = pd.DataFrame([])
    for file in os.listdir(folder):                     # loop over all downloaded items
        temp_list = read_html(folder+file,debug)              # read each file, convert it to a list with beautiful soup
        temp_df = pd.DataFrame(temp_list)               # list to df
        df = df.append(temp_df)                         # append the new df to the main df
        if limit == 1 : break
        limit -=1
        
    if debug:   
        print(len(df.index),'total books processed')
        print('first book is')
        print(df.iloc[0])
    return df

def read_html(filename,debug=0):
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
        
        stars = book.find(string=lambda text: "out of 5 stars" in text.lower())          # find the field that contains specified characters
        dict['stars'] = stars.replace('out of 5 stars','')                      # strip chars
        
        rating = book.find(string=lambda text: "ratings" in text.lower())
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

if __name__ == '__main__':
    ''' used for further debugging'''
    process_folder(
        script_folder + '\\downloads\\',
        script_folder + '\\books.csv',
        1,
        1,
        1,
    )
    