def index_page(s):
        
    try:
        
        html = req.get(s).text
        
        url = slugify(s)

        file = open(f'{url}.txt', "w", encoding='UTF-8')

        file.write(f'{html}')

        file.close()
        
    except: pass