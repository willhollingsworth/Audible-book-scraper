from bs4 import BeautifulSoup
import os

def convert_html_to_xml(html_file,xml_file):
    soup = BeautifulSoup(open(html_file, encoding='utf-8'), 'lxml')
    xml_file_folder = xml_file.parent
    if not os.path.exists(xml_file_folder):        # ensure cache exists
        os.mkdir(xml_file_folder)       # load the file
    with open(xml_file, 'w', encoding="utf-8") as f:
        f.write(soup.prettify())


if __name__ == '__main__':
    from pathlib import Path
    main_dir = Path.cwd().parents[0]
    cache_folder = main_dir.joinpath('cache')
    first_html_file = list(cache_folder.glob('*.html'))[0]
    xml_full_path = main_dir.joinpath('testing', 'test.xml')    
    convert_html_to_xml(first_html_file,xml_full_path)