import os
from bs4 import BeautifulSoup

html_folder = os.path.dirname(__file__) + '\\downloads\\'

''' file loader  '''
test_file = html_folder + 'mt1.html'


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
        
        stars = book.find(string=lambda text: "out of 5 stars" in text.lower())          # find the field that contains ""
        dict['stars'] = stars.replace('out of 5 stars','')                      # strip chars
        
        rating = book.find(string=lambda text: "ratings" in text.lower())
        rating = int(str(rating).split()[0].replace(',',''))            
        dict['ratings'] = rating
        
        url = book.find('a',class_='bc-link')
        url = url['href'].split('/')[-1]
        dict['url'] = url
        
        dict['full url'] = 'www.audible.com/pd/'+ url

        book_list.append(dict)
    if debug:
        print(len(book_list),'items processed')
    if debug > 1:
        print('first book is',book_list[0])
    return book_list

