import requests
from slugify import slugify

def index_page(link):
    try:
        html = requests.get(link).text
        nombre_arc = slugify(link) +'.html'
        file = open(nombre_arc, 'w')
        file.write(html)
        file.close()
 
    except:
        pass
    