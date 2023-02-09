import requests as req
from bs4 import BeautifulSoup as bs
import re
import os
from slugify import slugify

def index_page(link):
    
    try:
        nombre=slugify(link)
        slug = slugify(req.get(link).content)
        f = open(f'{nombre}.html', "w")
        f.write(slug)
    except:
        pass
    
    return