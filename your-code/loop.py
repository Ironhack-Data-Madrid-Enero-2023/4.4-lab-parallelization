from slugify import slugify 
import requests as req

def index_page(s):
    try:
        html=req.get(s).text
        
        name = slugify(s) + '.txt'
        
        new_file = open(name, 'w')
        
        new_file.write(str(html.encode('utf-8')))
    except:    
        pass
    