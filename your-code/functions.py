def cuadrado(x):
    return x**2


def index_page2(s):
    try:
        cont = requests.get(s).text
        slug = slugify(s)
        slug+='.html'
        filename = slug
        file = open(filename, 'w')
        file.write(cont)
        file.close()
    except:
        pass