def index_page(link):

    try:
        response = req.get(link)
        if response.status_code == 200:
            filename = slugify(link) + '.html'
            filepath = 'wikipedia' + filename
            with open(filepath, 'wb') as f:
                f.write(response.content)
    except:
        pass