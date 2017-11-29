from html.parser import HTMLParser
from urllib import parse
from urllib.request import urlretrieve
from domain import *


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url,project_name):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.project_name = project_name
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        elif tag == 'img':
            for (attribute, value) in attrs:
                if attribute == 'src':
                    print('image found!: ' + value)
                    filename = value.split('/')[-1]
                    try:
                        urlretrieve(value, self.project_name +"/images/"+ filename)
                    except Exception as e:
                        print(e)



    def page_links(self):
        return self.links

    def error(self, message):
        pass
