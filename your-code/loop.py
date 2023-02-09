from slugify import slugify
import requests as req

def index_page(link):
    try:
        contenido = req.get(link).text
        contenido = slugify(contenido)
        with open("paco", "w") as file: # la "a" y el "paco" va por ti Javi
            file.write(contenido)
    except:
        pass