import requests as req
import os

from slugify import slugify

unicode=str()

def index_page(s):
    #import requests as req
    #import os
    #from bs4 import BeautifulSoup as bs
    try:
        html2 = req.get(s).text  
        archivo = slugify(s)
    
        with open(archivo, 'w', encoding='utf-8') as file:
            file.write(html2) 
    except:
        pass

import time
from tqdm.notebook import tqdm    # from tqdm import tqdm   # para .py

import multiprocessing as mp

%%time

pool=mp.Pool(12)

res=pool.map(index_page, tqdm(clean_links))
pool.close()